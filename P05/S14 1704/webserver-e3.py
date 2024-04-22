import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green', force_color=True)

        # Extract the path from the request
        path = self.path.strip('/')

        # Set the default filename to error.html
        filename = 'error.html'
        status_code = 404

        # Try to open the requested file
        try:
            with open(path, 'rb') as file:
                contents = file.read()
            filename = path
            status_code = 200
        except FileNotFoundError:
            contents = b'File not found'

        self.send_response(status_code)
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents))
        # The header is finished
        self.end_headers()
        # Send the response message
        self.wfile.write(contents)

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
