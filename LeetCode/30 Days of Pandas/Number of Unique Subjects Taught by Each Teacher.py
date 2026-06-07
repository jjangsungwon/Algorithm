import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
    return teacher


if __name__ == "__main__":
    print(count_unique_subjects(teacher))
