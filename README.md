# PDF Reorder with OCR text recognition

Reorder PDF pages using OCR text recognition with Python and Regex.

## Getting Started

A simplified version of our script to reorder hundreds of PDF pages for our online orders.

This documentation assumes you have Python3 installed along with pip, virtualenv and git.

I'm using regex (regular expressions) in this example to match **phone numbers** in each PDF page to reorder the pages.

If phone numbers aren't standardized like in this example, results won't be perfect; improvise.

### Prerequisites

Things you need to install on your workstation

- python 3
- pip
- virtualenv
- tesseract
- poppler

Here are some references for **poppler** and **tesserect**:

- [blog.alivate.com.au/poppler-windows](https://blog.alivate.com.au/poppler-windows)
- [support.foxtrotalliance.com...](https://support.foxtrotalliance.com/hc/en-us/articles/360025802252-How-To-Work-With-Poppler-Utility-Library-PDF-Tool)
- [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)

Some useful reference for pdf2image:
- pdf2image [https://pypi.org/project/pdf2image/](https://pypi.org/project/pdf2image/)

As of this writing, I've tested this script using:

- Windows 10 Pro
- Python 3.7.4
- poppler-0.68.0_x86
- tesseract-ocr-w64-setup-v5.0.0-alpha.20191010.exe

You'll install the python modules using the **requirements.txt** example below.

### Installing

A step by step guide to set up a development environment.

- Install **poppler** on your workstation.

- Install **tesseract** on your workstation.

- Add them both to the PATH Environment.

Next, create a project folder and clone this repo:

```
mkdir pdfreorder
cd pdfreorder
git clone https://github.com/snowyTheHamster/pdf_reorder_with_ocr.git .
```

Create a virtual environment:

```
python -m virtualenv .venv
. .venv/scripts/activate # for windows
. .venv/bin/activate # for mac/linux
```

Install the included modules using pip

```
pip install -r requirements.txt
```

Now edit the full paths of the **poppler** and **tesseract** in the **start.py** file (details in **Code Explanation** below).

## Running the tests

I included a **sample.pdf** file.

To test, run:

```
python start.py
```

### Project Structure

- input_pdf_here: Add your pdf file here with a .pdf extension
- output_is_here: This is where the reordered pdf will be saved.
- start.py: Our python script.

### Break down of process

This example uses **regular expressions** to find **phone numbers** for sorting the pages.

Results may not be perfect if the **phone numbers** aren't standardized.

- The script saves the PDF page order in an array.
- Converts the PDF file to jpg files.
- Use OCR to grab text from the jpgs.
- Reorders the jpgs based on user defined regex match.
- Generates new PDF with updated page order.

**Some documentation**

- Documentation of [pdf2image](https://pypi.org/project/pdf2image/).
- Best regex youtube tutorial by Engineer Man: [https://www.youtube.com/watch?v=bgBWp9EIlMM](https://www.youtube.com/watch?v=bgBWp9EIlMM).
- Regex tester [https://www.debuggex.com/](https://www.debuggex.com/).

### Code Explanation

To make changes, edit the **start.py** file.

The script is divided in 3 main sections.
 
#### Part #1 : Converting PDF to images 

The PDF file is converted into jpgs.

Temporary jpg and txt files will be generated per pdf page.

You can edit the parameters in **convert_from_path** for more options.

More info is available in the **pdf2image** documentation above.

**Note**: You may need to add full path to **poppler** on some work stations:


```
pages = convert_from_path(PDF_file, 500, poppler_path="C:\\poppler-0.68.0\\bin")
```

**Note 2**: Change \ to / on linux and mac.

#### Part #2 : Recognizing text from the images using OCR

OCR will extract text from the jpg files to txt files.

We then use regex to research for phone numbers.

If regex matches a phone number, it'll add it to an array.

If regex doesn't match a phone number, it'll prepend a large number to it before adding it to the array. 

Finally, the script will reorder the array using the phone number as an index.

**Note**: You may need to add full path to **tesseract** on some work stations:

```
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\<username>\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
```

**Note 2**: Change \ to / on linux and mac.

#### Part #3 : Recognizing text from the images using OCR

The script will generate a new PDF with the updated page order.

The script will then delete all temporary txt and jpg files.

## Deployment

It might be easier to use this script if it's installed on the cloud with Flask. Provide users with frontend to upload their PDFs.

You can also use Pyinstaller to make executable versions for other workstations as long as tesseract and poppler are installed and the PATHs are correct.

## Authors

* **Taku** - [snowyTheHamster](https://github.com/snowyTheHamster)

## License

This project is licensed under the MIT License.