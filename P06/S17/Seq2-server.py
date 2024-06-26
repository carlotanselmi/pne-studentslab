import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from P06.S17.Seq1 import *

seq = ["GATCGATCGAGT", "CCAGCGATGCGG", "TCTATCGTGGCA", "ATCGGGCACTGA", "TCGACGCATCGT"]
genomes = {'U5': '../Genome Sequences/U5.fa', 'ADA': '../Genome Sequences/ADA.fa',
           'FRAT1': '../Genome Sequences/FRAT1.fa', 'RNU6_269P': '../Genome Sequences/RNU6_269P.fa',
           'FXN': '../Genome Sequences/FXN.fa'}


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green', force_color=True)

        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/":
            # Opens the main page
            contents = Path("../html/index.html").read_text()
            # Generating the response message
            self.send_response(200)  # -- Status line: OK!

        elif path == "/ping":  # Exercise 1
            contents = Path("../html/ping.html").read_text()
            self.send_response(200)

        elif path == "/get":  # Exercise 2
            query = urlparse(self.path).query
            params = parse_qs(query)
            number = params.get('number', [''])[0]
            sequence = seq[int(number)]
            contents = read_html_file("../html/get.html").render(context={"number": number, "sequence": sequence})
            self.send_response(200)

        elif path == "/gene":  # Exercise 3
            query = urlparse(self.path).query
            params = parse_qs(query)
            gene = params.get('gene', [''])[0]
            if gene in genomes:
                s = Seq()
                sequence = s.read_fasta(genomes[gene])
            else:
                sequence = f"Invalid gene name: {gene}"
            contents = read_html_file("../html/gene.html").render(context={"gene": gene, "sequence": sequence})
            self.send_response(200)

        elif path == "/operation":  # Exercise 4
            query = urlparse(self.path).query
            params = parse_qs(query)
            sequence = params.get('msg', [''])[0]
            if "info" == params.get('operation', [''])[0]:
                operation = "info"
                s = Seq(sequence)
                length = s.len()
                count = s.count()
                result = f"Total length: {length}\n"
                for key, value in count.items():
                    percentage = round((value / length) * 100, 1)
                    result += f"{key}: {value} ({percentage}%)\n"
            elif "comp" == params.get('operation', [''])[0]:
                operation = "comp"
                s = Seq(sequence)
                result = s.complement()
            elif "rev" == params.get('operation', [''])[0]:
                operation = "rev"
                s = Seq(sequence)
                result = s.reverse()
            contents = read_html_file("../html/operation.html").render(context={"sequence": sequence,
                                                                             "operation": operation, "result": result})
            self.send_response(200)

        else:
            contents = Path("../html/error.html").read_text()
            self.send_response(404)

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
