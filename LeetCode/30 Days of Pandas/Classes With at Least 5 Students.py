import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    result = result.rename(columns={'event_day': 'day'})
    return result


if __name__ == "__main__":
    print(total_time(employees))