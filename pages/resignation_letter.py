import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"


# Load the Word template
doc = DocxTemplate("pages/asset/Resignation Letter.docx")

st.title("Resignation Letter")

def main():
    # Create input text fields
    option = st.selectbox('Company Name', ('Kasperan Alytics', 'Precesion Staffing'), index=0)
    input1 = st.text_input("Name", "Sahil Sonar")
    input2 = st.text_input("Mail", "sahil@work.com".lower())
    input3 = st.text_input("Date and Time of Mail Send", "17 April 2024 at 16:05")
    input4 = st.selectbox("Designation",("US IT RECRUITER", "QA Engineer"), index=0)
    input5 = st.text_input("Employee ID", "KA100027/04")
    input6 = st.text_input("Phone number", "9579330721")
    input7 = st.text_input("Date and Time of Mail Recived", "17 April 2024 at 17:15")
    input2 = input2.lower()
    input1 = input1.title()

    # Create a submit button
    if st.button("Submit"):
        if option == "Kasperan Alytics":
            doc = DocxTemplate("pages/asset/Resignation Letter.docx")
        elif option == 'Precesion Staffing':
            doc = DocxTemplate("pages/asset/Resignation Letter of Precesion.docx")
        context = {
            'name': input1,
            'mail': input2,
            'dts': input3,
            'des': input4,
            'empi': input5,
            'num': input6,
            'dtr': input7
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Resignation Letter of {input1}.docx")
        doc.save(file_path)
        st.success(f"File Resignation Letter of '{input1}.docx' was created successfully.")

if __name__ == "__main__":
    main()
