import http.client

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

print(f"CONTENT main menu: {connect("/")}")
print(f"CONTENT list: {connect("/listSpecies?limit=&list=Send")}")
print(f"CONTENT karyotype: {connect("/karyotype?species=Atlantic+salmon+-+North+American+origin+Brian&get_karyotype=Send")}")
print(f"CONTENT chromosome length: {connect("/chromosomeLength?species=sheep&chromo=2&chromosome_length=Send")}")
print(f"CONTENT gene id: {connect("/geneLookup?gene=FOXP2&lookup=Send")}")
print(f"CONTENT gene seq: {connect("/geneSeq?gene=FOXP2&list=Send")}")
print(f"CONTENT gene info: {connect("/geneInfo?gene=FOXP2&info=Send")}")
print(f"CONTENT gene calcs: {connect("/geneCalc?gene=FOXP2&calc=Send")}")
print(f"CONTENT genes in region: {connect("/geneList?chromo=12&start=20000&end=30000&list=Send")}")
