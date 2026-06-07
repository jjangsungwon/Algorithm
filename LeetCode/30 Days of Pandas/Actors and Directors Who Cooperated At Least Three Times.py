import pandas as pd

def actors_and_directors(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(['actor_id', 'director_id']).size().reset_index(name='cnt')
    daily_sales = daily_sales[daily_sales['cnt'] >= 3][['actor_id', 'director_id']]
    return daily_sales


if __name__ == "__main__":
    print(actors_and_directors(daily_sales))
    