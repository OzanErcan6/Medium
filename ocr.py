# Tesseract-based OCR program developed to convert text and characters in images to text  

# USAGE #
# Open a folder called "images" in the directory where this program is located and copy the pictures you want to OCR into.
# With the python3 ocr.py command, print the text and characters in the images to the txt file.


from PIL import Image
import sys
import pyocr.builders
import os


os.system('ls images >> input.txt')

inputarr = []
with open('input.txt') as my_file:
    for line in my_file:
        inputarr.append(line)

tools = pyocr.get_available_tools()

if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % lang)

outCount=0


for x in inputarr:
    x = x[:-1]
    txt = tool.image_to_string(
        Image.open(x),
        lang="eng",
        builder=pyocr.builders.TextBuilder()
    )
    f = open("out%df.txt" % outCount, "a")
    txt = txt + "\n"
    f.write(txt)
    outCount += 1 

f.close()


os.unlink("input.txt")

