number = []

for i in range(5):
    n = input("Enter number : ")
    n = int(n)
    number.append(n)
    average = sum(number)/len(number)

print(number)
print("Average is ",average)