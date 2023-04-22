# Define the grade scale
grade_scale = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

# Define a function to calculate the letter grade based on the numeric score
def calculate_grade(score):
    for grade, cutoff in grade_scale.items():
        if score >= cutoff:
            return grade
    return "F"

# Define a function to calculate the subject grade
def calculate_subject_grade(subject_marks):
    total_marks = subject_marks
    percentage = round(total_marks / 100 * 100, 2)
    grade = calculate_grade(percentage)
    return {
        "total_marks": 100,
        "marks_obtained": total_marks,
        "percentage": percentage,
        "grade": grade
    }

# Define a list of subjects
subjects = ["Computer", "Mathematics", "Physics", "Chemistry"]

# Define a list to store student information
students = []

# Ask the user to enter marks for each student and subject
while True:
    student_marks = []
    for subject in subjects:
        valid_marks = False
        while not valid_marks:
            marks = int(input(f"Enter marks for {subject}: "))
            if marks <= 100:
                valid_marks = True
            else:
                print("Invalid input. Marks obtained cannot be greater than total marks.")
        student_marks.append(marks)
    student_info = {"subjects": student_marks}
    students.append(student_info)
    another_student = input("Do you want to enter marks for another student? (y/n) ")
    if another_student.lower() != "y":
        break

# Loop through the list of students and calculate their grades
for i, student in enumerate(students):
    total_marks_obtained = sum(student["subjects"])
    total_marks_possible = len(student["subjects"]) * 100
    print(f"Student {i+1}:")
    for j, subject in enumerate(student["subjects"]):
        subject_grade = calculate_subject_grade(subject)
        print(f"{subjects[j]} ({subject_grade['total_marks']} marks): {subject_grade['marks_obtained']} / {subject_grade['total_marks']} = {subject_grade['percentage']}% ({subject_grade['grade']})")
    overall_percentage = round(total_marks_obtained / total_marks_possible * 100, 2)
    overall_grade = calculate_grade(overall_percentage)
    print(f"Overall Percentage: {overall_percentage}%")
    print(f"Overall Grade: {overall_grade}")
    if overall_grade in ["A", "B"]:
        print("Remarks: Excellent performance!")
    elif overall_grade in ["C", "D"]:
        print("Remarks: Good performance.")
    else:
        print("Remarks: Needs improvement.")
    print()