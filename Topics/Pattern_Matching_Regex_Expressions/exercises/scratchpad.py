# # string  = "$50.00"
# # string = float(string[1:-1])
# # print(string, type(string))
# # # # newValue = float(string.strip("$").string[:-1])
# # # # print(newValue)
# # p = "15%"
# # new = float(p[0:-1]) / 100
# # print(type(new))

# fileName = "something.txt.pdf"



# if "." not in fileName:
#     print(f"application/octet-stream")
# else:
#     if fileName.endswith(".gif"):
#         extension = "image/gif"
#     elif fileName.endswith(".jpg"):
#         extension = "image/jpeg"
#     elif fileName.endswith(".jpeg"):
#         extension = "image/jpeg"
#     elif fileName.endswith(".png"):
#         extension = "image/png"
#     elif fileName.endswith(".pdf"):
#         extension = "application/pdf"
#     elif fileName.endswith(".txt"):
#         extension = "text/plain"
#     elif fileName.endswith(".zip"):
#         extension = "application/zip"
#     else:
#         extension = "application/octet-stream"
#     print(f"{extension}")


# myExpression = ["1", "+", "2"]
# x, y, z = myExpression
# if y == "+":
#     result = int(x) + int(z)
# print(f"{result:.1f}")

# myExpression = "1 + 2"
# x, y, z = myExpression.split()
# print(x)

# myString = "7:00"
# hours, minutes = myString.split(":")
# totalHours = float(hours) + (float(minutes) / 60)
# print(totalHours)

# if 7 <= totalHours <= 8:
#     print("Breakfast")
# if 12 <= totalHours <= 13:
#     print("Lunch")
# if 18 <= totalHours <= 19:
#     print("Dinner")
    
# myString = "7:00 a.m. and 8:00 a.m."
# if "a.m." or "p.m" in myString:
#     newString = myString.replace("a.m.", "").replace("and", "").strip()
#     first, second = newString.split()
#     firstHours, firstMinutes = first.split(":")
#     firstTime = float(firstHours) + (float(firstMinutes) / 60)
#     secondHours, secondMinutes = second.split(":")
#     secondTime = float(secondHours) + (float(secondMinutes) / 60)    
#     if 7 <= firstTime and secondTime <= 8:
#         print(firstTime)# 7:00 11:00
#     if 12 <= firstTime <= 12.59 and secondTime <= 8:

# COME BACK TO THe CODE ABOVE

# myVar = "camelCase"
# if myVar.islower():
#     print(myVar)
# for i in range(len(myVar)):
#     if myVar[i].isupper():
#         myVar = myVar.replace(myVar[i], "_" + myVar[i].lower())
#         print(myVar)

# amountDue = 50
# count = 0
# print(f"Amount Due: {amountDue}")
# while count < 50:
#     coin = int(input("Insert Coin: "))
#     if coin not in [5, 10, 25]:
#         continue
#     else:
#         amountDue -= coin
#         print(f"Amount Due: {amountDue}")

# myString = "Twitter"
# vowelS ="AaEeIiOoUu"
# newString = ""
# for i in range(len(myString)):
#     if myString[i] not in vowelS:
#         newString += myString[i]
    

# print(newString)    

def triangle(n):
    if n == 1:
        print(n)
    else:
        print(triangle(n - 1))

triangle(2)
n = 2

n = 1
t = 6
total = 0
for i in range(1,t+1):
    total = total + i
    print(total, end=" ")
    

