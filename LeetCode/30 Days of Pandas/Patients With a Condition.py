import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients['conditions'].str.contains(r'(^|\s)DIAB1', regex=True)
    return patients[mask]


if __name__ == "__main__":
    print(find_patients(patients))