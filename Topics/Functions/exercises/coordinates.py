
n = int(input("Enter the value of n: "))
counter = 0

for i in range(n+1):
    for j in range(n+1):
        if (i + j) % 2 != 0 and (i * j) % 3 == 0:
            print(f"Valid coordinate: {i, j}")
            isValid += 1
            
print(f"Number of valid coordinates: {counter}")