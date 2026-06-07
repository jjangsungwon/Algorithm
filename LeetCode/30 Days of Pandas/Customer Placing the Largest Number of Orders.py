import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].count().reset_index(name='cnt')
    orders = orders[orders['cnt'] == orders['cnt'].max()]
    return orders[['customer_number']]


if __name__ == "__main__":
    print(largest_orders(orders))
