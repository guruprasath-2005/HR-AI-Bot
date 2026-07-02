import os
import pandas as pd
from open_document import open_file

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load employee CSV
CSV_PATH = os.path.join(BASE_DIR, "employee.csv")
employees = pd.read_csv(CSV_PATH)

while True:
    emp_id = input("\nEnter Employee ID (or type exit): ").strip().upper()

    if emp_id == "EXIT":
        print("Goodbye!")
        break

    result = employees[employees["Employee ID"] == emp_id]

    if result.empty:
        print("❌ Employee not found.")
    else:
        employee = result.iloc[0]

        print("\n" + "=" * 50)
        print("Employee Details")
        print("=" * 50)

        for column in employees.columns:
            print(f"{column:<15}: {employee[column]}")

        print("\nChoose a document:")
        print("1. Photo")
        print("2. Aadhaar")
        print("3. PAN")
        print("4. Degree")

        choice = input("Enter your choice: ")

        if choice == "1":
            open_file(os.path.join(BASE_DIR, "Employee_Dataset_Synthetic_100", employee["Photo"]))
        elif choice == "2":
            open_file(os.path.join(BASE_DIR, "Employee_Dataset_Synthetic_100", employee["Aadhaar"]))
        elif choice == "3":
            open_file(os.path.join(BASE_DIR, "Employee_Dataset_Synthetic_100", employee["PAN"]))
        elif choice == "4":
            open_file(os.path.join(BASE_DIR, "Employee_Dataset_Synthetic_100", employee["Degree"]))
        else:
            print("Invalid choice.")