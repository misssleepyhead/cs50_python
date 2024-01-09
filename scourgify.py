import csv
import sys



# implement read sys.argv[1] file as input,column: name, house
# create a new file, column should be first, last ,house
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        students_list = read_file(sys.argv[1])
        new_list = create_new_list(students_list)
        write_file(sys.argv[2], new_list)
        sys.exit()

# Read from the oldfile name (last,fiest), home
def read_file(oldfile):
    students = []
    try:
        with open(oldfile) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name":row["name"], "house":row["house"]})

            return students
    except FileNotFoundError:
        sys.exit(f"Could not read {oldfile}")


# split name(last,fist), house into first, last, house
def create_new_list(students_list):
    new_list = []
    for row in students_list:
        last, first = row["name"].split(",")
        new_list.append(
            {"first":first.strip(),
             "last":last.strip(),
             "house":row["house"]}
        )

    return new_list

# write new_list into new csv file
def write_file(newfile, new_list):
    try:
        with open(newfile, "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
            writer.writeheader()
            for row in new_list:
                writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})



    except FileNotFoundError:
        sys.exit(f"Could not read {newfile}")


if __name__ == "__main__":
    main()


