import http.client
import json
import termcolor
##http://127.0.0.1:8080/karyotype?species=human&get_karyotype=Send
PORT = 8080
SERVER = 'localhost:8080'
def connect(ENDPOINT, EXTRA_PARAMS = None):
    if "?" in ENDPOINT:
        separator = "&"
    else:
        separator = "?"
    if EXTRA_PARAMS == None:
        path = ENDPOINT + separator+ "json=1"
    else:
        path = ENDPOINT + EXTRA_PARAMS + separator + "json=1"
    URL = "https://" + SERVER + path

    print(f"\nConnecting to server: {SERVER}")
    print(f"\nURL: {URL}")
    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)
    try:
        if EXTRA_PARAMS == None:
            conn.request("GET", path)
        else:
            conn.request("GET", path)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    return data1

print(f"CONTENT: {connect("/geneList?chromo=9&start=22125500&end=22146000&json=1")}")