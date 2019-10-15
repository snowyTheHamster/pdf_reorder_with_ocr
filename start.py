# Import libraries
from PIL import Image
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os, glob, re
from os import listdir
from PyPDF2 import PdfFileWriter, PdfFileReader

dirpath = os.getcwd() # get current directory

# select the pdf file in this folder
os.chdir("./input_pdf_here")
for file in glob.glob("*.pdf"):
    input_pdf = file
    break
pdf_input_dir = os.getcwd() # update the directory

input_pdf_fullpath = os.path.join(dirpath, "input_pdf_here", input_pdf) # input folder and file
pdf_output_dir = os.path.join(dirpath, "output_is_here", "output.pdf") # output folder and file


''' 
Part #1 : Converting PDF to images 
'''

# Store all the pages of the PDF in a variable 
pages = convert_from_path(input_pdf_fullpath, 500, poppler_path="C:\\poppler-0.68.0\\bin") # NEED TO ADD PATH TO POPPLER FOR SOME WORKSTATIONS

# Counter to store images of each page of PDF to image 
image_counter = 1
# Iterate through all the pages stored above 
for page in pages: 
    print(f"converting pdf to jpg for: {page}")
    # PDF page n -> page_n.jpg 
    filename = "page_"+str(image_counter)+".jpg"
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
    # Increment the counter to update filename 
    image_counter = image_counter + 1
    print(f"conversion done for: {page}")


''' 
Part #2 - Recognizing text from the images using OCR 
'''

original_pages = [] # remember that page numbering starts from 0
keep_pages = [] # remember that page numbering starts from 0

# Variable to get count of total number of pages 
filelimit = image_counter-1

# Add tesseract full path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\taku\\AppData\\Local\\Tesseract-OCR\\tesseract.exe' # NEED TO ADD PATH TO Tesseract FOR SOME WORKSTATIONS

# Creating a text file to write the output 
for i in range(1, filelimit + 1):
    print(f"text recognition for image #:{i}")
    print(f"generating text file for image #:{i}")
    filename = "page_"+str(i)+".jpg"
    outfile = "page_"+str(i)+".txt"
    f = open(outfile, "w")

    # Recognize the text as string in image using pytesserct 
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    text = text.replace('-\n', '')
    # Finally, write the processed text to the file. 
    f.write(text)
    # Close the file after writing all the text. 
    f.close()

# Search for phonenumber values from text files
# for i in range(1, filelimit + 1)[:-1]: # omit last page if you want
for i in range(1, filelimit + 1):
    print(f"searching phonenumber for #:{i}")
    outfile = "page_"+str(i)+".txt"

    # Open the file again in read mode
    f = open(outfile, "rt")

    # Read the content of the file
    contents = f.read()
    f.close()

    # Show off your Regex skills below
    searchtel = re.search("T: [0-9]{8}[^0-9a-zA-Z]|T: [0-9]{8} ", contents) #regex to match pattern
    if (searchtel):
        # get the phone number value
        customertel = searchtel.group(0)
        customertel = customertel[3:]

        print("matched PHONE")
        print("ヘ( ^o^)ノ＼(^_^ )")
        print("\n")

        original_pages.append([i-1, customertel])
        prevcustomertel = customertel
    else:
        print("no PHONE match")
        print("┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")
        print("\n")
        original_pages.append([i-1, f"99999999{i}"]) # prepend ridicuous number to push page to the end
        prevcustomertel = f"99999999{i}"

original_pages = sorted(original_pages, key=lambda x: x[1]) # reorder list using phone number

for i in range(len(original_pages)):
    new_order = original_pages[i][0] # get only the index value
    keep_pages.append(new_order) # append index value to array as the new page order
print(f"this is the new order: {keep_pages}") # print out new order


'''
Part #3 - Reorder the PDF files according to the new order
'''

print("Generating new PDF file with updated order")
infile = PdfFileReader(input_pdf_fullpath, 'rb')
output = PdfFileWriter()

for i in keep_pages:
    p = infile.getPage(i)
    output.addPage(p)

with open(pdf_output_dir, 'wb') as f:
    output.write(f)

# delete the temporary jpg and txt files
print("deleting all temporary jpg and text files")
for filename in listdir(pdf_input_dir):
    if filename.endswith(('.txt', '.jpg')):
        thefile = os.path.join(pdf_input_dir, filename)
        os.remove(thefile)

print("pdf reorder finished (⌐■_■) ")



