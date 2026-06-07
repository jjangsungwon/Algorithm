import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts['income'] < 20000]
    print(low_salary)
    medium_salary = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_salary = accounts[accounts['income'] > 50000]
    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [len(low_salary), len(medium_salary), len(high_salary)]})


if __name__ == "__main__":
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
    accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'int64', 'income':'int64'})
    print(count_salary_categories(accounts))