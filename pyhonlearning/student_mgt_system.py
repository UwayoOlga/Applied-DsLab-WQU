# Function to input student information
def input_student_info():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    
    # Decide number of courses
    num_courses = int(input("Enter number of courses (2 or 3): "))
    grades = []
    for i in range(num_courses):
        grade = float(input(f"Enter grade for course {i+1}: "))
        grades.append(grade)
        
    student = {
        'name': name,
        'age': age,
        'grades': grades
    }
    return student

# Function to calculate average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Function to display student info
def display_student_info(student, average):
    print("\n--- Student Information ---")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print(f"Average Grade: {average:.2f}")

# Main program
def main():
    student = input_student_info()
    avg = calculate_average(student['grades'])
    display_student_info(student, avg)

# Run the program
main()
