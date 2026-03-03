"""

studemt.py
-------------

Contains the student class for the milestone One project

Author: Lorenzo Julian Serrano
Contributors:
Date Created: 03-03-2026
Status: Development (alpha)


TO DO:
    * Add Unenroll method
"""


class Student:
    """
    Docstring for Student class

    Description: TBD
        
    """
    def __init__(self, student_id: str, name: str, courses: dict = {}):
        """
        TBD
        """
        self.student_id = student_id
        self.name = name
        self.courses = courses
    

    def enroll(self, course: object, grade:str):
        """
        Docstring for Student.enroll() method

        Description: Adds a course_object:"grade" key value pair to self.courses dictionary if the key does not exist in self.courses
        """
        
        if self.courses[course] not in self.courses: 
            self.courses[course] = grade
        else:
            raise ValueError(f"Student is already enrolled in '{course}'.")
        
        return


    def update_grade(self, course: object, grade: str):
        """
        Docstring for Student.update_grade() method

        Description: Updates a selected course_object:"grade" key value pair in the self.courses dictionary if the key exists in self.courses
        """

        if self.courses[course] in self.courses:
            self.courses[course] = grade
        else:
            raise ValueError(f"Student is not enrolled in '{course}'.")
        
        return

    def calculate_gpa(self):
        pass

    def get_courses(self):
        pass

    def get_course_info(self):
        pass