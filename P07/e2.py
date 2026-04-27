# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
genes = {"FRAT1": "", "ADA": "", "FXN": "", "RNU6-269P": "", "MIR633": "",
         "TTTY4C": "", "RBMY2YP": "", "FGFR3": "", "KDR": "", "ANK2": ""}

# Connect with the server
conn = http.client.HTTPConnection(SERVER)
for i in genes:
    ENDPOINT = '/lookup/symbol/homo_sapiens/' + i
    PARAMS = '?content-type=application/json;expand=1'
    URL = "https://" + SERVER + ENDPOINT + PARAMS
    print(f"\nConnecting to server: {SERVER}")
    print(f"\nURL: {URL}")
    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", ENDPOINT+PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    genes[i] = response['id']

print(genes)
