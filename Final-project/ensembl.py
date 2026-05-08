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
            for i in range(0, len(response['species']) - 1):
                species_list += (species[i]['display_name'] + "\n")
        else:
            for i in range (0, limit-1):
                species_list += (species[i]['display_name'] + "\n")

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
                print("it is name")
            elif specie.lower() in species_dict[i]:
                valid = True
                print("it is an alias")
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

        #If the user introduced an alias of the specie, get their name to look for a karyotype
        specie_name = self.get_name_from_alias(specie)

        ENDPOINT = '/info/assembly/' + specie_name.replace(' ', '_').lower()
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

    def get_name_from_alias(self, specie):
        name = ""
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

        if specie.replace(' ', '_').lower() in species_dict:
            name = specie
            print("it is name")
        for i in species_dict:
            if specie.lower() in species_dict[i]:
                name = i
                print("it is an alias")
        return name

    """
    
    This section further on corresponds to the methods used in the intermediate level:
    Human gene browsing
    
    """
    def get_gene_id(self, gene):
        ENDPOINT = '/lookup/symbol/homo_sapiens/' + gene
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
        gene_id = response['id']
        return gene_id

    def get_gene_seq(self, gene):
        ENDPOINT = '/sequence/id/' + self.get_gene_id(gene)
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
        gene_seq = response['seq']
        return gene_seq

    def get_gene_info(self, gene):
        ENDPOINT = '/lookup/id/' + self.get_gene_id(gene)
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
        gene_info = {"start": response["start"], "end": response["end"],"length": response["length"]}
        return gene_info
    def get_gene_calcs(self, gene):
        output = ""
        sequence = self.get_gene_seq(gene)
        s = Seq(sequence)
        seq_count = s.count()
        totalCount = 0
        for i in seq_count:
            totalCount += seq_count[i]
        output = "The total of bases is: " + str(totalCount) + "\n"
        for i in seq_count:
            print(i + ": " + str(seq_count[i]) + " (" + str(seq_count[i] / totalCount * 100) + "%)")
        return output
e = ensembl()
print(e.get_name_from_alias('shrew mouse'))
print(e.get_gene_id('ADA'))