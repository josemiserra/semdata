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
        html = f"<div><strong>{element.tag}:</strong>"
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract metadata to an HTML file.")
    parser.add_argument("path", help="Path to the input image file")
    args = parser.parse_args()
    
    res = read_tiff_metadata(args.path)
    keys = ['ImageWidth', 'ImageLength', 'BitsPerSample', 'Compression', 'Orientation', 'SamplesPerPixel','ResolutionUnit', 'Software', 'DateTime', 'SampleFormat']
    for el in keys:
        print("--"+ el +":" + str(res[el]))
    _, filename = os.path.split(args.path)
    print_info_image(res, filename )







