import asyncio

class ClientServer:
    def __init__(self, proxy, storage):
        self.proxy = proxy
        self.storage = storage
        self.origin = "https://my-app.com"

    async def user_action_flow(self, uid: str):
        print(f"\n[*] Client Scenario Start: {uid}")
        
        # 1. 업로드
        path = await self.storage.upload(f"RAW_DATA_OF_{uid}")
        
        # 2. 업데이트
        await self.proxy.handle_request(self.origin, "UPDATE_PROFILE", {"uid": uid, "path": path})
        
        # 3. 조회 및 검증
        profile = await self.proxy.handle_request(self.origin, "GET_PROFILE", {"uid": uid})
        
        # 💡 KeyError 방지: 데이터 존재 확인 후 출력
        if profile and 'uid' in profile:
            url = profile.get('full_url', 'N/A')
            print(f"[*] Client Received Profile: {profile['uid']} | URL: {url}")
        else:
            print(f"[!] Error: Profile for {uid} not found or invalid response.")