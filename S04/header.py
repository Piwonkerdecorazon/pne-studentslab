from pathlib import Path

FILENAME = "RNU6_269P.txt"

lines = Path(FILENAME).read_text().splitlines()

print(f' first line of the ', str(FILENAME), 'file: \n', lines[0])
