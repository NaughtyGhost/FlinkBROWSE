from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import logging

class FlinkBROWSEProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the incoming request
        parsed_path = urlparse(self.path)

        # Basic security: Only allow certain domains (add your own logic here)
        allowed_domains = ['example.com']  # Update this list as needed
        if parsed_path.netloc not in allowed_domains:
            self.send_response(403)  # Forbidden
            self.end_headers()
            self.wfile.write(b'Forbidden: Access to this domain is not allowed.')
            return

        # Create a new request to the target server
        req = Request(self.path)
        req.add_header('User -Agent', self.headers['User -Agent'])

        try:
            # Forward the request to the target server
            response = urlopen(req)

            # Send the response back to the client
            self.send_response(response.getcode())
            for header, value in response.info().items():
                self.send_header(header, value)
            self.end_headers()

            # Send the response body
            self.wfile.write(response.read())
        except HTTPError as e:
            # Handle HTTP errors
            logging.error(f'HTTP error: {e.code} - {e.reason}')
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(f'HTTP error: {e.code} - {e.reason}'.encode())
        except URLError as e:
            # Handle URL errors (e.g., server not found)
            logging.error(f'URL error: {e.reason}')
            self.send_response(502)  # Bad Gateway
            self.end_headers()
            self.wfile.write(b'Bad Gateway: Unable to reach the target server.')
        except Exception as e:
            # Handle other exceptions
            logging.error(f'Unexpected error: {str(e)}')
            self.send_response(500)  # Internal Server Error
            self.end_headers()
            self.wfile.write(b'Internal Server Error: An unexpected error occurred.')

def run_proxy(server_class=HTTPServer, handler_class=FlinkBROWSEProxyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('FlinkBROWSE proxy started on port 8000...')
    httpd.serve_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)  # Set up logging
    run_proxy()
