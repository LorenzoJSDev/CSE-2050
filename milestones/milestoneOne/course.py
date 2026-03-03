class Course:
    """
    Class made by Jerod Abraham
    """
    def __init__(self, course_code, credits):
        """
        Docstring for __init__
        
        :param self: Description
        :param course_code: Description
        :param credits: Description
        """
        self.course_code = course_code
        self.credits = credits
        self.students = []

    def add_student(self, student):
        """
        Docstring for add_student
        
        :param self: Description
        :param student: Description
        """
        if student not in self.students:
            self.students.append(student)
        
    def get_student_count(self):
        """
        Docstring for get_student_count
        
        :param self: Description
        """
        return len(self.students)
        
