# TODO
from cs50 import get_float

# Ask how many cents the customer is owed
while True:
    try:
        input = get_float("Change owed:")
        if input > 0:
            break
    except ValueError:
        print("Not an integer")

cents = input*100
i = 0

while cents >= 25:
    cents = cents-25
    i = i+1

while cents >= 10:
    cents = cents - 10
    i = i+1

while cents >= 5:
    cents = cents-5
    i = i+1

while cents >= 1:
    cents = cents - 1
    i = i+1

print(i)

