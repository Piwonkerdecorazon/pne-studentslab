from pathlib import Path

FILENAME = "U5.txt"

lines = Path(FILENAME).read_text().splitlines()

for i in range(1, len(lines)):
    print(lines[i])