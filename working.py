import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.upper().strip()

    # matches = re.search(r"^([\d?\d]):([0-5][0-9])\s([AP][M])\sTO\s(\d?\d):([0-5][0-9])\s([AP][M])$", s, re.IGNORECASE)

    if matches:= re.search(r"^(\d?\d):([0-5][0-9])\s([AP][M])\sTO\s(\d?\d):([0-5][0-9])\s([AP][M])$", s, re.IGNORECASE):
        start_hour = matches.group(1)
        start_min = matches.group(2)
        start_ampm = matches.group(3)
        end_hour = matches.group(4)
        end_min = matches.group(5)
        end_ampm = matches.group(6)

        # convert hour (5pm to 17pm)
        start_hour = int(start_hour)
        end_hour = int(end_hour)

        if start_ampm == "AM" and start_hour == 12:
            start_hour =0
        elif start_ampm == "PM" and start_hour < 12:
            start_hour +=12

        if end_ampm == "AM" and end_hour == 12:
            end_hour =0
        elif end_ampm == "PM" and end_hour < 12:
            end_hour +=12

        return (f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}")

    elif matches := re.search(r"^(\d?\d)\s([AP][M])\sTO\s(\d?\d)\s([AP][M])$", s, re.IGNORECASE):
        start_hour = matches.group(1)
        start_ampm = matches.group(2)
        end_hour = matches.group(3)
        end_ampm = matches.group(4)


        # convert hour (5pm to 17pm)
        start_hour = int(start_hour)
        end_hour = int(end_hour)

        if start_ampm == "AM" and start_hour == 12:
            start_hour =0
        elif start_ampm == "PM" and start_hour < 12:
            start_hour +=12

        if end_ampm == "AM" and end_hour == 12:
            end_hour =0
        elif end_ampm == "PM" and end_hour < 12:
            end_hour +=12

        return (f"{start_hour:02}:00 to {end_hour:02}:00")

    else:
        raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()
