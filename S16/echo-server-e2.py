import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green', force_color=True)

        path = urlparse(self.path).path

        if path == "/" or path.startswith("/echo"):
            if path == "/":
                contents = Path('html/form-e2.html').read_text()
            else:
                query = urlparse(self.path).query
                arguments = parse_qs(query)
                message = arguments.get('msg', [''])[0]
                check = arguments.get('chk', [''])[0]
                if check == 'on':
                    message = message.upper()
                contents = f"""<!DOCTYPE html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>RESULT</title>
                      </head>
                      <body>
                        <h1>Received message:</h1>
                        <p>{message}</p>
                        <a href="http://127.0.0.1:8080/">Main page</a>
                      </body>
                    </html>"""
        else:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
