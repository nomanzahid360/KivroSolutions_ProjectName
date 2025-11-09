# Function to calculate total marks
def calculate_total_marks(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average(total, num_subjects):
    return total / num_subjects

# Function to calculate grade based on average
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Main program
def main():
    print("===== Simple Student Grade Calculator =====")

    # Input student details
    name = input("Enter Student Name: ").title()
    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter marks for Subject {i}: "))
        if mark < 0 or mark > 100:
            print("Please enter a valid mark between 0 and 100.")
            return
        marks.append(mark)

    # Calculations
    total = calculate_total_marks(marks)
    average = calculate_average(total, len(marks))
    grade = calculate_grade(average)

    # Display results
    print("\n===== Student Result =====")
    print(f"Student Name : {name}")
    print(f"Marks        : {marks[0]} | {marks[1]} | {marks[2]}")
    print(f"Total Marks  : {total}")
    print(f"Average Marks: {average}")
    print(f"Grade        : {grade}")
    print("==========================")

# Run the program

main()
