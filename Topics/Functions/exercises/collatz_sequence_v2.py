xCheck = "❌"

def collatz(number):
    step = 1
    mystring = "Collatz Sequence "
    
    while number != 1:
        if number % 2 == 0:
            print(f"Step {step}: {number}  / 2 = {number // 2}")
            number = number // 2
            step += 1
            if number != 1:
                mystring += str(number) + " -> "
            else: 
                mystring += str(number)
        else:
            print(f"Step {step}: 3 * {number} + 1 = {number * 3 + 1}")
            number = number * 3 + 1
            step += 1
            mystring += str(number) + " -> "

    print(mystring)
    
while True:
    number = int(input("Enter a number: "))
    if number <= 0:
        print("Collatz Sequence is only generated for the numbers greater that zero") 
    else:
       break

collatz(number)