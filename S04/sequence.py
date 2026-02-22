from pathlib import Path
from S03.dna_count_file_corrected import count_bases_file
FILENAME = "ADA.txt"

lines = Path(FILENAME).read_text().splitlines()
del lines[0]
print(count_bases_file(lines))