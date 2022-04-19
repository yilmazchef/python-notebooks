import os
import sys
import PIL.Image
import json


def resize(image, new_width=100):
    width, height = image.size
    new_height = new_width * old_height / old_width
    return image.resize((new_width, new_height))


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


def to_py(ipynb_file, logo_path=None):
    py_file = ipynb_file.replace(".ipynb", ".py")

    code = json.load(open(ipynb_file))

    try:
        image = PIL.Image.open(logo_path)
    except:
        print(logo_path, "Unable to find image ")

    # resize image
    image = resize(image)
    # convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    # save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            print('# -------- code --------')
            for line in cell['source']:
                print(line, end='')
            print('\n')
        elif cell['cell_type'] == 'markdown':
            print('# -------- markdown --------')
            for line in cell['source']:
                print("#", line, end='')
            print('\n')


if __name__ == "__main__":

    src_path = input(
        "Please paste here the absolute path of the root folder: "
    )

    if src_path == "":
        src = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    base = input(
        "What is the source file extension? .ipynb | .md | .docx | .pptx | .odt : "
    )

    logo_file = input(
        "Please enter the URL for logo image (Acceptable formats are PNG and JPG): "
    )
