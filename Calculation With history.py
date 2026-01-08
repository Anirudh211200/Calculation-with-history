# CALCULATION WITH HISTORY
# Demonstrates how to perform calculations using historical data in a DataFrame.



History_File = "history.txt"

def show_history():
    file = open(History_File, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        for line in lines:
            print(line.strip())
    file.close()

def clear_history():
    file = open(History_File, "w")
    file.write("")
    file.close()
    print("History cleared.")   

def save_to_history(equation, result):
    file = open(History_File, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Use: number1 operator number2")
        return
    
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])  
    except ValueError:
        print("Invalid numbers.")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Unsupported operator. Use +, -, *, or /.")
        return  
    
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result) 

def main():
    print("---simple calculator with history---")
    while True:
        user_input = input("Enter Calculation (+ - * /) or 'history', 'clear', 'exit': ").strip().lower()
        if user_input == 'exit':
            print("Exiting calculator.")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()