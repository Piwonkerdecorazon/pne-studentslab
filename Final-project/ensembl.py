import http.client
import json
import termcolor
from Seq1 import Seq
class ensembl:
    """A class for calling the Ensembl API Rest"""
    def __init__(self):
        self.SERVER = 'rest.ensembl.org'
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
        #Ensembl sends a disorganized list, then we need to sort alphabetically every time we access
        def get_display_name(species):
            return species['display_name']
        species = sorted(response['species'], key=get_display_name)
        if limit is None or limit >= len(response['species']):
            for i in range(0, len(response['species'])):
                species_list += (species[i]['display_name'] + "\n")
        else:
            for i in range (0, limit):
                species_list += (response[i]['display_name'] + "\n")

        return species_list

    def check_specie(self, specie):
        valid = False
        species_dict = {}
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

        # Ensembl sends a disorganized list, then we need to sort alphabetically every time we access
        def get_name(species):
            return species['name']

        species_names = sorted(response['species'], key=get_name)

        for i in range(0, len(response['species'])):
            species_dict[species_names[i]['name'].lower()] = species_names[i]['aliases']
        print(species_dict)

        for i in species_dict:
            if specie.replace(' ', '_').lower() in species_dict:
                valid = True
            elif specie.lower() in species_dict[i]:
                valid = True
        return valid
    def check_chrom_database(self, specie):
        valid = True
        chromosome_list = self.karyo(specie).split("\n")
        if chromosome_list == ['']:
            valid = False
        return valid

    def check_chromosome(self, specie, chromosome):
        valid = False
        chromosome_list = self.karyo(specie).split("\n")
        print(chromosome_list)
        if chromosome in chromosome_list:
            valid = True
        else:
            valid = False
        return valid

    def karyo(self, specie):
        karyotype = ""

        #Check if the specie is in the database


        ENDPOINT = '/info/assembly/' + specie.replace(' ', '_').lower()
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
        for i in range (0, len(response['karyotype'])):
            karyotype += (response['karyotype'][i] + "\n")
        return karyotype


    def chrom_length(self, specie, chromosome):
        chromosome_length = 0
        ENDPOINT = '/info/assembly/' + specie.replace(' ', '_').lower()
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
        chromosome_list = self.karyo(specie).split("\n")
        if chromosome in chromosome_list:
            target = chromosome
        else:
            return "No chromosome found"

        for i in response['top_level_region']:
            if i['name'] == target:
                chromosome_length = i['length']
        return str(chromosome_length)
