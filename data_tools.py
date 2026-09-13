import random
from datetime import datetime

def generate_data_file():
    # Sample names used to generate the raw student records
    names = [
        "Lisa",
        "John",
        "Sarah",
        "Michael",
        "Thabo",
        "Lerato",
        "David",
        "Aisha",
    ]

    # Create messy records with different capitalisation and spacing
    records = []

    for name in names:
        score = random.randint(0, 100)

        messy_name = random.choice([
            name.lower(),
            name.upper(),
            name.title(),
            " " + name.lower() + " ",
            " " + name.upper(),
        ])

        messy_record = random.choice([
            messy_name + "," + str(score),
            messy_name + " , " + str(score),
            messy_name + ", " + str(score),
            " " + messy_name + " , " + str(score) + " ",
        ])

        records.append(messy_record)

    # Write all generated records to the students data file
    with open("data/students.txt", "w") as file:
        for record in records:
            file.write(record + "\n")

def load_students():
    # Store the cleaned student records
    students = []

    # Open the raw student data file for reading
    with open("data/students.txt", "r") as file:
        for line in file:
            # Remove surrounding whitespace from the whole line
            line = line.strip()

            # Split the line into the student's name and score
            name, score = line.split(",")

            # Clean the name and convert the score to an integer
            name = name.strip().title()
            score = int(score.strip())

            # Add the cleaned record as a tuple
            students.append((name, score))

    return students


def export_report(text):
    # Write the report text to the report file
    with open("data/report.txt", "w") as file:
        file.write(text)

def log_event(message):
    # Create a timestamp for the activity log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the timestamp and message to the activity log
    with open("data/activity.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

