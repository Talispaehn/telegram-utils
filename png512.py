# find all png images in current directory
# and resize them to 512x512 px
# and save them in a previously created directory named "resized"


import os
from PIL import Image

def main():
    directory = os.getcwd()
    print("Current directory: " + directory)
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            print("Found file: " + filename)
            im = Image.open(filename)
            imResize = im.resize((512, 512), Image.ANTIALIAS)
            imResize.save("resized/" + filename)

main()