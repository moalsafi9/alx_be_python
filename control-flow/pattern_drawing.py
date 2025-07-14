number = int(input("Enter the size of the pattern:"))

i = 0
while(i < number):
    for j in range(1, number + 1):
        print("*", end="")
    i += 1
    print("\n")