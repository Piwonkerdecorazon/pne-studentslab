from pathlib import Path
from S04.process_exons import get_exons_from_file
def locate_exons(FILE, EXON_FILE, first_base):
    lines = Path(FILE).read_text().splitlines()
    del lines[0]
    sequence = "".join(lines)
    exons = get_exons_from_file(EXON_FILE)
    exon_position_data = {}
    for i in range (0, len(exons)):
        exon_data = {"Exon "+ str(i+1):
                         {
                         "Exon": i+1,
                         "Length": len(exons[i]),
                         "Start": first_base - sequence.find(str(exons[i])),
                         "End": first_base - sequence.find(str(exons[i])) - len(exons[i])}}
        exon_position_data.update(exon_data)
    return exon_position_data



if __name__ == "__main__":
    exon_file = "ADA_EXONS.txt"
    file = "ADA.txt"
    initial_position = 44652852
    print("Exons           Long.           Start           End \n--------------------------------------------------------------")
    exon_dictionary = locate_exons(file, exon_file, initial_position)
    for i in range (0, len(exon_dictionary)):
        print(str(exon_dictionary["Exon "+ str(i+1)]["Exon"]) +
              "               "[:-len(str(exon_dictionary["Exon "+ str(i+1)]["Exon"]))] + "¡" +

              str(exon_dictionary["Exon "+ str(i+1)]["Length"]) +
              "               "[:-len(str(exon_dictionary["Exon "+ str(i+1)]["Length"]))] + "¡" +

              str(exon_dictionary["Exon "+ str(i+1)]["Start"]) +
              "               "[:-len(str(exon_dictionary["Exon "+ str(i+1)]["Start"]))] + "¡" +

              str(exon_dictionary["Exon "+ str(i+1)]["End"])
              + "             "[:-len(str(exon_dictionary["Exon "+ str(i+1)]["End"]))] + "¡" )
