import pandas as pd

def students_and_examinations(students, subjects, examinations):
    counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    result = students.merge(subjects, how='cross').merge(counts, how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    result['attended_exams'] = result['attended_exams'].astype(int)
    result = result.sort_values(['student_id', 'subject_name'])
    return result


if __name__ == "__main__":
    print(students_and_examinations(students, subjects, examinations))