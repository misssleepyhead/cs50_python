from validator_collection import validators, errors

def main():
    user = input("What's your email address?").strip()
    if validate(user):
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    try:
        result = validators.email(s, allow_empty=False)
        return True
    except errors.EmptyValueError:
        return False
    except errors.InvalidEmailError:
        return False

if __name__ == "__main__":
    main()
