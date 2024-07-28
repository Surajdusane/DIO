import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"



st.title("Increment Letter")

def main():
    # Create input text fields
    option = st.selectbox('Company Name', ('Kasperan Alytics', 'Precesion Staffing'), index=0)
    input1 = st.text_input("Letter Date", "15th JUN 2023")
    input2 = st.text_input("Name", "Sahil Sonar")
    input3 = st.selectbox("Designation",("US IT RECRUITER", "QA Engineer"), index=0)
    input4 = st.text_input("Employee ID", "KA100027/04")
    input5 = st.text_input("CTC", "6,50,000")
    input6 = st.text_input("Date of Increment", "20th Jun")
    input7 = st.text_input("Year of Increment", "2023")

    # Create a submit button
    if st.button("Submit"):
        if option == "Kasperan Alytics":
            doc = DocxTemplate("pages/asset/INCREMENT LETTER.docx")
        elif option == 'Precesion Staffing':
            doc = DocxTemplate("pages/asset/Increment letter of Precesion.docx")
        context = {
            'dol': input1,
            'name': input2.title(),
            'empi': input4,
            'des': input3,
            'doi': input6,
            'yoi': input7,
            'ctc': input5
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Increment Letter of {input2}.docx")
        doc.save(file_path)
        st.success(f"File Increment Letter of '{input2}.docx' was created successfully.")

if __name__ == "__main__":
    main()
