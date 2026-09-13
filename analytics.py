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

