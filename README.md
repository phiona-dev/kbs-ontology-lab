# University Course Ontology

## Description
This project implements a simple semantic ontology for a university academic ecosystem using Python. It structures core university entities as domain concepts, defines relational properties between them, and implements an interactive reasoning engine to query facts, track enrollments, and evaluate academic prerequisite rules dynamically.

## Ontology Structure

### Concepts (Classes)
* **Students**: Represents university learners, tracking their ID, name, programme, year of study, age, and academic history (`completed_courses`).
* **Lecturers**: Faculty members identified by an ID, name, and their parent academic department.
* **Courses**: Academic modules defined by a unique course code, descriptive name, and credit weights (defaults to 3).
* **Departments**: Structural divisions of the university overseen by an optional Department Head.
* **Classrooms**: Physical spaces designated by room numbers along with seating capacities (defaults to 30).

### Relationships (Object Properties)
The system models and enforces the following structural interactions using Python data structures:
1.  **Student** ── *enrolled in* (`enrollments`) ──> **Course**
2.  **Lecturer** ── *teaches* (`course_lecturers`) ──> **Course**
3.  **Course** ── *belongs to* (`department_courses`) ──> **Department**
4.  **Course** ── *has prerequisite* (`course_prerequisites`) ──> **Course**
5.  **Course** ── *is taught in* (`course_locations`) ──> **Classroom**

---

## Features & Reasoning Engine
Beyond data storage, the application contains analytical functions that evaluate relationships to provide intelligence:
* **Enrollment Lookup (`get_student_courses`)**: Instantly resolves all courses tied to a specific student profile.
* **Staffing Matrix (`get_course_lecturer`)**: Maps any given course to its assigned primary instructor.
* **Departmental Cataloging (`get_department_courses`)**: Filters and lists all courses managed under specific academic branches.
* **Class Roster Synthesis (`get_students_in_course`)**: Aggregates all concurrent student profiles enrolled within a shared module.
* **Prerequisite Dependency Reasoning (`can_take_course`)**: Dynamically reviews a student's `completed_courses` registry against a target course's prerequisite schema (supporting single, multiple, or nested dependencies) to authorize or block registration requests with detailed reasoning.

---

## Getting Started

### Prerequisites
* Python 3.x installed on your local environment.

### Installation & Execution
1. Clone the repo
```bash
git clone https://github.com/phiona-dev/kbs-ontology-lab
2. Open your terminal or command prompt.
3. Navigate to the project directory 
4. run the interactive script using:

````bash
python ontology_lab.py
```

## Author
Phiona