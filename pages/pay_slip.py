import streamlit as st
from docxtpl import DocxTemplate
import os
folder_path = "Docs Result"

# Load the Word template
doc = DocxTemplate("pages\\asset\\PAY SLIP of Precesion.docx")

st.title("Pay Slip")

month_details = {
    1: ["Jan", 31],
    2: ["Feb", 29],
    3: ["Mar", 31],
    4: ["Apr", 30],
    5: ["May", 31],
    6: ["Jun", 30],
    7: ["Jul", 31],
    8: ["Aug", 31],
    9: ["Sep", 30],
    10: ["Oct", 31],
    11: ["Nov", 30],
    12: ["Dec", 31]
}

def calculate_PT(k3):
    return 0 if k3 <= 10000 else 150 if k3 <= 15000 else 200


def main():
    # Create input text fields
    option = st.selectbox('Company Name', ('Kasperan Alytics', 'Precesion Staffing'), index=0)
    input1 = st.text_input("Month(IN Number)", 5)
    input2 = st.text_input("Date of Joining", "17-01-2022")
    input3 = st.text_input("PAN No", "CPSPA9831C")
    input4 = st.text_input("Bank A/C", "923010040962664")
    input5 = st.text_input("Name", "Sahil Sonar")
    input6 = st.text_input("Employee ID", "KA100027/04")
    input7 = st.selectbox("Designation",("US IT RECRUITER", "QA Engineer"), index=0)
    input8 = st.text_input("Salary/Month", "35000")
    input9 = st.text_input("Incentive first", "")
    input10 = st.text_input("Incentive second", "")
    input11 = st.text_input("Incentive third", "")
    input12 = st.text_input("Incentive fourth", "")
    

    pay_period = month_details[int(input1)-1][0] + " 2024"
    pay_days = month_details[int(input1)-1][1]

    #calculation of salary
    basic_pay = (int(input8)-2500)*70/100
    hra = (int(input8)-2500)*12/100
    bonus = (int(input8)-2500)*18/100
    total_earning = int(basic_pay) + int(hra)+ int(bonus) + 2500
    pt = calculate_PT(int(input8))
    total_deduction = int(pt)+700+2500
    net_pay = int(total_earning) - 800


    if st.button("Submit"):
        if option == "Kasperan Alytics":
            doc = DocxTemplate("pages\\asset\\PAY SLIP.docx")
        elif option == 'Precesion Staffing':
            doc = DocxTemplate("pages\\asset\\PAY SLIP of Precesion.docx")
        context = {
            'mon': month_details[int(input1)][0],
            'date': input2,
            'pep': pay_period,
            'pd': pay_days,
            'pan': input3,
            'bank': input4,
            'name': input5,
            'empi': input6,
            'des': input7,
            'bp': "{:,}".format(int(basic_pay)),
            'hra': "{:,}".format(int(hra)),
            'bonus': "{:,}".format(int(bonus)),
            'te': "{:,}".format(int(total_earning)),
            'pt': pt,
            'np': net_pay,
            'in': "{:,}".format(int(input9))
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Payslip of {month_details[int(input1)][0]}.docx")
        doc.save(file_path)

        #second month
        pay_period = month_details[int(input1)-2][0] + " 2024"
        pay_days = month_details[int(input1)-2][1]

        context = {
            'mon': month_details[int(input1)-1][0],
            'date': input2,
            'pep': pay_period,
            'pd': pay_days,
            'pan': input3,
            'bank': input4,
            'name': input5,
            'empi': input6,
            'des': input7,
            'bp': "{:,}".format(int(basic_pay)),
            'hra': "{:,}".format(int(hra)),
            'bonus': "{:,}".format(int(bonus)),
            'te': "{:,}".format(int(total_earning)),
            'pt': pt,
            'td': total_deduction,
            'np': net_pay,
            'in': "{:,}".format(int(input10))
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Payslip of {month_details[int(input1)-1][0]}.docx")
        doc.save(file_path)

        #second month
        pay_period = month_details[int(input1)-3][0] + " 2024"
        pay_days = month_details[int(input1)-3][1]

        context = {
            'mon': month_details[int(input1)-2][0],
            'date': input2,
            'pep': pay_period,
            'pd': pay_days,
            'pan': input3,
            'bank': input4,
            'name': input5,
            'empi': input6,
            'des': input7,
            'bp': "{:,}".format(int(basic_pay)),
            'hra': "{:,}".format(int(hra)),
            'bonus': "{:,}".format(int(bonus)),
            'te': "{:,}".format(int(total_earning)),
            'pt': pt,
            'td': total_deduction,
            'np': net_pay,
            'in': "{:,}".format(int(input11))
        }
        # Render the template with data
        doc.render(context)
        # Save the generated certificate with a filename based on the participant's name
        file_path = os.path.join(folder_path, f"Payslip of {month_details[int(input1)-2][0]}.docx")
        doc.save(file_path)

        st.write({
        'mon': month_details[int(input1)][0],
        'date': input2,
        'pep': pay_period,
        'pd': pay_days,
        'pan': input3,
        'bank': input4,
        'name': input5,
        'empi': input6,
        'des': input7,
        'bp': "{:,}".format(int(basic_pay)),
        'hra': "{:,}".format(int(hra)),
        'bonus': "{:,}".format(int(bonus)),
        'te': "{:,}".format(int(total_earning)),
        'pt': pt,
        'td': total_deduction,
        'np': net_pay,
        'in': "{:,}".format(int(input12))
    })
        st.success(f"File Payslip of {month_details[int(input1)][0]}, {month_details[int(input1)-1][0]} and {month_details[int(input1)-2][0]} was created successfully.")


if __name__ == "__main__":
    main()