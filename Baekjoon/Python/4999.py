import sys

if __name__ == "__main__":
    
    patient = list(input())    # 환자 기침 길이
    doctor = list(input())     # 의사 기침 길이
    
    # 길이 비교
    if len(patient) >= len(doctor):
        print("go")
    else:
        print("no")