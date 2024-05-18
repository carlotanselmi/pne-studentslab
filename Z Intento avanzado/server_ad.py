import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import http.client
import json
from SeqClass import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def c(ENDPOINT, EXTRA_PARAMS=""):
    SERVER = "rest.ensembl.org"
    PARAMS = f"?{EXTRA_PARAMS}content-type=application/json"

    URL = SERVER + ENDPOINT + PARAMS
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method
    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    # -- Transform it into JSON format
    response = json.loads(data1)
    return response


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def get_geneID(gene_name):
    endpoint = "/xrefs/symbol/homo_sapiens/" + gene_name
    gene_info = c(endpoint)
    id = ""
    for e in gene_info:
        if len(e.get("id")) == 15:
            id = e.get("id")
    return id


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
        arguments = parse_qs(url_path.query)

        content_type = 'text/html'
        json = False
        if arguments.get("json") and arguments.get("json")[0] == "1":
            json = True
        if json:
            content_type = 'application/json'

        contents = ""

        if path == "/":
            # Opens the main page
            contents = Path('welcome.html').read_text()
            # Generating the response message
            self.send_response(200)  # -- Status line: OK!

        else:
            try:
                if path == "/listSpecies":
                    endpoint = "/info/species"
                    species = c(endpoint)

                    all_species = species["species"]
                    limit = arguments.get("limit")
                    if limit:
                        limit = limit[0]
                    else:
                        limit = len(all_species)

                    names = ""
                    for i in range(int(limit)):
                        specie = all_species[i]
                        name = specie["display_name"]
                        names += f"> {name}<br>"

                    if json:
                        contents = json.dumps({"all_species": names})
                    else:
                        contents = read_html_file("listSpecies.html")

                    contents = contents.render(context={"all_species": len(all_species),
                                                        "limit": limit, "names": names})
                    # If the limit written by the user is not an integer: ValueError below

                elif path == "/karyotype":
                    contents = read_html_file("karyotype.html")
                    species_name = arguments.get("species")[0]
                    species_name = species_name.replace(" ", "_")
                    endpoint = f"/info/assembly/{species_name}"
                    species = c(endpoint)

                    karyotype = species["karyotype"]
                    names = ""
                    for k in karyotype:
                        names += f"> {k}<br>"
                    contents = contents.render(context={"species": species_name, "names": names})

                elif path == "/chromosomeLength":
                    contents = read_html_file("chromosome.html")
                    species_name = arguments.get("species")[0].lower()
                    species_name = species_name.replace(" ", "_")
                    endpoint = f"/info/assembly/{species_name}"
                    species = c(endpoint)

                    chromo = arguments.get("chromosome")[0]
                    top_level_region = species.get("top_level_region")
                    length = 0
                    for e in top_level_region:
                        name = e.get("name")
                        coord_system = e.get("coord_system")
                        if coord_system == "chromosome" and name == chromo:
                            length = e.get("length")
                    contents = contents.render(context={"species": species_name, "chromo": chromo, "length": length})

                elif path == "/geneSeq":
                    contents = read_html_file("geneSeq.html")
                    gene_name = arguments.get("gene")[0]
                    id = get_geneID(gene_name)
                    endpoint = f"/sequence/id/{id}"
                    gene = c(endpoint)

                    seq = gene["seq"]
                    contents = contents.render(context={"gene": seq, "name": gene_name})

                elif path == "/geneInfo":
                    contents = read_html_file("geneInfo.html")
                    gene_name = arguments.get("gene")[0]
                    id = get_geneID(gene_name)
                    endpoint = f"/lookup/id/{id}"
                    info = c(endpoint)

                    start = info.get("start")
                    end = info.get("end")
                    chromo = info.get("seq_region_name")
                    length = int(end) - int(start) + 1
                    contents = contents.render(context={"name": gene_name, "start": start, "end": end,
                                                        "len": length, "id": id, "chromo": chromo})

                elif path == "/geneCalc":
                    contents = read_html_file("geneCalc.html")
                    gene_name = arguments.get("gene")[0]
                    id = get_geneID(gene_name)
                    endpoint = f"/sequence/id/{id}"
                    gene = c(endpoint)

                    seq = gene["seq"]
                    seq = Seq(seq)
                    length = seq.len()
                    bases = ["A", "C", "G", "T"]
                    percentages = seq.count_base(bases)
                    contents = contents.render(context={"len": length, "percentages": percentages, "name": gene_name})

                elif path == "/geneList":
                    contents = read_html_file("geneList.html")
                    chromo = arguments.get("chromo")[0]
                    start = arguments.get("start")[0]
                    end = arguments.get("end")[0]
                    endpoint = f"/overlap/region/human/{chromo}:{start}-{end}"
                    extra_params = "feature=gene;feature=transcript;feature=cds;feature=exon;"
                    region = c(endpoint, extra_params)

                    list_genes = []
                    for e in region:
                        if e.get("feature_type") == "gene":
                            if e.get("external_name"):
                                list_genes.append(e.get("external_name"))
                    if len(list_genes) == 0:
                        names = "There are not genes in this region"
                    else:
                        names = ""
                        for gene in list_genes:
                            names += f"> {gene}<br>"
                    contents = contents.render(context={"chromo": chromo, "start": start, "end": end, "genes": names})

                self.send_response(200)

            except (FileNotFoundError, ValueError, TypeError, IndexError, ConnectionRefusedError,
                    KeyError, AttributeError):
                # With any possible error we will get the ERROR page
                contents = Path("error.html").read_text()
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
