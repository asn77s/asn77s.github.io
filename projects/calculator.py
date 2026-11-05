"""A four-operation calculator. Run this file to see 10 + 10."""


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


if __name__ == "__main__":
    result = calculator(10, 10, "+")
    print(result)
