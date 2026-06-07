import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.groupby('managerId').size()
    manager_ids = counts[counts >= 5].index
    result = employee[employee['id'].isin(manager_ids)][['name']]
    return result


if __name__ == "__main__":
    print(find_managers(employee))