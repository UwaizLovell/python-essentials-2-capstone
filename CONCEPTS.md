# Project Concepts

## 1. Python Essentials Module Mapping

### models.py

The main concepts in models.py come from the Python Essentials object-oriented programming material.

The Student class uses __init__() to initialise each object. Instance variables store the student's name, student ID, and score.

The class also uses class variables. school_name is shared by the Student class, while total_students keeps track of how many Student objects have been created.

The class contains methods for getting a grade, checking whether a student has passed, and displaying the student using __str__().

HonoursStudent demonstrates inheritance. It inherits from Student, uses super() to call the parent class constructor, adds research_topic, and overrides get_grade().

### data_tools.py

data_tools.py uses file handling and string processing.

generate_data_file() uses random to create messy student records and writes them to a text file.

load_students() reads the file and cleans each record using strip(), split(), title(), and int().

export_report() writes the final report to a file.

log_event() uses append mode to add timestamped activity messages to the activity log.

### analytics.py

analytics.py uses generators, closures, iterators, functions, loops, conditions, and numerical calculations.

passing_students() is a generator because it uses yield to produce passing students one at a time.

make_grader() demonstrates a closure. The inner grade() function remembers the pass_mark from the outer function.

first_passing_student() demonstrates the iterator protocol by using iter() and next().

The statistical functions calculate the class average, highest score, lowest score, and pass rate.

### reporting.py

reporting.py uses standard library modules from the Python Essentials material.

platform and os are used for environment information such as the operating system, Python version, working directory, and file information.

datetime is used for dates and timestamps.

calendar is used to check leap years and the number of days in the current month.

### main.py

main.py connects all the other files together.

It uses imports, functions, a while loop, if/elif/else conditions, input, and try-except for invalid numeric input.

The main program controls the menu while the other files contain most of the actual functionality.

## 2. Why Split the Program Into Several Files?

The project is split into several files so that each file has a clear responsibility.

models.py is responsible for the student classes.

data_tools.py is responsible for files and data.

analytics.py is responsible for analysing students.

reporting.py is responsible for environment and date reports.

main.py is responsible for controlling the menu and connecting everything.

This makes the project easier to read, test, and understand than putting the entire program into one large file.

## 3. Class vs Object

A class is a blueprint used to create objects.

In this project, Student is the class.

For example:

    student = Student("Lisa", "S1", 72)

student is an object created from the Student class.

The object has its own instance variables such as name, student_id, and score.

## 4. Generator vs Normal Function

A normal function can use return to give back a result.

The passing_students() function is a generator because it uses yield.

Instead of creating and returning a complete list of passing students, it produces each passing student one at a time.

This is shown in the project with:

    for student in students:
        if student.has_passed():
            yield student

## 5. Closure

A closure is an inner function that remembers a value from its outer function.

In this project, make_grader() receives a pass mark and returns the inner grade() function.

The grade() function remembers the pass mark even after make_grader() has finished.

For example:

    grader = make_grader(70)

The grader can then use 70 as its pass mark when checking student scores.

Different graders can remember different pass marks.

## 6. Write Mode and Append Mode

The project uses write mode when creating or replacing a file.

For example:

    with open("data/report.txt", "w") as file:
        file.write(text)

The "w" mode writes the report to the file.

The activity log uses append mode:

    with open("data/activity.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

The "a" mode adds the new message to the existing file instead of replacing the previous log entries.

## 7. Hardest Part of the Project

The hardest part was combining the different Python Essentials concepts into one working program.

Each concept works on its own, but the challenge was connecting them together.

The project solves this by separating the responsibilities into different files and then using main.py to connect them through the menu.

The data moves through a clear pipeline:

    Generate raw data
    ↓
    Clean the data
    ↓
    Create Student objects
    ↓
    Analyse the students
    ↓
    Generate reports
    ↓
    Export results

This allowed the file handling, OOP, generators, closures, iterators, statistics, and date/environment features to work together as one application.