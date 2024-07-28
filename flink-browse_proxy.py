from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.parse import urlparse

class FlinkBROWSEProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the incoming request
        parsed_path = urlparse(self.path)

        # Create a new request to the target server
        req = Request(self.path)
        req.add_header('User-Agent', self.headers['User-Agent'])

        # Forward the request to the target server
        response = urlopen(req)

        # Send the response back to the client
        self.send_response(response.getcode())
        for header, value in response.info().items():
            self.send_header(header, value)
        self.end_headers()

        # Send the response body
        self.wfile.write(response.read())

def run_proxy(server_class=HTTPServer, handler_class=FlinkBROWSEProxyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('FlinkBROWSE proxy started on port 8000...')
    httpd.serve_forever()

if __name__ == "__main__":
    run_proxy()
