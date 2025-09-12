history_file = "history.txt"

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found.")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")

def clear_history():
    open(history_file, 'w').close()
    print("History cleared.")

def save_to_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8 + 8)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /.")
        return

    
    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("--- SIMPLE CALC (type 'history', 'clear', or 'exit') ---")
    while True:
        user_input = input("Enter calculation (+ - * /): ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculator(user_input)

main()
