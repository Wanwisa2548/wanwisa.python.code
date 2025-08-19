students = {}

while True:
    code = input("Enter code number : ")
    if code == "end":
        break

    name = input("Your name : ")
    age = int(input("Your age : "))
    grade = input("your grade : ")

    students[code] = {
        "name": name,
        "age":age,
        "grade":grade
    }
    print(students)

print("All infomation  ")
for code , info in students.items():
    print(f"Code ",{code} , {info})