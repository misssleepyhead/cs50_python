from datetime import date
import re
import sys
import inflect

def main():
    # prompt for birthdate
    birthdate = input("Date of Birth:")
    valid_format(birthdate)


def valid_format(birthdate):

    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birthdate):
        try:
            get_min(birthdate)

        except ValueError:
            sys.exit("Invalid Date")

    else:
        sys.exit("Invalid Date")


def get_min(birthdate):
    # get today object
    today = date.today()
    # print(today)
    # get todat's y,m,d
    ty, tm, td = today.year, today.month, today.day

    birthdate = date.fromisoformat(birthdate)
    # print(birthdate)
    y, m, d = birthdate.year, birthdate.month, birthdate.day

    result = today - birthdate
    print(result)

    # since set time to 0am, only take days
    diff = result.days * 24 *60
    # print(result.days)
    # print(diff)

    p = inflect.engine()
    result = p.number_to_words(diff, andword="").capitalize()

    print (result +" minutes")


if __name__ == "__main__":
    main()
