import os
import re
import pandas as pd
from langchain_ollama import OllamaLLM
from open_document import open_file

# Load Llama3
llm = OllamaLLM(model="llama3")

# Project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load CSV
CSV_PATH = os.path.join(BASE_DIR, "employee.csv")
employees = pd.read_csv(CSV_PATH)

print("=" * 50)
print("🤖 HR AI Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    # Find Employee ID
    match = re.search(r"EMP\d+", question.upper())

    if not match:
        print("\nBot : Please mention an Employee ID (Example: EMP1001)")
        continue

    emp_id = match.group()

    result = employees[employees["Employee ID"] == emp_id]

    if result.empty:
        print("\nBot : Employee not found.")
        continue

    employee = result.iloc[0].to_dict()

    prompt = f"""
You are an HR Assistant.

Employee Data:
{employee}

User Question:
{question}

Answer ONLY using the employee data above.
"""

    # Ask Llama
    answer = llm.invoke(prompt)

    print("\nBot :", answer)

    # Open document automatically
    question_lower = question.lower()

    if "photo" in question_lower:
        open_file(os.path.join(BASE_DIR,
                               "Employee_Dataset_Synthetic_100",
                               employee["Photo"]))

    elif "aadhaar" in question_lower:
        open_file(os.path.join(BASE_DIR,
                               "Employee_Dataset_Synthetic_100",
                               employee["Aadhaar"]))

    elif "pan" in question_lower:
        open_file(os.path.join(BASE_DIR,
                               "Employee_Dataset_Synthetic_100",
                               employee["PAN"]))

    elif "degree" in question_lower:
        open_file(os.path.join(BASE_DIR,
                               "Employee_Dataset_Synthetic_100",
                               employee["Degree"]))

    elif "experience" in question_lower:
        open_file(os.path.join(BASE_DIR,
                               "Employee_Dataset_Synthetic_100",
                               employee["Experience"]))