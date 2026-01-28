class Student:
    
    teacher="linda"

    def __init__(self,name,id):
        """Define Instance Varibles"""
        self.student_name = name
        self.id = id
        self.course = ""
        self.grade = 0

    def add_course(self,new_course):
            """adding new course"""
            self.course = new_course

    def add_grade(self,student_grade):
            """adding grades"""
            self.grade = student_grade
        
    def __str__(self):
            """prints the object as a string"""
            return f"The student's name is {self.student_name}, id {self.id}, course {self.course}, grade {self.grade}"

    def __gt__(self,other):
          """Compare two student objects"""
          return self.grade > other.grade

student1 = Student("Lorenzo", 9999)
print(student1.student_name, student1.teacher)

student2 = Student("Serrano", 8888)
print(student2.student_name, student2.teacher)

student1.add_course = "CSE2050"
student1.add_grade = 100
print(student1)

student2.add_course("CSE2102")
student2.add_grade(60)
print(student1 > student2)


