# Basic set operations สร้าง set ขึ้นมา
fruits = {"apple", "banana", "orange", "grape"}
citrus = {"orange", "lemon", "lime", "grapefruit"}

print(f"Fruits: {fruits}") # โชว์ข้อมูลในlist
print(f"Citrus: {citrus}")

# Adding elements เพิ่มข้อมูล(strawberry) เข้าไปใน list
fruits.add("strawberry")
print(f"After adding strawberry: {fruits}")

# Adding multiple elements 
fruits.update(["kiwi", "mango"])
print(f"After adding multiple: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises error if not found ถ้าไม่เจอมันจะขึ้น error
print(f"After removing banana: {fruits}")

fruits.discard("pineapple")  # No error if not found มันจะไม่โชว์ error จะไม่มีอะไรเกิดขึ้น
print(f"After discarding pineapple: {fruits}")

removed_fruit = fruits.pop()  # Remove arbitrary element
print(f"Removed: {removed_fruit}")
print(f"Remaining fruits: {fruits}")

# Set mathematical operations สร้าง set ที่เป็นทางคณิตศาสตร์
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}") # โชว์ข้อมูลใน set
print(f"Set B: {set_b}")

# Union (all elements from both sets) เอาทั้ง 2 เซ็ตมาอยู๋ด้วยกัน ถ้าตัวเลขซ้ำ ก็ตัดออก
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union (A | B): {union}")

# Intersection (common elements)
intersection = set_a & set_b  # or set_a.intersection(set_b) เอาตัวที่ซ้ำกัน
print(f"Intersection (A & B): {intersection}")

# Difference (elements in A but not in B) มีใน A แต่ไม่อยู่ใน B
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference}")

# Symmetric difference (elements in either A or B, but not both)เอาผลลัพธ์ของการยูเนียน แล้วเอามาลบกับอินเตอร์เซ็ค จะได้ผลลัพธ์
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {sym_diff}")

# ทำไมต้องมีโครงสร้างข้อมูลชื่อ set ด้วย เพราะว่ามี operater ที่สามารถยูเนียน อิเตอร์เซ็คได้ ไม่ต้องเขียนวนลูป ลดขั้นตอนลง