#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os
import subprocess

# Configuration
PORT = 8444  # Using another port
CERT_FILE = 'trusted_cert.pem'
KEY_FILE = 'trusted_key.pem'

def create_trusted_cert():
    """Create a certificate that might work better on mobile"""
    if not os.path.exists(CERT_FILE):
        print("Creating trusted certificate...")
        # Create certificate with better settings for mobile browsers
        cmd = [
            'openssl', 'req', '-x509', '-newkey', 'rsa:2048',
            '-keyout', KEY_FILE, '-out', CERT_FILE,
            '-days', '365', '-nodes',
            '-subj', '/C=US/ST=CA/L=San Francisco/O=Development/CN=192.168.0.169',
            '-addext', 'subjectAltName=DNS:192.168.0.169,IP:192.168.0.169,IP:127.0.0.1'
        ]
        subprocess.run(cmd, check=True)
        print("Certificate created!")

# Create a simple HTTPS server
class HTTPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        # Create SSL context with better settings
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(CERT_FILE, KEY_FILE)
        context.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384')
        self.socket = context.wrap_socket(self.socket, server_side=True)

if __name__ == '__main__':
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create trusted certificate
    create_trusted_cert()
    
    # Create HTTPS server
    httpd = HTTPServer(('0.0.0.0', PORT), http.server.SimpleHTTPRequestHandler)
    
    print(f"🚀 Trusted HTTPS Server running on https://localhost:{PORT}")
    print(f"📱 Access from phone: https://192.168.0.169:{PORT}")
    print("⚠️  Note: You'll see a security warning - click 'Advanced' then 'Proceed'")
    print("🛑 Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.shutdown() 