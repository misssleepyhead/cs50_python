
def main():
    f = input("Fraction: ")
    precetage = convert(f)
    result = gauge(precetage)
    print(result)



def convert(fraction):
    while True:
        try:
            x = int(fraction.split("/")[0])
            y = int( fraction.split("/")[1])
            if y == 0:
                raise ZeroDivisionError
            elif x > y:
                raise ValueError
            elif x <= y:
                n = int(round(100 *(x/y)))
                print(n)
                return n

        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if 1< percentage < 99:
        result = str(f"{percentage}%")
        return result
    elif percentage <= 1:
        # result == "E"
        return "E"
    elif percentage >= 99:
        # result == "F"
        return "F"


if __name__ == "__main__":
    main()
