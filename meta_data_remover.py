import os
import PyPDF2

def remove_metadata(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all the PDF files in the input directory
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(input_folder, filename)
            output_pdf_path = os.path.join(output_folder, filename)

            # Open the input PDF
            with open(input_pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                writer = PyPDF2.PdfWriter()

                # Copy all the pages from the reader to the writer
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    writer.add_page(page)

                # Clear the metadata
                writer._info = PyPDF2.generic.DictionaryObject()

                # Write the output PDF
                with open(output_pdf_path, 'wb') as output_file:
                    writer.write(output_file)


