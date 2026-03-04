#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_university.py
-------------

Description: Contains the test cases for the University class.

Author: Lorenzo .S
Contributor(s): Jerod Abraham
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
        """
        Docstring for TestUniversity.test_add_course()
            - Description: Tests if a course can be added and stored successfully
            - Author: Jerod Abraham
        """
        course1 = self.university1.add_course("CSE2050", 3)
        self.assertEqual(course1.course_code, "CSE2050")
        self.assertEqual(course1.credits, 3)
        self.assertIn("CSE2050", self.university1.courses)

    def test_duplicate_course(self):
        """
        Docstring for TestUniversity.test_duplicate_course()
            - Description: Tests whether creating two of the same courses actually makes duplicates
            - Author: Jerod Abraham
        """
        c1 = self.university1.add_course("CSE2050",2)
        c2 = self.university1.add_course("CSE2050",2)
        self.assertIs(c1, c2)
        self.assertEqual(len(self.university1.courses), 1)

    def test_add_student(self):
        """
        Docstring for TestUniversity.test_add_student()
            - Description: Tests if a student can be added and stored successfully
            - Author: Jerod Abraham
        """
        student1 = self.university1.add_student("STU00001", "Student_1")
        self.assertEqual(student1.student_id, "STU00001")
        self.assertIn("STU00001", self.university1.students)
    
    def test_duplicate_student(self):
        """
        Docstring for TestUniversity.test_duplicate_student()
            - Description: Tests whether adding two of the same ID'ed students really raises a ValueError
            - Author: Jerod Abraham
        """
        self.university1.add_student("STU00001","Student_1")
        with self.assertRaises(ValueError):
            self.university1.add_student("STU00001","Student_2")
    
    def test_get_student(self):
        """
        Docstring for TestUniversity.test_get_student()
            - Description: Tests if we can return the correct student from the student ID
            - Author: Jerod Abraham
        """
        self.university1.add_student("STU00001","Student_1")
        student1 = self.university1.get_student("STU00001")
        self.assertEqual(student1.student_id, "STU00001")

    def test_get_imaginary_student(self):
        """
        Docstring for TestUniversity.test_get_imaginary_student()
            - Description: Tests if requesting a non-student really raises a ValueError
            - Author: Jerod Abraham
        """
        with self.assertRaises(ValueError):
            self.university1.get_student("STU12028")

    def test_get_course(self):
        """
        Docstring for TestUniversity.test_get_imaginary_student()
            - Description: Tests if we can return the correct course from the course code
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3)
        course1 = self.university1.get_course("CSE2050")
        self.assertEqual(course1.course_code, "CSE2050")
    
    def test_get_imaginary_course(self):
        """
        Docstring for TestUniversity.test_get_imaginary_course()
            - Description: Tests that requesting a non-existent course returns None.
            - Author: Jerod Abraham
        """
        self.assertIsNone(self.university1.get_course("CSE2500"))

    def test_get_course_enrollment(self):
        """
        Docstring for TestUniversity.test_get_course_enrollment()
            - Description: Tests that the enrollment count for a course with no students returns zero.
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3)
        count = self.university1.get_course_enrollment("CSE2050")
        self.assertEqual(count, 0)

    def test_students_in_class(self):
        """
        Docstring for TestUniversity.test_students_in_class()
            - Description: Tests if we get an empty list from requesting students in the class
            - Author: Jerod Abraham
        """
        self.university1.add_course("CSE2050", 3)
        self.assertEqual(self.university1.students_in_class("CSE2050"), [])
        

if __name__ == "__main__":
    unittest.main()



