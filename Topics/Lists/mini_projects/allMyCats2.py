catNames = []
while True:
    print(f"Enter the name of cat {len(catNames) + 1} (or enter nothing to stop)")
    name = input()
    if name == "":
        break
    catNames += [name] # concatentate list

print("The cat names are: ")
for name in catNames:
    print(f"\t{name}")