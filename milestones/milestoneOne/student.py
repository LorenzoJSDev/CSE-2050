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
    TBD
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
        TBD
        """

        self.courses[course] = grade
        pass

    def update_grade(self, course: object, grade: str):
        
