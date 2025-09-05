
n = int(input("Enter the value of n: "))
print(f"First {n} triangular numbers are: ", end=" ")
num = 0
for i in range(1, n+1):
    num += i
    print(f"{num}", end=" ")
