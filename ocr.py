# bu programin yanina resimler diye bir klasor acip içine OCR dan gecirmek istediginiz resimleri kopyalayin
# python3 ocr.py   komutuyla resimlerdeki yazi ve karakterleri txt dosyasina bastirin.



from PIL import Image
import sys
import pyocr.builders
import os


# tum resimlerin dosya yollarini input.txt dosyasina yazdirir.
os.system('ls resimler >> input.txt')

# alinan dosya yollarini kullanmak için arraye kopyalanir.
inputarr = []
with open('input.txt') as my_file:
    for line in my_file:
        inputarr.append(line)



#  tesseract OCR kodu çalisan kisim.
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

# OCR dan elde edilen outputlari txt dosyalarina yazdirir.
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

