import sys


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
    if n[1] == "py":
         check_file(sys.argv[1])

    else:
        sys.exit("Not a python file")

def check_file(argv):
    # open file
    n = sys.argv[1]
    count = 0
    try:
        with open(n) as file:
            for line in file:
                if line.strip():
                    if not line.lstrip().startswith("#"):
                        count += 1

                else:
                    pass
            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
