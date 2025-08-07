#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os

# Configuration
PORT = 8000
CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

class HTTPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.socket = ssl.wrap_socket(
            self.socket,
            certfile=CERT_FILE,
            keyfile=KEY_FILE,
            server_side=True
        )

if __name__ == '__main__':
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create HTTPS server
    httpd = HTTPServer(('0.0.0.0', PORT), http.server.SimpleHTTPRequestHandler)
    
    print(f"🚀 HTTPS Server running on https://localhost:{PORT}")
    print(f"📱 Access from phone: https://192.168.0.169:{PORT}")
    print("⚠️  Note: You'll see a security warning - click 'Advanced' then 'Proceed'")
    print("🛑 Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.shutdown() 