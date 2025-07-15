direction = input("What is your conversion direction (1: THB to USD, 2: USD to THB)")
amount = float(input("Amount to convert: "))

if direction == "1":
    result = amount / 35.5
    print("Result: ", result," USD")

if direction == "2":
    print("Result: ", result, " THB")