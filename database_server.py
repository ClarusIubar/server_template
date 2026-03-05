import asyncio

class DatabaseServer:
    def __init__(self):
        # 💡 데이터 규격 통일: 'id' 대신 'uid' 사용
        self._master = {"user_01": {"uid": "user_01", "name": "Gemini", "img_path": None},
                        "user_02": {"uid": "user_02", "name": "User2", "img_path": None}}
        self._replica = self._master.copy()

    async def execute_command(self, uid: str, path: str):
        await asyncio.sleep(0.3)
        if uid in self._master:
            self._master[uid]["img_path"] = path
            self._replica = self._master.copy() 
            print(f"  [DB-Command] User {uid} path updated.")

    async def execute_query(self, uid: str) -> dict:
        await asyncio.sleep(0.1)
        # 💡 안전한 반환: 결과가 없을 경우 빈 딕셔너리 반환
        result = self._replica.get(uid, {})
        print(f"  [DB-Query] Fetching user {uid} from Replica.")
        return result