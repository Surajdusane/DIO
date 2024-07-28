import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"


# Load the Word template
doc = DocxTemplate(r"./pages/asset/CERTIFICATE.docx")

st.title("Certificate")

def main():
    # Create input text fields
    input1 = st.text_input("Duration", "Jul 2023 to Feb 2024")
    input2 = st.text_input("Name", "sahil sonar".upper())
    input3 = st.text_input("Month Duration", 6)
    input4 = st.text_input("Certificate Date", "28/12/2003")
    input2 = input2.upper()
    input1 = input1.title()

    # Create a submit button
    if st.button("Submit"):
        context = {
            'd': input1,
            'name': input2,
            'md': input3,
            'cd': input4
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Certificate of {input2.title()}.docx")
        doc.save(file_path)
        st.success(f"File Certificate of '{input2.title()}.docx' was created successfully.")

if __name__ == "__main__":
    main()
