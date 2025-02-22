def get_student_score():
   # Handles user input to obtain the student's score.
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):
    # Determines the letter grade based on the given score and grading scale.
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Main program flow.
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")

# Run the program
if __name__ == "__main__":
    main()
