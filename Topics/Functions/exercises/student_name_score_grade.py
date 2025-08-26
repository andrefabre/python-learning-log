# def main():
#     numStudents = int(input("Enter the number of students: "))
#     count = 1
#     while count <= numStudents:
#         name = input(f"Enter the name of student {count}: ")
#         while True:
#             score = int(input(f"Enter score of {name}: "))
#             if 0 <= score <= 100:
#                 break
#             else: continue
#             # Determine Grade
#         finalGrade = grade(score)
#         print(f"Name: {name} -> Score: {score} -> Grade: {finalGrade}")
#         count += 1
import pyinputplus as pyip

def main():
    numStudents = pyip.inputInt(prompt="Enter the number of students: ")
    for i in range(numStudents):
        name = pyip.inputStr(prompt=f"Enter the name of student {i+1}: ")
        while True:
            score = pyip.inputInt(prompt=f"Enter score of {name}: ")
            if 0 <= score <= 100:
                break
            else: continue
            # Determine Grade
        finalGrade = grade(score)
        print(f"Name: {name} -> Score: {score} -> Grade: {finalGrade}")
        
def grade(score):
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"
    return grade 

main()