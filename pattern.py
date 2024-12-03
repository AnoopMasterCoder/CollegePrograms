num = int(input("Enter the number to print pattern for: "))

for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


