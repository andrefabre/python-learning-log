
decimal_number = int(input("Enter the decimal number: "))
base_number = int(input("Enter the base: "))
result = []

while decimal_number > 0:
    value_remainder = decimal_number % base_number
    print(value_remainder)
    result.insert(0, str(value_remainder))
    decimal_number //= base_number

result = int("".join(result))
print(f"Final result is: {result}")