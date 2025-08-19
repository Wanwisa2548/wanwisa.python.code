#หาผลรวมของ list

numbers = []

while True:
    n = input("Enter number : ")
    if n == "end":
        break
    numbers.append(int(n))
print("Total is :",sum(numbers))



