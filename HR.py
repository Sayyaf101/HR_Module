import streamlit as st
import pandas as pd
import datetime

# Initialize a list to store employee and payroll data
employees = []
payroll_history = []

# Function to calculate payroll for each employee
def calculate_payroll(employee_id, basic_salary, bonuses, deductions):
    net_salary = basic_salary + bonuses - deductions
    return net_salary

# Page layout and title
st.title("Human Resource Management System")
st.subheader("Payroll Process Module")

# Employee details form
st.sidebar.header("Add Employee Details")
with st.sidebar.form("employee_form"):
    employee_id = st.text_input("Employee ID")
    employee_name = st.text_input("Employee Name")
    basic_salary = st.number_input("Basic Salary", min_value=0.0, step=100.0)
    bonuses = st.number_input("Bonuses", min_value=0.0, step=50.0)
    deductions = st.number_input("Deductions", min_value=0.0, step=50.0)
    add_employee = st.form_submit_button("Add Employee")
    
    if add_employee:
        employees.append({
            "Employee ID": employee_id,
            "Name": employee_name,
            "Basic Salary": basic_salary,
            "Bonuses": bonuses,
            "Deductions": deductions,
            "Net Salary": calculate_payroll(employee_id, basic_salary, bonuses, deductions)
        })
        st.sidebar.success("Employee added successfully!")

# Display payroll processing section
st.header("Payroll Processing")

if st.button("Run Payroll Process"):
    # Process payroll for each employee and record the transaction
    payroll_date = datetime.date.today()
    for employee in employees:
        payroll_history.append({
            "Employee ID": employee["Employee ID"],
            "Name": employee["Name"],
            "Payroll Date": payroll_date,
            "Basic Salary": employee["Basic Salary"],
            "Bonuses": employee["Bonuses"],
            "Deductions": employee["Deductions"],
            "Net Salary": employee["Net Salary"]
        })
    st.success("Payroll processed for all employees.")

# Display payroll slips for each employee
st.header("Payroll Slips")
if payroll_history:
    for record in payroll_history:
        st.write("-------------------------------------------------")
        st.write(f"Employee ID: {record['Employee ID']}")
        st.write(f"Name: {record['Name']}")
        st.write(f"Payroll Date: {record['Payroll Date']}")
        st.write(f"Basic Salary: ${record['Basic Salary']}")
        st.write(f"Bonuses: ${record['Bonuses']}")
        st.write(f"Deductions: ${record['Deductions']}")
        st.write(f"Net Salary: ${record['Net Salary']}")
        st.write("-------------------------------------------------")
else:
    st.info("No payroll slips available. Please run the payroll process.")

# Display Payroll Register
st.header("Payroll Register")
if payroll_history:
    payroll_df = pd.DataFrame(payroll_history)
    st.dataframe(payroll_df)
    
    # Download payroll register as CSV
    csv = payroll_df.to_csv(index=False)
    st.download_button(
        label="Download Payroll Register as CSV",
        data=csv,
        file_name="payroll_register.csv",
        mime="text/csv"
    )
else:
    st.info("No payroll register available. Please run the payroll process.")
