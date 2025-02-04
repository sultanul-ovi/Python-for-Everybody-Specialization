def compute_grade(score):
    
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


try:
    score = float(input("betwn 0.0 and 1.0: "))
    if 0.0 <= score <= 1.0:
        grade = compute_grade(score)
        print(grade)
    else:
        print("Error: Score out of range")
except ValueError:
    print("Error: Invalid input")
