import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe.+></iframe?",s.strip()):

        # search the url including http(s):///(www).youtube.com/embed/(str)
        if matches := re.search(r"(?:<iframe)?https?://(?:www\.)?youtube.com/embed/(\w+)",s.strip()):
            return("https://youtu.be/"+ matches.group(1))



if __name__ == "__main__":
    main()
