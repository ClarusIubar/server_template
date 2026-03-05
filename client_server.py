class ClientServer:
    """[클라이언트 서버] UI 및 사용자 요청 시작점"""
    def __init__(self, proxy_instance, storage_instance):
        self.proxy = proxy_instance
        self.storage = storage_instance
        self.origin = "https://my-app.com"

    def run_scenario(self, uid: str):
        print(f"\n[Client] 1. 이미지 업로드")
        url = self.storage.upload("PNG_DATA_001")
        
        print(f"\n[Client] 2. 프로필 업데이트 요청")
        self.proxy.dispatch(self.origin, "UPDATE_PROFILE", {"uid": uid, "url": url})
        
        print(f"\n[Client] 3. 프로필 조회 (최초)")
        res = self.proxy.dispatch(self.origin, "GET_PROFILE", {"uid": uid})
        print(f"  >> 결과: {res}")