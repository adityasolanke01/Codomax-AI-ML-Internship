# Student Grade Calculator
# Codomax Digital Solutions - AI & ML Internship, Module 02

def calculate_grade(average):
    """Return a grade based on the average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def main():
    print("=" * 42)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 42)

    student_name = input("Enter student name: ").strip() or "Student"
    subjects = ["Mathematics", "Science", "English"]
    marks = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks in {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                print("Please enter a value from 0 to 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("\n" + "-" * 42)
    print("                 RESULT")
    print("-" * 42)
    print(f"Student: {student_name}")
    for subject, score in zip(subjects, marks):
        print(f"{subject}: {score:g}/100")
    print(f"Total: {total:g}/300")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade}")
    print(f"Status: {'Pass' if grade != 'F' else 'Needs improvement'}")
    print("-" * 42)


if __name__ == "__main__":
    main()
