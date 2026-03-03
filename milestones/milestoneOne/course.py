#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student.py
-------------

Description: Contains the student class for the milestone One project

Author: Jerod Abraham
Contributors: Lorenzo .S
Date Created: 03-03-2026
Status: Development (alpha)


TO DO:
    * Add __str__ method
    * Make Course.get_student_count() more efficient?
"""

# ===== Imports =====

# Standard library


# Third-party


# Local application (your project modules)
from student import Student


# ===== Classes =====

class Course:
    """
    Docstring for Course class

    Description:

    Author: Jerod Abraham
    Contributor(s): Lorenzo .S
    """
    
    def __init__(self, course_code: str, course_credits: int, students: list = None):
        """
        Docstring for __init__
        
        Description:

        Author: Jerod Abraham
        Contributor(s): Lorenzo .S
        """
        if students is None:
            students = []
        self.course_code = course_code
        self.credits = course_credits
        self.students = students



    def add_student(self, student: Student):
        """
        Docstring for Course.add_student()
        
        Description: TBD

        Author: Jerod Abraham
        Contributor(s): Lorenzo .S
        """
        
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError(f"Student {student} already enrolled in course {self.course_code}")
        
    def get_student_count(self):
        """
        Docstring for Course.get_student_count()

        Description:

        Author: Jerod Abraha
        """
        return len(self.students)
        
