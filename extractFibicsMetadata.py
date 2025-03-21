import tifffile
import xml.etree.ElementTree as ET
import argparse
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def read_tiff_metadata(file_path):
    """Reads and returns the metadata of a .tif file."""
    with tifffile.TiffFile(file_path) as tif:
        metadata = tif.pages[0].tags  # Metadata from the first page
        meta_dict = {tag.name: tag.value for tag in metadata.values()}
    return meta_dict


def xml_to_html(xml_string):
    """Converts XML to an HTML representation."""
    root = ET.fromstring(xml_string)
    
    def traverse(element):
        """Recursively traverse XML elements and convert them into HTML."""
        html = f"<div><strong>{element.tag}:</strong> "
        if element.text and element.text.strip():
            html += f"{element.text.strip()}"
        html += "</div>"
        
        for child in element:
            html += f"<div style='margin-left:20px;'>{traverse(child)}</div>"
        
        return html
    
    html_content = "<html><body>" + traverse(root) + "</body></html>"
    return html_content


def print_info_image(res, filename):
    html_file = xml_to_html(res['FibicsXML'])
    output_file = os.path.join(os.getcwd(), f"metadata_{filename}.html")
    
    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_file)
    print("HTML saved in "+output_file)


def select_file():
    """Open file dialog to select an XML file and convert it."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.tif")])
    if file_path:
        res = read_tiff_metadata(file_path)
        keys = ['ImageWidth', 'ImageLength', 'BitsPerSample', 'Compression', 'Orientation', 'SamplesPerPixel','ResolutionUnit', 'Software', 'DateTime', 'SampleFormat']
        for el in keys:
                print("--"+ el +":" + str(res[el]))
        _, filename = os.path.split(file_path)
        print_info_image(res, filename)

def main():
    """Create a simple GUI for selecting an image file."""
    root = tk.Tk()
    root.title("IMAGE METADATA EXTRACTOR")
    root.geometry("300x150")
    
    tk.Label(root, text="Select an image file to get metadata:").pack(pady=10)
    tk.Button(root, text="Choose File", command=select_file).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()







