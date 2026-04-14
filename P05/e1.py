import http.server
import socketserver
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True
Handler = http.server.SimpleHTTPRequestHandler


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")
        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')
        # Print the command received (should be GET)
        print("  Command: " + self.command)
        # Print the resource requested (the path)
        print("  Path: " + self.path)

        path_list = ["/info/A", "/info/G", "/info/C", "/info/T", "/","/index"]

        if self.path in path_list:
            if self.path == "/" or self.path == "/index":
                body = Path("html" + "/index" + ".html").read_text()
            else:
                body = Path("html" + self.path + ".html").read_text()
        else:
            body = Path("html/Error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(body.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(body.encode())

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

