import re
import pandas as pd


def is_valid(s: str) -> bool:
    return bool(re.fullmatch(r'[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com', s))


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users = users[users['mail'].apply(is_valid)]
    return users


if __name__ == "__main__":
    print(valid_emails(users))