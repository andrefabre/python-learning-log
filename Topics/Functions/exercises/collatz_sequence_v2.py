
def collatz(num):
    step = 1
    mystring = ""
    
    while num != 1:
        if num % 2 == 0:
            print(f"Step {step}: {num}  / 2 = {num // 2}")
            num = num // 2
        else:
            print(f"Step {step}: 3 * {num} + 1 = {num * 3 + 1}")
            num = num * 3 + 1

        step += 1
        if num != 1: mystring += str(num) + " -> "
        else: mystring += str(num)
    
    print("Collatz Sequence: " + mystring)

def main():
    while True:
        num = int(input("Enter a num: "))
        if num <= 0:
            print("Collatz Sequence is only generated for the numbers greater that zero") 
        else:
            break
        
    collatz(num)

main()