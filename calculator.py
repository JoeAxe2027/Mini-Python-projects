def calculate(first_operand, operator, second_operand):
    try:
        num1 = float(first_operand)
        num2 = float(second_operand)
    except ValueError:
        print("Error. The first operand should be a number. Program terminates.")
        return


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error. You cannot divide by zero.")
            return
    else:
        print("Error. Invalid operator.")
        return
    print(f"The result of {num1} {operator} {num2} is: {result}")

if __name__ == "__main__":

    first_operand = input("Enter the first operand: ")
    operator = input("Enter the operator: +, -, *, /:")
    second_operand = input("Enter the second operand:")
    calculate(first_operand, operator, second_operand)




