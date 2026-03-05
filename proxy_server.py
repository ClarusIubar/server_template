class ProxyServer:
    """[프록시 서버] 게이트웨이, CORS 검증, 라우팅"""
    def __init__(self, db_instance, cdn_instance):
        self.db = db_instance
        self.cdn = cdn_instance
        self.allowed_origin = "https://my-app.com"

    def dispatch(self, origin: str, action: str, params: dict):
        if origin != self.allowed_origin:
            return "403 Forbidden"

        print(f"  [Log-Proxy] {action} 요청 중계 중...")
        if action == "UPDATE_PROFILE":
            self.db.update_user_img(params['uid'], params['url'])
            return "SUCCESS"
        elif action == "GET_PROFILE":
            user = self.db.find_user(params['uid'])
            if user and user.get("img_url"):
                user["image_data"] = self.cdn.get_static_resource(user["img_url"])
            return user