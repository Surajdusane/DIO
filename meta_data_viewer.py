import os
from spire.pdf import PdfDocument

def get_pdf_info(folder_path):
    # Dictionary to store information for each PDF
    pdf_info_dict = {}

    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            # Create a PdfDocument object
            doc = PdfDocument()
            
            # Load the PDF file
            file_path = os.path.join(folder_path, filename)
            doc.LoadFromFile(file_path)
            
            # Get the document information
            information = doc.DocumentInformation
            
            # Read built-in properties
            pdf_info = {
                "Author": information.Author,
                "Title": information.Title,
                "Subject": information.Subject,
                "Keywords": information.Keywords,
                "Producer": information.Producer,
                "Company": information.GetCustomProperty("Company"),
                "Telephone": information.GetCustomProperty("Telephone")
            }
            
            # Add the information to the dictionary
            pdf_info_dict[filename] = pdf_info
            
            # Close the document
            doc.Close()
    
    return pdf_info_dict




