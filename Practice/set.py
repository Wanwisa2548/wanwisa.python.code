A = set()


print("Input Data")
while True:
    item = input("A : ")
    if item == "end":
        break
    A.add(item)

B = set()
while True:
    item = input("B : ")
    if item == "end":
        break
    B.add(item)

print("A - B", A.difference(B))
print("B - A", B.difference(A))

print("Intersection ", A.intersection(B))
print("Symmetric Difference ", A.symmetric_difference(B))