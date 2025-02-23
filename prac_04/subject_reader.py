"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """read data from file"""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert the number of students to an integer
            data.append(parts)  # Add the processed line to the data list
    return data

def display_subject_details(data):
    """display subject details"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]:3} students")


main()