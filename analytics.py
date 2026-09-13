def passing_students(students):
    # Yield each student who has passed, one at a time
    for student in students:
        if student.has_passed():
            yield student