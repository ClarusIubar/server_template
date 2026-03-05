# main.py
from storage_server import StorageServer
from database_server import DatabaseServer
from cdn_server import CDNServer
from proxy_server import ProxyServer
from client_server import ClientServer

def bootstrap():
    """시스템 부팅 및 의존성 주입(Dependency Injection)"""
    # 1. 하위 인프라 생성
    storage = StorageServer()
    db = DatabaseServer()
    
    # 2. 미들웨어 생성 (하위 인프라 주입)
    cdn = CDNServer(storage)
    
    # 3. 게이트웨이 생성 (DB, CDN 주입)
    proxy = ProxyServer(db, cdn)
    
    # 4. 클라이언트 생성 (프록시, 스토리지 주입)
    client = ClientServer(proxy, storage)
    
    # 시나리오 실행
    client.run_scenario("user_01")

if __name__ == "__main__":
    bootstrap()