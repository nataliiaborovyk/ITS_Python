class Student:
    studentNames = []
    studentGrades = []
    diz = {}
    def __init__(self, studentName, grade):
        self.name = studentName
        self.studentGrades.append(grade)
        self.studentNames.append(studentName)
        self.diz[studentName] = grade # NON PRENDE IL NUOVO VOTO MA VECCHIO

    def changeGrade(self, newGrade):
        self.grade = newGrade
        print(*self.studentNames, self.grade)

    def getGroupAverage(cls):
        lista_grade = cls.studentGrades
        lista_names = cls.studentNames
        dizionario = cls.diz
        avg = sum(cls.studentGrades) / len(cls.studentGrades)
        print(f"media: {avg}")
        print(lista_grade)
        print(lista_names)
        print(dizionario)
        return avg, dizionario, lista_grade, lista_names
    
anna = Student("Anna", 8)
anna.changeGrade(9)  # nuovo voto

maria = Student("Maria", 10)
francesca = Student("Francesca", 9)


anna.getGroupAverage()
