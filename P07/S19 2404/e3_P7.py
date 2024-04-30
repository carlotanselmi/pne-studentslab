import http.client
import termcolor
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
ID = "/ENSG00000207552"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + ID + PARAMS

print(f"\nServer: {SERVER}\nURL: {URL}")
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method.
try:
    conn.request("GET", ENDPOINT + ID + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
person = json.loads(data1)

# -- Print the received data
termcolor.cprint('Gene', 'green', force_color=True, end="")
print(": MIR633")
termcolor.cprint('Description', 'green', force_color=True, end="")
print(f': {person["desc"]}')
termcolor.cprint('Bases', 'green', force_color=True, end="")
print(f': {person ["seq"]}')
