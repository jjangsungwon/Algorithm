import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date')['product'].agg(
        num_sold='nunique',
        products=lambda x: ','.join(sorted(set(x)))
    ).reset_index()
    activities = activities.sort_values(by='sell_date')
    return activities


if __name__ == "__main__":
    print(group_sold_products_by_the_date(activities))
    