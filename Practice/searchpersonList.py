person = []

while True:
    name = input("Enter your name :")
    if name.lower() == "end":
        break
    person.append(name)
    print(person)

print("All info")
for i,info in enumerate(person,start=1):
    print(f"{i} name:{info}")

search_name = input("What name you will search : ")
if search_name in person:
    print(f"Yes '{search_name}' happend")
else:
    print(f"No '{search_name}' happend")
