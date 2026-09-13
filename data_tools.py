import random

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

