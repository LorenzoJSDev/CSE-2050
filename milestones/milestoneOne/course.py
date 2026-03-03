#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
student.py
-------------

Descrition: Contains the student class for the milestone One project

Author: Jerod Abraham
Contributors: Lorenzo .S
Date Created: 03-03-2026
Status: Development (alpha)


TO DO:
    * Add __str__ method
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
    
    def __init__(self, course_code: str, credits: int, students: list = []):
        """
        Docstring for __init__
        
        Description:

        Author: Jerod Abraham
        Contributor(s): Lorenzo .S
        """
        self.course_code = course_code
        self.credits = credits
        self.students = []



    def add_student(self, student: Student):
        """
        Docstring for add_student
        
        Description:

        Author: Jerod Abraham
        Contributor(s): Lorenzo .S
        """
        
        if student not in self.students:
            self.students.append(student)
            
            student.enroll()
        
    def get_student_count(self):
        """
        Docstring for get_student_count
        
        :param self: Description
        """
        return len(self.students)
        
