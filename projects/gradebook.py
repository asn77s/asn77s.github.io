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


# Fictional sample data for this demonstration.
students = [["Student 1", 90], ["Student 2", 80], ["Student 3", 75]]

for student in students:
    name = student[0]
    num_grade = student[1]
    letter_grade = gradebook(num_grade)
    print("Hello", name, "your grade is", letter_grade)
