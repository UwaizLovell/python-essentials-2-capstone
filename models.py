class Student:
    # Class variables shared by all Student objects
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        # Store the student's information as instance variables
        self.name = name
        self.student_id = student_id
        self.score = score

        # Increase the total student count whenever a Student is created
        Student.total_students += 1

    def get_grade(self):
        # Return a grade based on the student's score
        if self.score >= 80:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "Fail"

    def has_passed(self):
        # Return True when the student has achieved a passing score
        return self.score >= 50

    def __str__(self):
        # Return a clean, readable description of the student
        return f"{self.student_id}: {self.name} | Score: {self.score} | Grade: {self.get_grade()}"

    