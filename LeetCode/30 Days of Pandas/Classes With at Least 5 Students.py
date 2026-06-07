import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count().reset_index(name='cnt')
    courses = courses[courses['cnt'] >=5 ]
    return courses[['class']]


if __name__ == "__main__":
    print(find_classes(courses))
    
