def factorial():
    n = int(input("Enter number: "))
    total = 1
    for i in range(1, n + 1):
        total *= i
    print(total)

factorial()
