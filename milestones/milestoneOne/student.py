#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student.py
-------------

Descrition: Contains the student class for the milestone One project

Author: Lorenzo Julian Serrano
Contributors:
Date Created: 03-03-2026
Status: Development (alpha)


TO DO:
    * Add Unenroll method
    * Add __str__ method

"""

# ===== Imports =====

# Standard library


# Third-party


# Local application (your project modules)
from course import Course


# ===== Classes =====
class Student:
    """
    Docstring for Student class

    Description: TBD

    Contributor(s): "Lorenzo .J Serrano"
    """
    
    GRADE_POINTS = {
    'A'  : 4.0,  'A-' : 3.7,
    'B+' : 3.3,  'B'  : 3.0,  'B-' : 2.7,
    'C+' : 2.3,  'C'  : 2.0,  'C-' : 1.7,
    'D'  : 1.0,
    'F'  : 0.0
    }


    def __init__(self, student_id: str, name: str, courses: dict = {}):
        """
        Docstring for Student.__init__() method

        Description: the constructor for Student class instances / objects

        Author: Lorenzo .S
        """
        self.student_id = student_id
        self.name = name
        self.courses = courses
    

    def enroll(self, course:Course, grade: str):
        """
        Docstring for Student.enroll() method

        Description: Adds a course_object:"grade" key value pair to self.courses dictionary if the key does not exist in self.courses

        Author: Lorenzo .S
        """
        
        if self.courses[course] not in self.courses: 
            if grade in self.GRADE_POINTS:
                self.courses[course] = grade
                course.add_student(self)
            else:
                raise ValueError(f"{grade} is not a valid grade input")
        else:
            raise ValueError(f"Student is already enrolled in '{course}'.")
        
        return


    def update_grade(self, course: Course, grade: str):
        """
        Docstring for Student.update_grade() method

        Description: Updates a selected course_object:"grade" key value pair in the self.courses dictionary if the key exists in self.courses
        
        Author: Lorenzo .S
        """

        if self.courses[course] in self.courses:
            self.courses[course] = grade
        else:
            raise ValueError(f"Student is not enrolled in '{course}'.")
        
        return

    def calculate_gpa(self):


        pass

    def get_courses(self):
        return list(self.courses.keys())
        pass

    def get_course_info(self):
        pass