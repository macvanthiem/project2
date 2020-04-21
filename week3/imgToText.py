import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os.path
from os import path

def main():
	name = input("Enter photo name: ")
	if(path.exists(name)):
		img = Image.open(name)
		text = tess.image_to_string(img)
		print("Result: \n")
		print(text)
	else:
		print("This file does not exist!")

ctn = True
count = 1
while ctn:
	if (count == 1):
		main()
		count = count + 1
	
	a = input("Do you want to continue? y/...")
	if (a == 'y'):
		main()
	else:
		ctn = False
		print("The End!")

