# prompts the user for a str of text
# outputs that same text but with all vowels (A, E, I, O, and U) omitted.

vowels = ["a", "e", "i", "o", "u"]


def main():
    x = input("Input: ")
    print("Output:",shorten(x))



def shorten(x):

    output = ""
    for char in x:
        if char.lower() not in vowels:
            output += char

    return output


if __name__ == "__main__":
    main()
