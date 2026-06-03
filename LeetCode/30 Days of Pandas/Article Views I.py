import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views['author_id'] == views['viewer_id']]
    return result[['author_id']].rename(columns={'author_id': 'id'}).sort_values('id').asc()


if __name__ == "__main__":
    print(article_views(views))