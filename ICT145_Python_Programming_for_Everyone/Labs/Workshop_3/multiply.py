
num = int(input("Enter a number: "))
print(f"\nMultiplication of {num}\n")
while True:
    for i in range(1, 11):
        result = i * num
        print(f"{num} x {i} = {result}")
    break
print()
