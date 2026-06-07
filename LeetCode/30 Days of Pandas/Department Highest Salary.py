import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('', '_department'))
    employee = employee.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    employee = employee[['name_department', 'name', 'salary']]
    employee.columns = ['Department', 'Employee', 'Salary']
    return employee


if __name__ == "__main__":
    print(department_highest_salary(employee, department))   
    