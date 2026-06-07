import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # find sales_id
    red_com_ids = company[company['name'] == 'RED']['com_id']
    red_sales_id = orders[orders['com_id'].isin(red_com_ids)]['sales_id'].unique()
    sales_person = sales_person[~sales_person['sales_id'].isin(red_sales_id)]
    return sales_person[['name']]


if __name__ == "__main__":
    print(sales_person(sales_person, company, orders))