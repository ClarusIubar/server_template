class DatabaseServer:
    """[DB 서버] CQRS 패턴 적용 - 조회와 명령 분리"""
    def __init__(self):
        self._master = {"user_01": {"id": "user_01", "name": "Gemini", "img_url": None}}
        self._replica = self._master.copy()

    def update_user_img(self, uid: str, url: str):
        if uid in self._master:
            self._master[uid]["img_url"] = url
            self._replica = self._master.copy() # 동기화 시뮬레이션
            print(f"  [Log-DB] Command: {uid} 이미지 경로 업데이트")

    def find_user(self, uid: str) -> dict:
        print(f"  [Log-DB] Query: Replica에서 {uid} 조회")
        return self._replica.get(uid, {})