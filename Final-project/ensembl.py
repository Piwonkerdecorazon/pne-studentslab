import http.client
import json
import termcolor
from Seq1 import Seq
class ensembl:
    """A class for calling the Ensembl API Rest"""
    def __init__(self):
        self.SERVER = 'rest.ensembl.org'
        self.ENDPOINT = '/info/species'
        self.PARAMS = '?content-type=application/json'

    def list(self, limit=None):
        species_list = ""
        ENDPOINT = '/info/species'
        URL = "https://" + self.SERVER + ENDPOINT + self.PARAMS
        print(f"\nConnecting to server: {self.SERVER}")
        print(f"\nURL: {URL}")
        # Connect with the server
        conn = http.client.HTTPConnection(self.SERVER)
        try:
            conn.request("GET", ENDPOINT + self.PARAMS)
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
        if limit is None or limit >= len(response['species']):
            for i in range(0, len(response['species'])):
                print(str(len(response['species'])))
                species_list += (response['species'][i]['display_name'] + "\n")
        else:
            for i in range (0, limit):
                species_list += (response['species'][i]['display_name'] + "\n")

        return species_list
