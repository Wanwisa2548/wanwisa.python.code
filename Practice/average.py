number = []
odd_number = []
even_number = []

while True:
    n = (input("Enter Number : "))
    if n == "end":
        break
    n = int(n)
    number.append(n)
    print(number)
    if n % 2 == 0:
        even_number.append(n)
    else:
        odd_number.append(n)
    
average = sum(number)/len(number)

print("Sum ",sum(number))
print("Max ",max(number))
print("Min ",min(number))
print("Average ",average)
print("Even number : ",even_number)
print("Odd number ", odd_number)