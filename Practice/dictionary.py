students = {}
while True:
    code = input("number code : ")
    if code == "end":
        break

    name = input("Your name : ")
    age = int(input("Your age : "))
    grade = input("Your grade : ")

    students[code] = {
        "name":name,
        "age":age,
        "grade":grade
    }
print("All info ")
for code , info in students.items():
    print(f"code {code} : {info}")