class Student:
    def __init__(self, name, student_id, programme, year, age=None):
        self.name = name
        self.student_id = student_id
        self.programme = programme
        self.year = year
        self.age = age
        self.completed_courses = []
    
class Lecturer:
    def __init__(self, name, lecturer_id, department):
        self.name = name
        self.lecturer_id = lecturer_id
        self.department = department

    def __str__(self):
        return f"Lecturer(name={self.name}, lecturer_id={self.lecturer_id}, department={self.department}, courses={self.courses})"
    
    
class Course:
    def __init__(self, course_code, course_name, credits=3):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f"Course(course_code={self.course_code}, course_name={self.course_name}, credits={self.credits})"
    
class Department:
    def __init__(self, name, head=None):
        self.name = name
        self.head = head

    def __str__(self):
        return f"Department(name={self.name}, head={self.head}, courses={self.courses})"

class Classroom:
    def __init__(self, room_number, capacity=30):
        self.room_number = room_number
        self.capacity = capacity

    def __str__(self):
        return f"Classroom(room_number={self.room_number}, capacity={self.capacity})"
    
    
#Ontology Objects
dept_cs = Department(name="Computer Science", head="Dr. Otieno")
dept_is = Department(name="Information Systems", head="Dr. Mwangi")

lecturer1 = Lecturer("Dr. Otieno", "L001", "Computer Science")
lecturer2 = Lecturer("Dr. Mwangi", "L002", "Information Systems")
lecturer3 = Lecturer("Dr. Kimani", "L003", "Computer Science")

course1 = Course("APT2010", "Introduction to Programming", credits=3)
course2 = Course("APT2020", "Data Structures", credits=4)
course3 = Course("APT2030", "Database Systems", credits=3) 
course4 = Course("APT2040", "Software Engineering", credits=3) 
course5 = Course("APT4040", "Artificial Intelligence", credits=4)

student1 = Student("Alice", "S001", "Computer Science", 2, 20)
student2 = Student("Bob", "S002", "Information Systems Technology", 3, 21)
student3 = Student("Charlie", "S003", "Applied Computer Technology", 1, 19)
student4 = Student("David", "S004", "Computer Science", 4, 22)
student5 = Student("Eve", "S005", "Information Systems Technology", 2, 20)

student1.completed_courses = ["APT2010"]

room1 = Classroom("Lab 1", 30)
room2 = Classroom("Lab 2", 45)
room3 = Classroom("Auditorium A", 120)

enrollments = {
    "Alice": ["APT2010", "APT2020"],
    "Bob": ["APT2030"],
    "Charlie": ["APT2010", "APT2040"],
    "David": ["APT2020"],
    "Eve": ["APT2030"]
}

course_lecturers = {
    "APT2010": "Dr. Otieno",
    "APT2020": "Dr. Kimani",
    "APT2030": "Dr. Mwangi",
    "APT2040": "Dr. Otieno",
    "APT4040": "Dr. Kimani"
}

department_courses = {
    "Computer Science": ["APT2010", "APT2020", "APT2040", "APT4040"],
    "Information Systems": ["APT2030"]
}

course_prerequisites = {
    "APT2020": ["APT2010"],
    "APT2030": ["APT2010"],
    "APT2040": ["APT2010", "APT2020"],
    "APT4040": ["APT2020", "APT2030"]
}

course_locations = {
    "APT2010": "Lab 1", 
    "APT2020": "Lab 2",
    "APT2030": "Lab 1",
    "APT2040": "Lab 2",
    "APT4040": "Auditorium A"
}

students_db = {
    "Alice": student1,
    "Bob": student2,
    "Charlie": student3,
    "David": student4,
    "Eve": student5
}

def get_student_courses(student_name):
    """Returns a list of courses a student is enrolled in."""
    return enrollments.get(student_name, [])

def get_course_lecturer(course_code):
    """Returns the lecturer teaching a specific course."""
    return course_lecturers.get(course_code, "Unknown Lecturer")

def get_department_courses(department_name):
    """Returns a list of courses offered by a specific department."""
    return department_courses.get(department_name, [])

def get_students_in_course(course_code):
    """Returns a list of students enrolled in a specific course."""
    return [student for student, courses in enrollments.items() if course_code in courses]

def can_take_course(student_name, course_code):
    """Checks if a student can take a course based on prerequisites."""
    prerequisites = course_prerequisites.get(course_code)
    if not prerequisites:
        return "Yes."
    student_obj = students_db.get(student_name)
    if student_obj and prerequisites in student_obj.completed_courses:
        return "Yes."
    else:
        return f"No.\n Missing prerequisite: {prerequisites}."
    

if __name__ == "__main__":
    print("=== University Ontology Database ===")
    print("Available students in system: Mary, Brian, Linda, John, Alice\n")
    
    while True:
        # 1. Get student name from user
        student_name = input("Enter a student's name (or type 'exit' to quit): ").strip()
        
        # Check if the user wants to leave the program
        if student_name.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        # Check if the student actually exists in our database
        if student_name not in students_db:
            print(f"Error: Student '{student_name}' not found. Please try again.\n")
            continue
            
        print("-" * 40)
        
        # Output 1: Courses taken by the entered student
        print(f"Courses taken by {student_name}:")
        courses = get_student_courses(student_name)
        if courses:
            for course in courses:
                print(f"- {course}")
        else:
            print("- None (Not enrolled in any courses)")
        print()

        # Output 2 & 4: Find lecturer and other classmates for their first course (if they have one)
        if courses:
            primary_course = courses[0]
            print(f"Lecturer teaching {primary_course}:")
            print(f"- {get_course_lecturer(primary_course)}")
            print()

            print(f"Students taking {primary_course}:")
            for student in get_students_in_course(primary_course):
                print(f"- {student}")
            print()
        else:
            print("No course enrollment data to display for lecturer/classmate lookups.\n")

        # Output 5: Dynamic Prerequisite Check
        target_course = input(f"What course does {student_name} want to take next? (e.g., APT4040): ").strip()
        print(f"Can {student_name} take {target_course}?")
        print(can_take_course(student_name, target_course))
        
        print("-" * 40)
        print()  # Blank line for spacing before the next loop    