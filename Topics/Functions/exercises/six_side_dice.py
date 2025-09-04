
count = 0
for i in range(1,7):
    for j in range(1, 7):
        if i + j == 7:
            sum = i + j
            print(f"({i}, {j}) Sum: {sum}")
            count += 1
            