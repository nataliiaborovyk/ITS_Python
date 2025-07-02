'''
University Management System
Create a system to manage a university with departments, courses, professors, and students.  
1. Create an abstract class Person:
Attributes:
    name
    age
Methods:
    get_role, an abstract method to be implemented by subclasses.
    __str__, method to return a string representation of the person.
2. Create subclasses Student and Professor that inherit from Person and implement the abstract method.
Class Student:
Additional attributes:
        student_id,
        courses (list of Course instances).
Additional method:
        enroll, to enroll the student in a course.
Class Professor:
Additional attributes:
        professor_id,
        department (a Department instance), 
        courses (list of Course instances)
Additional method:
        assign_to_course, to assign the professor to a course.
3. Create a class Course:
Attributes:
    course_name
    course_code
    students (list of Student instances)
    professor (Professor instance)
Methods:
    add_student, to add a student to the course.
    set_professor, to set the professor for the course.
    __str__, method to return a string representation of the course.
4. Create a class Department:
Attributes:
    department_name
    courses (list of Course instances)
    professors (list of Professor instances)
Methods:
    add_course, to add a course to the department.
    add_professor, to add a professor to the department.
    __str__, method to return a string representation of the department.
5. Create a class University:
Attributes:
    name
    departments (list of Department instances)
    students (list of Student instances)
Methods:
    add_department, to add a department to the university.
    add_student, to add a student to the university.
    __str__, method to return a string representation of the university.
Finally, write a simple driver program. After creating a University, you should begin by creating instances of the main components that make up a university:
    Departments (e.g., Computer Science, Literature)
    Courses (e.g., Data Structures, Medieval Literature)
    Professors (e.g., faculty members who will teach the courses)
    Students (e.g., individuals who will enroll in the courses)
Once these instances are created, follow these steps:
    Add all entities to the university: Ensure the university class can register departments and students. 
    Enroll students in courses: Simulate student registration by assigning students to one or more courses. 
    Assign professors to courses: Each course should have a professor responsible for teaching it. 
    Display the state of the university: at each significant step, print out a summary of the university’s current state. This might include:
        A list of courses with assigned professors.
        Which students are enrolled in which courses.
        A breakdown of departments and the courses they offer.
'''