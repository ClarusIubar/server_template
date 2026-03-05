import uuid

class StorageServer:
    """[스토리지 서버] 비정형 데이터(이미지) 저장 담당"""
    def __init__(self):
        self._disk = {}

    def upload(self, content: str) -> str:
        file_id = uuid.uuid4().hex[:8]
        url = f"https://cdn.myapp.com/assets/{file_id}.png"
        self._disk[url] = content
        print(f"  [Log-Storage] 파일 저장 완료: {url}")
        return url

    def download(self, url: str) -> str:
        return self._disk.get(url, "404 Not Found")