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

    # ---- Test University.__init__() ---- #
    def test_add_course(self):
        course1 = self.university1.add_course("CSE2050", 3)
        self.assertEqual(course1.course_code, "CSE 2050")
        self.assertEqual(course1.credits, 2)
        self.assertIn("CSE2050", self.university1.courses)

    def test_duplicate_course(self):
        c1 = self.university1.add_course("CSE2050",2)
        c2 = self.university1.add_course("CSE2050",2)
        self.assertIs(c1, c2)
        self.assertEqual(len(self.university1.courses), 1)

    def test_add_student(self):
        student1 = self.university1.add_student("STU00001", "Student_1")
        self.assertEqual(student1.student_id, "STU00001")
        self.assertIn("STU00001", self.university1.students)
    
    def test_duplicate_student(self):
        self.university1.add_student("STU00001","Student_1")
        with self.assertRaises(ValueError):
            self.university1.add_student("STU00001","Student_2")
    
    def test_get_student(self):
        self.university1.add_student("STU00001","Student_1")
        student = self.university1.get_student("STU00001")
        self.assertEqual(student.student_id, "STU00001")

    def test_got_imaginary_student(self):
        with self.assertRaises(ValueError):
            self.university1.get_student("STU12028")

    def test_get_course(self):
        self.university1.add_course("CSE2050", 3)
        course = self.university1.get_course("CSE2050")
        self.assertEqual(course.course_code, "CSE2050")
    
    def test_get_imaginary_course(self):
        self.assertIsNone(self.university1.get_course("CSE2500"))

    def test_get_course_enrollment(self):
        self.university1.add_course("CSE2050", 3)
        count = self.university1.get_course_enrollment("CSE2050")
        self.assertEqual(count, 0)

    def test_students_in_class(self):
        self.university1.add_course("CSE2050", 3)
        self.assertEqual(self.university1.students_in_class("CSE2050"), [])
        

if __name__ == "__main__":
    unittest.main()



