from logo import logo

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide (n1, n2):
    return n1 / n2

#operator dictionary for calculations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("Welcome to the calculator app! What is the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with the number {answer}, type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()