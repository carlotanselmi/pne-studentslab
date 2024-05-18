import http.server
import http.client
import json


def client(ENDPOINT, PARAMS=""):
    PORT = 8080
    SERVER = 'localhost'

    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method
    try:
        conn.request("GET", ENDPOINT + f'?{PARAMS}json=1')
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


def read_response(response):
    if "error" in response:
        print(f"Error: {response['error']}")
    else:
        return response


def listSpecies(limit=None):
    if limit:
        PARAMS = f"limit={limit}&"  # WITH &?
    else:
        PARAMS = ""

    response = client("/listSpecies", PARAMS)
    response = read_response(response)
    if response:
        all_species = response.get("all_species")
        print(f"LIST OF SPECIES\nThe limit you have selected is: {limit}\nThe names of the species are:\n")
        for name in all_species:
            print(f"> {name}")


def karyotype(species):
    response = client("/karyotype", f"species={species}&")
    response = read_response(response)
    if response:
        print(f"KARYOTYPE\nSelected species: {species}\nThe names of the CHROMOSOMES are:\n")
        karyotype = response.get("karyotype")
        for chromosome in karyotype:
            print(f"> {chromosome}")


def chromosome(species, chromo):
    response = client("/chromosomeLength", f"species={species}&chromo={chromo}&")
    response = read_response(response)
    if response:
        length = response.get("length")
        print(f"LENGTH OF THE SELECTED CHROMOSOME\n"
              f"Selected species: {species}\nThe length of the chromosome {chromo} is: {length}")


def geneSeq(gene):
    response = client("/geneSeq", f"gene={gene}&")
    response = read_response(response)
    if response:
        seq = response.get("seq")
        print(f"SEQUENCE OF A HUMAN GENE\nSelected Gene: {gene}\n {seq}")


def geneInfo(gene):
    response = client("/geneInfo", f"gene={gene}&")
    response = read_response(response)
    if response:
        print(f"INFORMATION OF A HUMAN GENE\nSelected Gene: {gene}\n")
        for key in response:
            print(f"{key.capitalize()}: {response.get(key)}")


def geneCalc(gene):
    response = client("/geneCalc", f"gene={gene}&")
    response = read_response(response)
    if response:
        print(f"CALCULATIONS ON A HUMAN GENE\nSelected Gene: {gene}\n")
        for key in response:
            print(f"{key.capitalize()}: {response.get(key)}")


def geneList(chromo, start, end):
    response = client("/geneList", f"chromo={chromo}&start={start}&end={end}&")
    response = read_response(response)
    if response:
        genes = response.get("genes")
        print(f"GENES LOCATED IN A CHROMOSOME REGION\nSelected Chromosome: {chromo}"
              f"Start: {start}\nEnd: {end}\nLIST OF GENES:\n")
        for gene in genes:
            print(f"> {gene}")



listSpecies(10)
#list_species()
#karyotype("mouse")
#chromosome_length("mouse", "18")
#gene_sequence("FRAT1")
#geneInfo("FRAT1")
#geneCalc("FRAT1")
#geneList("9", 22125500, 22136000)

#igual añadir que las keys de los diccionarios sean los nombres de los genes