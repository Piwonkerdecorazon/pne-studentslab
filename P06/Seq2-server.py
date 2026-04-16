import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from S03.dna_count_file import totalBases
from Seq1 import Seq
import jinja2 as j

S1 = Seq("ATGCGTACTGCTAGCTAGCT")
S2 = Seq("CGGATTCGATCGATAGCTAG")
S3 = Seq("TTTAGCGATCGATCGATCGA")
S4 = Seq("GACGTACGTACGTACGTACG")
file_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

s = Seq()
sequence_list = [S1, S2, S3, S4]
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        print(arguments)
        print(path)
        contents = Path('html/index.html').read_text()
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        valid = True
        if arguments == {}:
            if path == "/":
                contents = Path('html/index.html').read_text()
            else:
                contents = Path('html/Error.html').read_text()
        else:
            if 'ping' in arguments:
                contents = Path('html/ping.html').read_text()
            elif 'get sequence' in arguments:
                contents = read_html_file("Sequence.html").render(context={"number": arguments['Seq number'][0], "sequence": sequence_list[int(arguments['Seq number'][0])-1]})  # provide a dictionary to build the form
            elif 'get gene' in arguments:
                print("../gene_files/" + str(arguments['Gene'][0]) + ".txt")
                s.read_fasta("../gene_files/" + str(arguments['Gene'][0]) + ".txt")
                print(s)
                contents = read_html_file("Gene.html").render(context={"name": arguments['Gene'][0], "gene": s})  # provide a dictionary to build the form
            elif 'operate' in arguments:
                user_sequence = arguments['sequence'][0]
                s(user_sequence)
                output = ""
                operation = ""
                if 'info' in arguments:
                    seq_count = s.count()
                    totalCount = 0
                    for i in seq_count:
                        output += i + ": " + str(seq_count[i]) + "\n"
                        totalCount += seq_count[i]
                    output += str(totalCount) + "\n"
                    operation = "info"
                elif 'reverse' in arguments:
                    output = s.reverse()
                    operation = "reverse"
                elif 'complementary' in arguments:
                    output = s.reverse()
                    operation = "reverse"
                contents = read_html_file("Gene.html").render(context={
                    "input seq": s,
                    "operation": operation,
                    "output seq": output

                })  # provide a dictionary to build the form







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
