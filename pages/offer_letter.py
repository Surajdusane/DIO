import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"

# Load the Word template
doc = DocxTemplate("pages/asset\Precesion offeer letter Final.docx")

st.title("Offer Letter")

def main():
    # Create input text fields
    option = st.selectbox('Company Name', ('Kasperan Alytics', 'Precesion Staffing'), index=0)
    input1 = st.text_input("Date of Offer Latter", "28th Dec 2023")
    input2 = st.text_input("Name", "sahil pravin sonar".title())
    input3 = st.selectbox("Designation",("US IT RECRUITER", "QA Engineer"), index=0)
    input4 = st.text_input("Date of Joining", "16th Jan 2022")
    input5 = st.text_input("CTC", "6,50,000")
    input6 = st.text_input("Time Zone", "10:00 AM to 07:00 PM")
    input2 = input2.title()
    input3 = input3.upper()


    salary = int(input5.replace(',', ''))/12
    basic_pay = (int(salary))*70/100
    hra = (int(salary))*12/100
    bonus = (int(salary))*10/100
    special = (int(salary))*8/100
    costofcompany = int(salary) - 800

    # Create a submit button
    if st.button("Submit"):
        if option == "Kasperan Alytics":
            doc = DocxTemplate("pages/asset/Offer Letter.docx")
        elif option == 'Precesion Staffing':
            doc = DocxTemplate("pages/asset/Offer Letter Precesion.docx")
        context = {
            'dol': input1,
            'name': input2.title(),
            'des': input3.upper(),
            'doj': input4,
            'ctc': input5,
            'tz': input6,
            'mbs': int(basic_pay),
            'abs': int(basic_pay)*12,
            'mhra': int(hra),
            'ahra': int(hra)*12,
            'msb': int(bonus),
            'asb': int(bonus)*12,
            'msa': int(special),
            'asa': int(special)*12,
            'mgs': int(salary),
            'ags': int(salary)*12,
            "mctc": int(costofcompany),
            'actc': int(costofcompany)*12
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Offer Letter of {input2.title()}.docx")
        doc.save(file_path)
        st.success(f"File Offer Letter of '{input2.title()}.docx' was created successfully.")

if __name__ == "__main__":
    main()
