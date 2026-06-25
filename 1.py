print("Simple Calculator")
print("Type exit to stop.")

while True:
    expression = input("> ")
    if expression == "exit":
        break

    try:
        print(eval(expression))
    except Exception:
        print("Invalid input")
