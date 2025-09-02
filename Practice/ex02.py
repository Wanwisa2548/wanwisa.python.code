students = []

while True:
    name = input("Enter name  : ")
    if name == "end":
        break
    students.append(name)
print(students)

search_name = input("Enter name to search : ")
if search_name in students:
    print(f"Name '{search_name} ' happend")
else:
    print(f"Name '{search_name}'  No Happend")


""""
to_remove = input("Enter name need to remove : ")
if to_remove in students:
    students.remove(to_remove)
    print(to_remove)
print(students)
"""""