import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq
import jinja2 as j
from ensembl import ensembl

e = ensembl()
s = Seq()
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
        contents = Path('html/main.html').read_text()
        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        valid = True
        if arguments == {}:
            if path == "/":
                contents = Path('html/main.html').read_text()
            else:
                contents = Path('html/Error.html').read_text()
        else:
            if 'list' in arguments:
                if 'limit' in arguments:
                    try:
                        int(arguments['limit'][0])
                        valid = True
                    except:
                        valid = False
                    if valid == True:
                        limit = int(arguments['limit'][0])
                        contents = read_html_file("list.html").render(context={"list": e.list(limit), "limit": limit})
                    else:
                        contents = Path('html/Error.html').read_text()
                else:
                    contents = read_html_file("list.html").render(context={"list": e.list(), "limit": "not defined by the user"})
            if 'get_karyotype' in arguments:
                if 'species_karyotype' in arguments:
                    if e.check_specie(arguments['species_karyotype'][0]) == True:
                        contents = read_html_file("karyotype.html").render(context=
                        {
                            "karyotype": e.karyo(arguments['species_karyotype'][0]),
                            "specie": arguments['species_karyotype'][0]
                        })
                    else:
                        contents = Path('html/Error.html').read_text()
                else:
                    contents = Path('html/Error.html').read_text()
            if 'chromosome_length' in arguments:
                if ('chromosome_species' in arguments) and ('chromosome_name' in arguments):
                    if e.check_specie(arguments['chromosome_species'][0]) == True:
                        if e.check_chrom_database(arguments['chromosome_species'][0]) == True: #Check if said species has its karyotype sequenced
                            if e.check_chromosome(arguments['chromosome_species'][0], arguments['chromosome_name'][0]) == True: #Check if the chromosome is in the karyotype
                                contents = read_html_file("chromosome.html").render(context=
                                {
                                    "length": e.chrom_length(arguments['chromosome_species'][0], arguments['chromosome_name'][0])
                                })
                            else:
                                contents = Path('html/Error.html').read_text()
                        else:
                            contents = Path('html/Error.html').read_text()
                    else:
                        contents = Path('html/Error.html').read_text()
                else:
                    contents = Path('html/Error.html').read_text()


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
