import csv
import matplotlib.pyplot as plt
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


def avg(ar):
    return sum(ar) / len(ar)


def dispers(ar):
    av = avg(ar)

    nw = [((x - av) ** 2) for x in ar]

    return sum(nw) / len(ar)


def correl_coef(a, b):
    av_a = avg(a)
    av_b = avg(b)

    disp_a = dispers(a)
    disp_b = dispers(b)

    nw = [((x - av_a) * (y - av_b)) for x, y in zip(a, b)]

    return sum(nw) / (len(a) * ((disp_a * disp_b) ** 0.5))


def calc_A(a, b):
    av_a = avg(a)
    av_b = avg(b)

    n = len(a)

    s1 = sum([(x * y) for x, y in zip(a, b)])
    s2 = sum([(x**2) for x in a])

    # yapf: disable
    return (((av_a * av_b) - (s1 / n))
            / ((av_a ** 2) - (s2 / n)))


def calc_B(a, b):
    return avg(b) - (avg(a) * calc_A(a, b))


days, views, regs = read_csv(DATA_FILENAME)

mx = avg(views)
print("mx =", mx)
mz = avg(regs)
print("mz =", mz)

dx = dispers(views)
print("dx =", dx)
dz = dispers(regs)
print("dz =", dz)

k = correl_coef(views, regs)
print("k =", k)

a = calc_A(views, regs)
print("a =", a)
b = calc_B(views, regs)
print("b =", b)

f = lambda x: a * x + b
