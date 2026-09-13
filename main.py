from models import Student, HonoursStudent
from data_tools import generate_data_file, load_students, export_report, log_event
from analytics import (
    passing_students,
    make_grader,
    class_average,
    highest,
    lowest,
    pass_rate,
    first_passing_student
)
from reporting import environment_report, date_report

def display_menu():
    # Display the main Student Analytics Toolkit menu
    print("\n===== STUDENT ANALYTICS TOOLKIT =====")
    print("1. Generate sample data file")
    print("2. Load & clean records from file")
    print("3. View all students")
    print("4. Analyse (averages, pass/fail, top student)")
    print("5. Filter students (generator)")
    print("6. Grade with a custom pass mark (closure)")
    print("7. Environment & date report")
    print("8. Export results to a file")
    print("9. Exit")

def main():
    # Store the Student objects loaded from the data file
    students = []

    # Keep the program running until the user chooses to exit
    while True:
        display_menu()

        # Get the user's menu choice
        choice = input("Choose an option (1-9): ")

        if choice == "1":
            # Generate a new messy student data file
            generate_data_file()
            print("Sample data file generated.")
            log_event("Sample data file generated.")

        elif choice == "2":
            # Load and clean the records from the data file
            records = load_students()

            # Turn each cleaned record into a Student object
            students = []

            for index, record in enumerate(records, start=1):
                name, score = record
                student = Student(name, f"S{index}", score)
                students.append(student)

            print(f"{len(students)} student records loaded and cleaned.")
            log_event("Student records loaded and cleaned.")

        elif choice == "3":
            # Display all loaded students
            if not students:
                print("No students loaded. Please choose option 2 first.")
            else:
                for student in students:
                    print(student)

        elif choice == "4":
            # Display class statistics and the top student
            if not students:
                print("No students loaded. Please choose option 2 first.")
            else:
                average = class_average(students)
                top_student = highest(students)
                lowest_student = lowest(students)
                rate = pass_rate(students)

                print(f"Class Average: {average:.2f}")
                print(f"Highest: {top_student}")
                print(f"Lowest: {lowest_student}")
                print(f"Pass Rate: {rate:.2f}%")

                first_pass = first_passing_student(students)

                if first_pass:
                    print(f"First Passing Student: {first_pass}")
                else:
                    print("First Passing Student: None")

        elif choice == "5":
            # Use the generator to display passing students one at a time
            if not students:
                print("No students loaded. Please choose option 2 first.")
            else:
                passing = passing_students(students)

                print("Passing Students:")

                found_passing = False

                for student in passing:
                    print(student)
                    found_passing = True

                if not found_passing:
                    print("No students have passed.")

        elif choice == "6":
            # Ask the user for a custom pass mark
            try:
                pass_mark = int(input("Enter a custom pass mark: "))

                # Create a grader that remembers the chosen pass mark
                grader = make_grader(pass_mark)

                if not students:
                    print("No students loaded. Please choose option 2 first.")
                else:
                    print(f"Results using pass mark {pass_mark}:")

                    for student in students:
                        result = grader(student.score)
                        print(f"{student.name}: {result}")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

        elif choice == "7":
            # Display environment and date information
            print("\n===== ENVIRONMENT REPORT =====")
            print(environment_report())

            print("\n===== DATE REPORT =====")
            print(date_report())

        elif choice == "8":
            # Create a text report and export it to a file
            if not students:
                print("No students loaded. Please choose option 2 first.")
            else:
                report = (
                    "===== STUDENT ANALYTICS REPORT =====\n"
                    f"Number of Students: {len(students)}\n"
                    f"Class Average: {class_average(students):.2f}\n"
                    f"Highest: {highest(students)}\n"
                    f"Lowest: {lowest(students)}\n"
                    f"Pass Rate: {pass_rate(students):.2f}%\n"
                )

                export_report(report)
                log_event("Analytics report exported.")
                print("Report exported to data/report.txt.")

        elif choice == "9":
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle an invalid menu option
            print("Invalid option. Please choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
