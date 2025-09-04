
# def gcd(a, b):
#     # if a >= b: num, denom = a, b
#     # else: num, denom = b, a
#     num, denom = b, a
#     remainder = num % denom
#     result = num // denom
    
#     if remainder == 0:
#         print(f"Step {num} / {denom} = {result}, remainder {remainder}")
#         print(f"\nGCD of {first} and {second} is: {denom}")
#     else:
#         print(f"Step {num} / {denom} = {result}, remainder {remainder}")
#         gcd(remainder, denom)
    
def gcd(a, b):
    
    if a >= b: num, denom = a, b
    else: num, denom = b, a
    step = 1
    
    while True:
        
        remainder = num % denom
        result = num // denom
        
        if remainder == 0:
            # hcf = denom
            print(f"Step {step} {num} / {denom} = {result}, remainder {remainder}")
            print(f"\nGCD of {first} and {second} is: {denom}")
            break
        else:
            print(f"Step {step} {num} / {denom} = {result}, remainder {remainder}")
            step += 1
            num = denom
            denom = remainder
            
            #gcd(denom, expr)
 

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
# step = 0
gcd(first, second)

# print(gcd(8, 12))
# print(gcd(100, 25))
# print(gcd(13, 7))

