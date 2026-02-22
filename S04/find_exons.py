from pathlib import Path
from S04.process_exons import get_exons_from_file
def locate_exons(sequence_file, exons_file):
    initial_position = 44,652,852
    pass


if __name__ == "__main__":
    EXON_FILE = "ADA_EXONS.txt"
    FILE = "ADA.txt"
    lines = Path(FILE).read_text().splitlines()
    del lines[0]
    sequence = "".join(lines)
    exons = get_exons_from_file(EXON_FILE)
    print(sequence)