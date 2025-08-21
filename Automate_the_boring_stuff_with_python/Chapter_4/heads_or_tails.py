# import random
# numOfStreaks = 0
# headsOrTails = []
# myString = ""

# for experimentNumber in range(10_000):
        
#     for coinFlips in range(100):
#         if random.randint(0,1) == 0:
#             myString += "H"
#         else:
#             myString += "T"

#     for i in range(len(myString)-5):
#         myNewString = myString[i: i + 6]
#         if myNewString == "HHHHHH" or myNewString == "TTTTTT":
#             numOfStreaks += 1
    
#     myString = ""
# #print(myString)
# print(f"Number of streaks: {numOfStreaks}")
# print(f"Chance of streak: {(numOfStreaks / 10000)}%")
