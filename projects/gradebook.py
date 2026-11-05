"""Interactive gradebook. Enter names and scores, then view the results."""

import math


def gradebook(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def main():
    students = []
    print("Gradebook — enter q as a name to finish and view all grades.")
    while True:
        name = input("Student name: ").strip()
        if name.lower() == "q":
            break
        if not name:
            print("Please enter a name.")
            continue
        while True:
            try:
                score = float(input("Numerical grade (0–100): "))
                if not math.isfinite(score) or not 0 <= score <= 100:
                    raise ValueError
                break
            except ValueError:
                print("Enter a number from 0 to 100.")
        students.append([name, score])
        print(f"Hello {name}, your grade is {gradebook(score)}.")
    if students:
        print("\nGradebook summary:")
        for name, score in students:
            print(f"{name}: {score:g} — {gradebook(score)}")
    else:
        print("No students entered.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGradebook closed.")
