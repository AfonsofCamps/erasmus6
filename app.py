from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

def run_server():
    port = 8000
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print(f"🚀 Servidor em: http://localhost:{port}")
    webbrowser.open(f'http://localhost:{port}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado")

if __name__ == '__main__':
    run_server()