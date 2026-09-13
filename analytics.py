def passing_students(students):
    # Yield each student who has passed, one at a time
    for student in students:
        if student.has_passed():
            yield student

def make_grader(pass_mark):
    # Create a function that remembers the chosen pass mark
    def grade(score):
        # Compare the score with the remembered pass mark
        if score >= pass_mark:
            return "Pass"
        return "Fail"

    return grade

def class_average(students):
    # Return the average score for the class
    if not students:
        return 0

    total = 0

    for student in students:
        total += student.score

    return total / len(students)


def highest(students):
    # Return the student with the highest score
    if not students:
        return None

    highest_student = students[0]

    for student in students:
        if student.score > highest_student.score:
            highest_student = student

    return highest_student


def lowest(students):
    # Return the student with the lowest score
    if not students:
        return None

    lowest_student = students[0]

    for student in students:
        if student.score < lowest_student.score:
            lowest_student = student

    return lowest_student


def pass_rate(students):
    # Return the percentage of students who have passed
    if not students:
        return 0

    passed = 0

    for student in students:
        if student.has_passed():
            passed += 1

    return (passed / len(students)) * 100

