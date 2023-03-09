def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


flag = 1

while flag:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    # menu input with typecast to int
    operation = int(input("Enter [1, 2, 3, 4]: "))

    # enter numbers with typecast to int
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    # check which operation to use
    if operation == 1:
        answer = add(x, y)
    elif operation == 2:
        answer = subtract(x, y)
    elif operation == 3:
        answer = multiply(x, y)
    elif operation == 4:
        answer = divide(x, y)
    else:
        print("Invalid input")

    print("Answer: ", answer)
    again = input("Try again? y/n: ")

    if again == "y":
        flag = 1
    else: # terminate
        flag = 0