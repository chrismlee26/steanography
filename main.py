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
            pass

    # Step 1: Read first 3 pixels
    # Step 2: Even = 0, Odd = 1, Sets of 8 (Binary)
    # Step 3: Binary value -> decimal -> ASCII
    # Step 4: When 9th value == even, stop

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

    pass


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass
    # Step 1: Each character, ASCII converted into 8-bit binary
    # Step 2: Read 3 pixels at a time, 3*3 = 9 RBG Values
    # Step 3: RBG and binary compared. If binary == 1, RBG = Odd, If Binary == 0, RBG = Even
    # Step 4: Check 9th value == odd = continue, even = stop


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass
