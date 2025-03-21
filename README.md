# Extract Metadata from SEM images

## Description
This is a simple GUI-based application that allows users to extract XML metadata from .tiff image files into HTML format coming from Fibics SEM Atlas software. The program uses Python's Tkinter for the graphical interface and `xml.etree.ElementTree` for XML parsing.

There is also a script version.

Authors:
- José Miguel Serra Lleti
- Anna Steyer

## Features
- Select an image file using a file dialog or using the script
- Save the XML into a structured HTML file.
- Save the output file with a user-defined name or a randomly generated filename.
- Simple graphical interface.

## Requirements
- Python 3.9 onwards
### GUI
- Tkinter (included in standard Python installation)

### Script
- Required dependencies:
  ```sh
  pip install tifffile
  ```

##  Usage 
If you want to run the script directly, simply execute:
```sh
        python extractFibicsMetadata2.py "slice_01715_z=25.7100um.tif"
```
 The second is an executable, it does the same but only for Fibics metadata. SImple select the image.


## Installation

To create a Windows executable:
1. Install `pyinstaller` if you haven’t already:
   ```sh
   pip install pyinstaller
   ```
2. Navigate to the script directory and run:
   ```sh
   pyinstaller --onefile --noconsole --name "MetadataExtractor" extractFibicsMetadata.py
   ```
3. The executable file will be found in the `dist/` folder.

## Usage
1. Run the application.
2. Click the **"Choose File"** button to select an image file.
4. The application will convert the internal metadata in XML into HTML and save it.

## Notes
- The application works only with well-formed XML files.

## License
This project is open-source and available under the MIT License.