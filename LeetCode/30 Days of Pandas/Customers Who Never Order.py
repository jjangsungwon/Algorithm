import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats'] == "Y") & (products['recyclable'] == "Y")]
    return result[['product_id']]


if __name__ == "__main__":
    print(find_products(products))