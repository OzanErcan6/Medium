# bu programın yanına resimler diye bir klasör açıp içine OCR dan geçirmek istediğiniz resimleri kopyalayın
# python3 ocr.py   komutuyla resimlerdeki yazı ve karakterleri txt dosyasına bastırın.



from PIL import Image
import sys
import pyocr.builders
import os


# getting all frame paths from the current directory 
os.system('ls resimler >> input.txt')

# filling inputarr 
inputarr = []
with open('input.txt') as my_file:
    for line in my_file:
        inputarr.append(line)


# setting density for all frames 
#os.system('for i in *.png; do echo "mogrify -set units PixelsPerInch -density 1606 $i"; done')

#  OCR work here 
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

