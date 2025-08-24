
import random

def marks(mark):
    
    if mark < 0 or mark > 100:
        print("Invalid marks entered")
    else:
        if 50 <= mark <= 100:
            print("Pass")
            if 90 <= mark <= 100:
                grade = "A+";
            elif 80 <= mark <= 89:
                grade = "A"
            elif 70 <= mark <= 79:
                grade = "B"
            elif 60 <= mark <= 69:
                grade = "C"
            else:
                grade = "D"
            print(f"Grade: {grade}")
        else:
            print("Fail")
            if 40 <= mark <= 49:
                grade = "E"
            else:
                grade = "F"
            print(f"Grade: {grade}")

# Instead of user input, unit testing with the below

# Bounds checking unit tests
# print("Unit Test 1: mark < 0, Expected result: Invalid marks entered")
# marks(-1) # Invalid marks entered
# print("Unit Test 2: mark > 100, Expected result: Invalid marks entered")
# marks(101) # Invalid Marks EnteredFail, Grade F
# print("Unit Test 3: mark == 0, Expected result: Fail Grade: F")
# marks(0)
# print("Unit Test 4: mark == 39, Expected result: Fail Grade: F")
# marks(39)
# print("Unit Test 5: mark == 40, Expected result: Fail Grade: E")
# marks(40)
# print("Unit Test 6: mark == 41, Expected result: Fail Grade: E")
# marks(41)
# print("Unit Test 7: mark == 40, Expected result: Fail Grade: E")
# marks(49)
# print("Unit Test 8: mark == 50, Expected result: Pass Grade: D")
# marks(50)
# print("Unit Test 8: mark == 51, Expected result: Pass Grade: D")
# marks(51)
# print("Unit Test 9: mark == 59, Expected result: Pass Grade: D")
# marks(59)
# print("Unit Test 10: mark == 60, Expected result: Pass Grade: C")
# marks(60)
# print("Unit Test 11: mark == 61, Expected result: Pass Grade: C")
# marks(61)
# print("Unit Test 12: mark == 69, Expected result: Pass Grade: C")
# marks(69)
# print("Unit Test 13: mark == 70, Expected result: Pass Grade: B")
# marks(70)
# print("Unit Test 14: mark == 71, Expected result: Pass Grade: B")
# marks(71)
# print("Unit Test 14: mark == 79, Expected result: Pass Grade: B")
# marks(79)
# print("Unit Test 15: mark == 80, Expected result: Pass Grade: A")
# marks(80)
# print("Unit Test 16: mark == 81, Expected result: Pass Grade: A")
# marks(81)
# print("Unit Test 17: mark == 89, Expected result: Pass Grade: A")
# marks(89)
# print("Unit Test 18 mark == 90, Expected result: Pass Grade: A+")
# marks(90)
# print("Unit Test 19: mark == 91, Expected result: Pass Grade: A+")
# marks(91)
# print("Unit Test 20: mark == 99, Expected result: Pass Grade: A+")
# marks(99)
# print("Unit Test 21: mark == 100, Expected result: Pass Grade: A+")
# marks(100)

# 20 Tests of random generate marks between 0 and 120

myMarks = [mark for mark in range(0, 121)]

for i in range(11):
    test_mark = random.choice(myMarks)
    print(f"Enter your marks (0-100) {test_mark}")
    marks(test_mark)

