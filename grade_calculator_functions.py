def get_student_score():
    while True:
        try:
            score = float(input("Enter your score (0 to 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):
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
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your grade is: {grade}")

if __name__ == "__main__":
    main()
