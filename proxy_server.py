import os

class ProxyServer:
    def __init__(self, db, cdn):
        self.db = db
        self.cdn = cdn
        self.external_domain = os.getenv("SERVICE_DOMAIN", "api.myapp.com")
        self.external_port = os.getenv("SERVICE_PORT", "443")
        self.base_url = f"https://{self.external_domain}:{self.external_port}"

    async def handle_request(self, origin: str, action: str, payload: dict):
        if origin != "https://my-app.com": return None

        if action == "GET_PROFILE":
            user = await self.db.execute_query(payload['uid'])
            # 💡 방어적 코드: 유저 데이터가 존재하는지 확인
            if user and "uid" in user:
                if user.get("img_path"):
                    user["full_url"] = f"{self.base_url}/{user['img_path']}"
                    user["bin_data"] = await self.cdn.fetch_content(user["img_path"])
                else:
                    user["full_url"] = "No Image"
                return user
            return None # 404 Not Found 역할
        
        elif action == "UPDATE_PROFILE":
            await self.db.execute_command(payload['uid'], payload['path'])
            return "SUCCESS"