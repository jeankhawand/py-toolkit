import csv
import os
import pprint
DATADIR = "../assets/"
DATAFILE = "MOCK_DATA.csv"


def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rt') as file:
        reader = csv.DictReader(file)
        for line in reader:
            data.append(line)
    return data


if __name__ == "__main__":
    datafile = os.path.join(DATADIR, DATAFILE)
    dataextracted = parse_csv(datafile)
    pprint.pprint(dataextracted)
