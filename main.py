import asyncio
import os

# 1. 운영 레벨 설정 위임 (IaC 가상화)
# 프록시 서버가 참조할 외부 도메인과 포트를 환경 변수로 주입합니다.
os.environ["SERVICE_DOMAIN"] = "prod-api.gemini.io"
os.environ["SERVICE_PORT"] = "8443"

# 2. 각 서버 모듈 임포트
from storage_server import StorageServer
from database_server import DatabaseServer
from cdn_server import CDNServer
from proxy_server import ProxyServer
from client_server import ClientServer

async def main():
    """
    시스템 부팅 및 의존성 주입 (Dependency Injection)
    """
    print("=== [Infrastructure] 시스템 부팅 및 서버 배치 시작 ===")

    # [Layer 1] 하부 인프라 구축
    storage = StorageServer()
    db = DatabaseServer()
    
    # [Layer 2] 미들웨어 및 가속 계층 (스토리지 의존성 주입)
    cdn = CDNServer(storage)
    
    # [Layer 3] 제어 및 게이트웨이 계층 (DB, CDN 의존성 주입)
    proxy = ProxyServer(db, cdn)
    
    # [Layer 4] 사용자 인터페이스 계층 (프록시, 스토리지 의존성 주입)
    client = ClientServer(proxy, storage)

    print("=== [Traffic] 비동기 병렬 요청 처리 시작 ===\n")

    # 3. 비동기 병렬 실행 (asyncio.gather)
    # 여러 사용자가 동시에 접속해도 I/O Blocking 없이 처리되는지 확인합니다.
    try:
        await asyncio.gather(
            client.user_action_flow("user_01"),
            client.user_action_flow("user_02"),
            client.user_action_flow("user_03") # 추가 테스트 케이스
        )
    except Exception as e:
        print(f"\n[Runtime Error] 시스템 가동 중 예상치 못한 오류 발생: {e}")

    print("\n=== [Infrastructure] 모든 시나리오 완료 및 서버 종료 ===")

if __name__ == "__main__":
    # 파이썬 3.7+ 공식 비동기 실행 방식
    asyncio.run(main())