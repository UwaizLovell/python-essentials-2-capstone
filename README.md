# Python Essentials 2 — Student Analytics Toolkit

The Student Analytics Toolkit is a Python terminal program that generates messy student data, cleans the records, turns them into Student objects, analyses the results, and exports a report. The project brings together the Python Essentials 1 foundation and Python Essentials 2 Modules 1–4 in one multi-file program.

## 1. Student Information

Name: Uwaiz Slade Lovell  
Cohort: 2026 DS Jan Cohort

## 2. Features

- Generate a sample student data file with messy records
- Clean student names and scores when loading the file
- Create Student objects from the cleaned records
- Display all students with their grades
- Calculate the class average
- Find the highest and lowest scoring students
- Calculate the class pass rate
- Use a generator to find passing students
- Use a closure for a custom pass mark
- Use an iterator with iter() and next()
- Display environment information
- Display date and calendar information
- Export analytics results to a report file
- Keep an activity log with timestamps
- Handle invalid menu and numeric input without crashing

## 3. How to Run

Clone the repository:

    git clone https://github.com/UwaizLovell/python-essentials-2-capstone.git

Move into the project folder:

    cd python-essentials-2-capstone

Install the requirements:

    pip install -r requirements.txt

Run the program:

    python main.py

## 4. Project Structure

main.py — Controls the menu and connects the different parts of the program.

models.py — Contains the Student and HonoursStudent classes.

data_tools.py — Generates, cleans, loads, exports, and logs student data.

analytics.py — Contains the generator, closure, iterator, and statistical functions.

reporting.py — Creates environment, date, and calendar reports.

requirements.txt — Contains the project requirements.

README.md — Explains the project and how to run it.

CONCEPTS.md — Explains the Python concepts used in the project.

data/ — Stores generated data, reports, and activity logs.

## 5. Concepts Demonstrated

The project uses Python Essentials 1 foundations together with Python Essentials 2 Modules 1–4.

- Variables, strings, numbers, lists, loops, conditions, functions, and input
- File handling with open(), read, write, and append
- String cleaning with strip(), split(), title(), and int()
- Object-oriented programming with classes, objects, methods, instance variables, and class variables
- Inheritance with HonoursStudent and super()
- Generators with yield
- Closures that remember a custom pass mark
- Iterators using iter() and next()
- Standard library modules including random, os, platform, datetime, and calendar

## 6. Sample Output

Example menu:

    ===== STUDENT ANALYTICS TOOLKIT =====
    1. Generate sample data file
    2. Load & clean records from file
    3. View all students
    4. Analyse (averages, pass/fail, top student)
    5. Filter students (generator)
    6. Grade with a custom pass mark (closure)
    7. Environment & date report
    8. Export results to a file
    9. Exit
    Choose an option (1-9):
