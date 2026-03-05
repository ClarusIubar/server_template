class CDNServer:
    """[CDN 서버] 프록시 캐시를 통한 지리적 가속"""
    def __init__(self, storage_instance):
        self.storage = storage_instance
        self.cache = {}

    def get_static_resource(self, url: str) -> str:
        if url in self.cache:
            print(f"  [Log-CDN] Cache Hit!")
            return self.cache[url]
        
        print(f"  [Log-CDN] Cache Miss! 스토리지 접근")
        data = self.storage.download(url)
        self.cache[url] = data
        return data