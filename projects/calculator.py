"""Interactive calculator. Run with Python 3; enter q to quit."""

import math


def calculator(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Cannot divide by zero"
        return n1 / n2
    return "You didn't enter a valid operation"


def main():
    print("Calculator — enter q at any prompt to quit.")
    while True:
        first = input("First number: ").strip()
        if first.lower() == "q":
            break
        second = input("Second number: ").strip()
        if second.lower() == "q":
            break
        op = input("Operation (+, -, *, /): ").strip()
        if op.lower() == "q":
            break
        try:
            n1, n2 = float(first), float(second)
            if not math.isfinite(n1) or not math.isfinite(n2):
                raise ValueError
        except ValueError:
            print("Enter two valid, finite numbers.")
            continue
        result = calculator(n1, n2, op)
        if isinstance(result, (int, float)):
            print(f"Result: {result:g}" if math.isfinite(result)
                  else "Result is too large. Try smaller numbers.")
        else:
            print(result)
    print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
