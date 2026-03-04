#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_university.py
-------------

Description: Contains the test cases for the University class.

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development
"""

# ===== Imports =====

# Standard library
import unittest

# Local application
from milestones.milestoneOne.university import University
from milestones.milestoneOne.course import Course
from milestones.milestoneOne.student import Student


# ==== Classes ==== #

class TestUniversity(unittest.TestCase):

    def setUp(self):
        """
        Docstring for TestUniversity.setUp()
            - Description: Runs before every test, so every test has access to premade objects.
            - Author: Lorenzo .S
        """
        #-- Test Objects --#

        #University Objects
        self.university1 = University()

        #Course Objects
        self.course1 = Course("CSE2050",2)
        self.course2 = Course("MATH1010",3)

        #Student Objects
        self.student1 = Student("STU00001","Student_1")
        self.student2 = Student("STU00002","Student_2")

        return

    # ---- Test University.__init__() ---- #


