from pathlib import Path
from unittest import skip


def get_exons_from_file(filename):
    lines = Path(filename).read_text().splitlines()
    exon = ""
    exon_list = []
    for i in range (0, len(lines)):
        if lines[i].startswith(">"):
            if lines[i] == lines[0]:
                pass
            else:
                exon_list.append(exon)
                exon = ""

        else:
            exon = exon + lines[i]

    return exon_list

if __name__ == "__main__":
    FILENAME = "ADA_EXONS.txt"
    exons = get_exons_from_file(FILENAME)
    print(exons)
