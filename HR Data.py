# I imported the libraries and make sure to have these installed
import os
import zipfile
import pandas as pd
import numpy as np
from kaggle.api.kaggle_api_extended import KaggleApi

# Set the Kaggle configuration directory to a file that can be located within file explorer
os.environ['KAGGLE_CONFIG_DIR'] = "C:/Users/mason/.kaggle"
print(os.path.getsize('HRDataset_v14.csv') / (1024 * 1024), "MB")  # File size in MB

# Authenticate and download the dataset from kaggle
api = KaggleApi()
api.authenticate()
dataset = "rhuebner/human-resources-data-set"
download_path = "./"
print("Downloading dataset...")
api.dataset_download_files(dataset, path=download_path, unzip=True)

# Load the extracted dataset into visual studio code for analysis
HR = pd.read_csv("HRDataset_v14.csv")

# Inspect dataset structure
print(" ")
print(HR.info())
print(" ")
print(HR.head())

# Count unique managers per department
manager_counts = HR.groupby('Department')['ManagerName'].nunique().reset_index()
manager_counts.columns = ['Department', 'Unique_Manager_Count']
print(" ")
print("Manager Counts")
print(manager_counts)

# Count the number of employees in the Production department
production_count = HR[HR['Department'].str.strip() == 'Production'].shape[0]

# Display the count
print(f"Number of employees in the Production department: {production_count}")

# Filter for managers in the Production department
production_managers = HR[HR['Department'].str.strip() == 'Production']['ManagerName'].dropna().unique()

# Display unique managers
print(" ")
print("Managers in the Production Department:")
for manager in production_managers:
    print(manager)
# Count the occurrences of each race in the dataset
race_count = HR['RaceDesc'].str.strip().value_counts()

# Display the counts to see diversity profile
print(" ")
print("Race distribution in the workplace:")
print(race_count)

# Average pay by position
average_pay_by_position = HR.groupby('Position')['Salary'].mean().reset_index()
average_pay_by_position.columns = ['Position', 'Average_Salary']
average_pay_by_position = average_pay_by_position.sort_values(by='Average_Salary', ascending=False)

# Display the average pay by position, sorted
print(" ")
print("Average Pay by Position (Highest to Lowest):")
print(average_pay_by_position)

# Average pay by department. HR groupby is used to group the conditions department and salary. 
# Salary.mean() gives the average pay
average_pay_by_department = HR.groupby('Department')['Salary'].mean().reset_index()
average_pay_by_department.columns = ['Department', 'Average_Salary']
average_pay_by_department = average_pay_by_department.sort_values(by='Average_Salary', ascending=False)

# Display the average pay by department from code above, sorted. \n creates a new line
print("\nAverage Pay by Department (Highest to Lowest):")
print(average_pay_by_department)

# Filter for terminated employees
terminated_employees = HR[HR['EmploymentStatus'].str.contains("Terminated", na=False)]
terminated_for_Cause_employees = HR[HR['EmploymentStatus'].str.contains("Terminated for Cause", na=False)]
print(" ")
print(terminated_for_Cause_employees)
print(" ")
print(terminated_employees)

# Count the number of terminated employees in each department
termination_counts_by_department = terminated_employees.groupby('Department').size().reset_index(name='Terminated_Count')

# Display the results
print(" ")
print("Terminated Employees by Department:")
print(termination_counts_by_department)

