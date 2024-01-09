import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip.strip())
    try:
        if match:
            groups = [int(match.group(i)) for i in range(1, 5)]
            return all(0 <= x <= 255 for x in groups)
        else:
            return False
        
    except ValueError:
        return False



if __name__ == "__main__":
    main()
