# PDF Reorder with OCR text recognition

Reorder PDF pages using OCR text recognition with Python and Regex.

## Getting Started

This documentation assumes you have Python3 installed along with pip, virtualenv and git.

### Prerequisites

What things you need to install the software and how to install them

- Python 3
- Pip
- virtualenv
- pillow
- pypdf2
- tesseract
- poppler
- pdf2image [https://pypi.org/project/pdf2image/](https://pypi.org/project/pdf2image/)

You may need to install **poppler** and **tesserect** on your workstation and add them to the PATH Environment.

Here are some references for **poppler** and **tesserect**:

- [blog.alivate.com.au/poppler-windows](https://blog.alivate.com.au/poppler-windows)
- [support.foxtrotalliance.com...](https://support.foxtrotalliance.com/hc/en-us/articles/360025802252-How-To-Work-With-Poppler-Utility-Library-PDF-Tool)
- [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)

### Installing

A step by step series of examples that tell you how to get a development env running.

First, install **poppler** and **tesseract** on your workstation with reference to docs above.

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

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

To test, run:

```
python start.py
```

You'll need to change path to **poppler** and **tesseract** in **start.py** script to match your workstation.

### Project Structure

- input_pdf_here: Add your pdf file here with a .pdf extension
- output_is_here: This is where the reordered pdf will be saved.
- temp_folder: a temp folder where jpgs and txt files are temporarily generated.
- start.py: The python script that does everything.

### Break down of process

This example uses **regular expressions** to find **phone numbers** for sorting the pages. Results may not be perfect if the **phone numbers** arn't standardized.

- The script saves PDF order in an array.
- Converts PDF to jpg.
- Use OCR to grab text from jpgs.
- Reorders jpgs based on user defined values.
- Generates PDF with updated page order.

- Documentation of [pdf2image](https://pypi.org/project/pdf2image/)
- best regex youtube tutorial: [https://www.youtube.com/watch?v=bgBWp9EIlMM](https://www.youtube.com/watch?v=bgBWp9EIlMM)
- regex tester [https://www.debuggex.com/](https://www.debuggex.com/)

### Code Explanation

To make changes, edit the **start.py** file.

The script is divided in 3 main sections.
 
#### Part #1 : Converting PDF to images 

The PDF file is converted into jpgs.

There will be one jpg file per PDF page and they will be generated in the temp_folder.

You can edit the parameters in **convert_from_path** for more options. More info is available in the **pdf2image** documentation above.

**Note**: You may need to add full path to **poppler** on some work stations.

#### Part #2 : Recognizing text from the images using OCR

OCR will extract text from the jpg files to txt files.

We then use regex to research for phone numbers.

If regex matches a phone number, it'll add it to an array.

If regex doesn't match a phone number, it'll prepend a large number to it before adding it to the array. 

Finally, the script will reorder the array using the phone number as an index.

#### Part #2 : Recognizing text from the images using OCR

The script will generate a new PDF with the updated page order.

The script will then delete all txt and jpg files in the temp folder.

## Deployment

It might be easier to use this script if it's installed on the cloud with Flask. Provide users with frontend to upload their PDFs.

You can also use Pyinstaller to make executable versions for other workstations as long as tesseract and poppler are installed and the PATHs are correct.

## Authors

* **Taku** - *Initial work* - [snowyTheHamster](https://github.com/snowyTheHamster)

## License

This project is licensed under the MIT License.