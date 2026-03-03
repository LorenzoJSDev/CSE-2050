class University:
    """
    Docstring for University

    Collaboration between Jerod Abraham and Lorenzo Serrano
    """
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_course(self, course_code, credits):
        if course_code not in self.courses:
            course = Course(course_code, credits)
            self.courses[course_code] = course
        return self.courses[course_code]
    
    def add_student(self, student_id, name):
        """
        """
        pass

    def get_student(self, student_id):
        """
        """
        pass

    def get_course(self, course_code):
        return self.courses.gen(course_code)

    def get_course_enrollment(self, course_code):
        course = self.get_course(course_code)
        if course:
            return course.get_student_count()
        return 0

    def students_in_class(self, course_code):
        course = self.get_course(course_code)
        if course:
            return course.get_students()
        return []