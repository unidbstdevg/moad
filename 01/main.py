import csv
import itertools

DATA_FILENAME = "website_stat.csv"


def read_csv(filename):
    """Returns tuple of (header_row and attribute_columns)"""

    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")

        # skip header row
        reader = itertools.islice(reader, 1, None)
        # yes, transpose
        reader = zip(*reader)

        # yapf: disable
        return [
                [
                    int(val)
                    for val in col
                ]
                for col in reader
            ]

    return None


days, views, regs = read_csv(DATA_FILENAME)
