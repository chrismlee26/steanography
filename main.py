"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image, ImageDraw, ImageFont
from PIL.ImagePalette import raw


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open('./static/encoded_sample.png')

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    # Start coding here!
    for x in range(x_size):
        for y in range(y_size):
            buffer = red_channel.getpixel((x, y))

            binary = bin(buffer)
            lsb = binary[len(binary) - 1]
            lsb = int(lsb)

            rgb = (255, 255, 255) if lsb == 0 else (0, 0, 0)

            decoded_image.putpixel((x, y), rgb)

    decoded_image.save("decoded_image.png")


decode_image("./static/encoded_sample.png")
