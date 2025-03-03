def get_student_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Replace the input() with a predefined value for testing
score = 85  # Example score for testing
if 0 <= score <= 100:
    print(f"Your grade is: {get_student_score(score)}")
else:
    print("Please enter a valid score between 0 and 100.")
