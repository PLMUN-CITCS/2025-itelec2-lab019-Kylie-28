def get_student_score():
    """
    Prompt the user to enter the student's score.

    Returns:
        float: The numerical score between 0 and 100.
    """
    while True:
        try:
            score = float(input("Enter the student's score: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def calculate_grade(score):
    """
    Determine the letter grade based on the given score.

    Args:
        score (float): The numerical score.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'


def main():
    """
    Main program flow to get the score, calculate the grade, and display the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")


if __name__ == "__main__":
    main()
