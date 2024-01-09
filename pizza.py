import sys
from tabulate import tabulate
import csv


menu = []

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        check_argv(sys.argv)
        sys.exit()

def check_argv(argv):
    n = sys.argv[1].split(".")
    if n[1] == "csv":
         format(sys.argv[1])

    else:
        sys.exit("Not a CSV file")

def format(argv):
    n = sys.argv[1]
    try:
        with open(n) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

            print(tabulate(menu, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
