import os
from docx2pdf import convert

def convert_docx_folder_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a Word document
        if filename.endswith(".docx"):
            # Full path to the Word document
            input_path = os.path.join(input_folder, filename)

            # Define the output PDF path
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.pdf")

            # Convert the document to PDF
            convert(input_path, output_path)
            
            print(f"Converted: {input_path} to {output_path}")




