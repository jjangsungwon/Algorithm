import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct = employee['salary'].drop_duplicates().sort_values(ascending=False)
    col = f'getNthHighestSalary({N})'
    if N < 1 or len(distinct) < N:
        return pd.DataFrame({col: [None]})
    return pd.DataFrame({col: [distinct.iloc[N - 1]]})


if __name__ == "__main__":
    print(nth_highest_salary(employee, N))