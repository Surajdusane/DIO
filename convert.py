import os
import platform
from docx2pdf import convert
import subprocess

def convert_docx_folder_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Check the operating system
    os_name = platform.system().lower()

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a Word document
        if filename.endswith(".docx"):
            # Full path to the Word document
            input_path = os.path.join(input_folder, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.pdf"
            output_path = os.path.join(output_folder, output_filename)

            if os_name == "windows":
                # Convert the document to PDF using docx2pdf
                convert(input_path, output_path)
            elif os_name == "linux":
                # Convert the document to PDF using LibreOffice
                subprocess.call(['soffice', '--convert-to', 'pdf', '--outdir', output_folder, input_path])
            else:
                print(f"Unsupported operating system: {os_name}")
                continue

            print(f"Converted: {input_path} to {output_path}")