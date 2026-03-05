import asyncio
import uuid
import os

class StorageServer:
    def __init__(self):
        # 운영 레벨 위임: 저장 경로나 클러스터 ID는 환경 변수에서 가져옴
        self.node_id = os.getenv("NODE_ID", "storage-node-01")
        self._disk = {}

    async def upload(self, content: str) -> str:
        """비동기 디스크 I/O 시뮬레이션"""
        await asyncio.sleep(0.5) # I/O Latency
        # 하드코딩된 URL이 아닌 '내부 상대 경로'만 반환
        internal_path = f"assets/{self.node_id}/{uuid.uuid4().hex[:8]}.png"
        self._disk[internal_path] = content
        print(f"  [Storage] Data saved at: {internal_path}")
        return internal_path

    async def download(self, path: str) -> str:
        await asyncio.sleep(0.2)
        return self._disk.get(path, "404 Not Found")