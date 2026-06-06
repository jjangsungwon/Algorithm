import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 == 1), 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values('employee_id')


if __name__ == "__main__":
    print(calculate_special_bouns(employees))
    