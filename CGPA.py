def cgpa_calculator():
    num_subjects = int(input("Enter the number of subjects: "))
    
    total_credits = 0
    weighted_grade_points = 0
    
    for i in range(num_subjects):
        print(f"Subject {i+1}:")
        credits = float(input("Enter the number of credits: "))
        grade_point = float(input("Enter the grade point (on a scale of 10): "))
        
        total_credits += credits
        weighted_grade_points += grade_point * credits
    
    cgpa = weighted_grade_points / total_credits
    print(f"Your CGPA is: {cgpa:.2f}")

cgpa_calculator()
