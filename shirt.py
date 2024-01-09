from PIL import Image, ImageOps
import sys
import os

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        input_file, output_file = sys.argv[1], sys.argv[2]
        check_valid(input_file, output_file)
        sys.exit()


# input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
def check_valid(input_file, output_file):
    input = input_file.split(".")
    output = output_file.split(".")
    file_name = ["jpg", "png", "jpeg"]

    if input[1].lower() not in file_name:
        sys.exit("Invalid input ")
    elif output[1].lower() not in file_name:
        sys.exit("Invalid output ")

    else:
        check_extension(input_file, output_file)

# check if input/output havve same extension 
def check_extension(input_file, output_file):
    a, input_extension = os.path.splitext(input_file)
    b, output_extension = os.path.splitext(output_file)

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")
    else:
        apply_shirt(input_file, output_file)


def apply_shirt(input_file, output_file):

    # open input(before.jpg) and shirt.png
    try:
        muppet = Image.open(input_file)
        shirt = Image.open("shirt.png")

    except FileNotFoundError:
        sys.exit("Input does not exist")

    # get the shirt size
    size = shirt.size

    # corp input with ImageOps.fit()
    muppet = ImageOps.fit(muppet, size)

    # paste shirt on input
    muppet.paste(shirt, shirt)

    # save to output
    muppet.save(output_file)




if __name__ == "__main__":
    main()





