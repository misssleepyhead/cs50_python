def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6 and s[0:2].isalpha()):
        return False

    for char in s:
        if not char.isalnum():
            return False
        elif char.isdigit() and char =="0":
            return False

        first_digit = s.index(char)
        first_part = s[:first_digit]
        second_part = s[first_digit:]

        for i in first_part:
            if i.isdigit():
                return False
            for j in second_part:
                if j.isalpha():
                    return False

    return True



if __name__ == "__main__":
    main()
