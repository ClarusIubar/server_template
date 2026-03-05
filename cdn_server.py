import asyncio

class CDNServer:
    def __init__(self, storage_ref):
        self.storage = storage_ref
        self.edge_cache = {}

    async def fetch_content(self, path: str) -> str:
        # 캐시 히트 시 I/O 지연 없음
        if path in self.edge_cache:
            print(f"  [CDN] Cache Hit: {path}")
            return self.edge_cache[path]
        
        # 캐시 미스 시 비동기 네트워크 I/O 발생
        print(f"  [CDN] Cache Miss: Fetching from Origin...")
        data = await self.storage.download(path)
        self.edge_cache[path] = data
        return data