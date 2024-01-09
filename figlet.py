import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
figList = figlet.getFonts()

if len(sys.argv) == 3:
    if "-f" in sys.argv[1] or "--font" in sys.argv[1]:
        if sys.argv[2] in figList:
            s = input ("Input:")
            figlet.setFont(font=sys.argv[2])
            print("Output:")
            print(figlet.renderText(s))
        else:
            print("Invalid usuage")
            sys.exit(1)
    else:
        print("Invalid usuage")
        sys.exit(1)


elif len(sys.argv) == 1:
    s = input ("Input:")
    s_output = random.choice(figList)
    figlet = Figlet(font=s_output)
    print("Output:")
    print(figlet.renderText(s))

elif len(sys.argv) != 1:
    print("Invalid usuage")
    sys.exit(1)
else:
    print("Invalid usuage")
    sys.exit(1)


