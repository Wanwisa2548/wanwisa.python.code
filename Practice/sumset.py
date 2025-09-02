numbers = set()
while True:
    n = input("Enter your Number :")
    if n == "stop":
        break
    numbers.add(int(n))
print("set is :",numbers)
print("Total is :", sum(numbers))