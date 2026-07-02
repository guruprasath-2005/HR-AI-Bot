import pandas as pd

employees = pd.read_csv("employee.csv")

emp = employees.iloc[0]

print("=" * 40)

for column in employees.columns:
    print(f"{column:15}: {emp[column]}")