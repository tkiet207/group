from http.server import ThreadingHTTPServer
from backend.config import HOST, PORT
from backend.database import init_and_seed_db
from backend.router import Tech2HandRequestHandler


def main():
    init_and_seed_db()
    server = ThreadingHTTPServer((HOST, PORT), Tech2HandRequestHandler)
    print("=" * 64)
    print("  TECH2HAND - SAN THUONG MAI DIEN TU CONG NGHE CU & SECOND-HAND")
    print(f"  Dang chay tai: http://{HOST}:{PORT}")
    print("  Nhan Ctrl+C de dung may chu.")
    print("=" * 64)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung may chu Tech2Hand.")
        server.server_close()


if __name__ == "__main__":
    main()