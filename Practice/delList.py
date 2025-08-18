numbers=[]

while True:
    n = input("Enter number : ")
    if n == "end":
        break
    numbers.append(int(n))
    print(numbers)
to_remove = int(input("number need to rempve : "))
if to_remove in numbers:
    numbers.remove(to_remove)
    print(numbers)