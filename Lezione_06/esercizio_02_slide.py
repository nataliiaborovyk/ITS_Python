'''
Exercise 2 (Folder 9 ex_2.py)
1. Write a class called Student with the attributes name (str) and studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a Student. 
Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.
'''
print("\n   Esercizio 2 da slide")

        # 1. Write a class called Student with the attributes name (str) and studyProgram (str)
class Student:

    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"{self.name} - study program: {self.studyProgram}, age: {self.age}, gender: {self.gender}") 

        # 2. Create three instances. One for yourself, one for your left neighbour and one for our right neighbour.
nat = Student("Nataliia", "Data Analyst", 40, "femmina")
lor = Student("Lorenzo","Claud developer", 27, "maschio")        
ele = Student("Eleonora", "Data analyst", 46, "femmina")

        # 3. Add a method printInfo that prints the name and studyProgram of a Student. 
        # Test your method on the objects!
nat.print_info()
lor.print_info()
ele.print_info()