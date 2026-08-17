# Python Utility Programs

A small collection of Python utility programs focused on practical programming concepts, file handling, date calculations, and command-line input.

## Projects Included

### 1. JPEG Images to PDF Converter

Converts JPEG images into a single PDF file.

- Accepts either a single `.jpeg` file or a directory containing JPEG images.
- Uses command-line arguments to receive the input path.
- Generates an `output.pdf` file in the current directory.
- Uses the `img_to_pdf` package for PDF conversion.

The program checks whether the supplied path is a file or directory and processes JPEG images accordingly. fileciteturn0file0L6-L21

### 2. Age Calculator

Calculates a person's age in years, months, and days using the current local date.

- Takes the user's name and age as input.
- Handles leap years.
- Calculates the number of days elapsed across the relevant years.
- Uses Python's built-in `time` and `calendar` modules.

The program uses `calendar.isleap()` to determine leap years and `time.localtime()` to obtain the current date. fileciteturn0file1L1-L8 fileciteturn0file1L25-L46

## Technologies Used

- Python 3
- `time`
- `calendar`
- `os`
- `sys`
- `img_to_pdf`

## Installation

Clone the repository and install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

### JPEG to PDF Converter

Run the program with a JPEG file or directory path:

```bash
python image_to_pdf.py path/to/image.jpeg
```

or:

```bash
python image_to_pdf.py path/to/images
```

The converted file will be saved as:

```text
output.pdf
```

### Age Calculator

Run:

```bash
python age_calculator.py
```

Then enter your name and age when prompted.

## Repository Structure

```text
Python-Utility-Programs/
│
├── image_to_pdf.py
├── age_calculator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Learning Goals

This repository demonstrates:

- Functions
- Conditional statements
- Loops
- Command-line arguments
- File and directory handling
- Working with dates and time
- Leap-year calculations
- Python package usage
- Basic input/output operations

## Future Improvements

Possible improvements include:

- Support for `.jpg` and other image formats.
- Better command-line argument validation.
- Custom output PDF filenames.
- More accurate date-based age calculation using a birth date instead of only a numeric age.
- Improved error handling and user-friendly messages.

## License

This project is intended for learning and personal programming practice.
