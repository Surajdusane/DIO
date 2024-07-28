import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"


# Load the Word template
doc = DocxTemplate("pages/asset\Resignation Letter.docx")

st.title("Resignation Letter")

def main():
    # Create input text fields
    option = st.selectbox('Company Name', ('Kasperan Alytics', 'Precesion Staffing'), index=0)
    input1 = st.text_input("Name", "Sahil Sonar")
    input8 = st.selectbox("His or Her", ("His", "Her"), index=0)
    input2 = st.text_input("Date of Letter", "28th July 2024")
    input4 = st.selectbox("Designation",("US IT RECRUITER", "QA Engineer"), index=0)
    input5 = st.text_input("Employee ID", "KA100027/04")
    input6 = st.text_input("Joining Date", "6th June 2022")
    input7 = st.text_input("Resign Date", "19th July 2024")
    input1 = input1.title()

    # Create a submit button
    if st.button("Submit"):
        if option == "Kasperan Alytics":
            doc = DocxTemplate(r"pages\asset\Release Letter kas.docx")
        elif option == 'Precesion Staffing':
            doc = DocxTemplate(r"pages\asset\Release letter Letter.docx")
        
        if input8 == "His":
            input8 = "is"
        elif input8 == "Her":
            input8 = "er"
        context = {
            'name': input1,
            'date': input2,
            'emi': input5,
            'jdate': input6,
            'rdate': input7,
            'x': input8,
            'des': input4
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Release Letter of {input1}.docx")
        doc.save(file_path)
        st.success(f"File Release Letter of '{input1}.docx' was created successfully.")

if __name__ == "__main__":
    main()
