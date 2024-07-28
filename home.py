import streamlit as st
from convert import convert_docx_folder_to_pdf
from meta_data_viewer import get_pdf_info
from meta_data_remover import remove_metadata
from clean import clear_folder
from zip_download import zip_folder

st.set_page_config(
    page_title="Docs Automation",
    page_icon="😴"
)
st.title("Docmation")
st.sidebar.success("Select the page above")

if st.sidebar.button("Clean All"):
    clear_folder('Docs Result')
    clear_folder('PDF Result')
    clear_folder('Output')

st.header('Convert Word Files to PDF', divider='grey')
if st.button("Convert"):
    # Define your input and output folders
    input_folder = r'Docs Result'
    output_folder = r'PDF Result'
    # Convert the Word files to PDFs
    convert_docx_folder_to_pdf(input_folder, output_folder)

st.header('View Metadata of All PDF', divider='grey')
if st.button("View"):
    # Specify the folder containing the PDFs
    folder_path = "PDF Result"
    # Get the PDF information dictionary
    pdf_info = get_pdf_info(folder_path)
    st.write(pdf_info)

st.header('Remove Metadata of All PDF', divider='grey')
if st.button("Remove"):
    # Example usage
    input_folder = 'PDF Result'  # Change this to your actual input folder
    output_folder = 'output'  # Change this to your actual output folder
    remove_metadata(input_folder, output_folder)
    st.success("Metadata Remove Succesfully!!!")

st.header('View Metadata of All PDF', divider='grey')
if st.button("View Reoved Data"):
    # Specify the folder containing the PDFs
    folder_path = "Output"
    # Get the PDF information dictionary
    pdf_info = get_pdf_info(folder_path)
    st.write(pdf_info)

# Button to create a zip file
if st.button("Create Zip"):
    zip_folder('output', "output")
    st.success("Zip file created successfully!")

# Button to download the zip file
with open("output.zip", "rb") as file:
    st.download_button("Download Zip", data=file, file_name='output.zip')


if __name__ == "__home__":
    main()
