import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(employee_uni, on='id', how='left')
    return employees[['unique_id', 'name']] 


if __name__ == "__main__":
    print(replace_employee_id(employees, employee_uni))