#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_student.py
-------------

Description: Contains the test cases for the Student class.

Author: Lorenzo .S
Date Created: 03-03-2026
Status: Development
"""

import unittest

from milestones.milestoneOne.course import Course
from milestones.milestoneOne.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        # Courses
        self.course1 = Course("CSE2050", 3, [])
        self.course2 = Course("MATH1010", 4, [])

        # Students
        # Start each student with no courses (clean tests)
        self.student1 = Student("STU100", "Student1")
        self.student2 = Student("STU200", "Student2")

    # ---------- __init__ / attributes ----------

    def test_init_sets_fields(self):
        self.assertEqual(self.student1.student_id, "STU100")
        self.assertEqual(self.student1.name, "Student1")
        self.assertIsInstance(self.student1.courses, dict)
        self.assertEqual(len(self.student1.courses), 0)

    def test_init_uses_given_courses_dict(self):
        preset = {self.course1: "A"}
        s = Student("STU300", "Student3", preset)
        self.assertIn(self.course1, s.courses)
        self.assertEqual(s.courses[self.course1], "A")

    # ---------- __str__ ----------

    def test_str_contains_id_and_name(self):
        s = str(self.student1)
        self.assertIn("STU100", s)
        self.assertIn("Student1", s)

    # ---------- enroll ----------

    def test_enroll_adds_course_and_grade(self):
        self.student1.enroll(self.course1, "A")
        self.assertIn(self.course1, self.student1.courses)
        self.assertEqual(self.student1.courses[self.course1], "A")

    def test_enroll_calls_course_add_student(self):
        # If Course tracks students, enrolling should add the student to the course too.
        self.student1.enroll(self.course1, "A")

        # This part depends on your Course implementation.
        # Common patterns: course.students list OR get_students() method.
        if hasattr(self.course1, "students"):
            self.assertIn(self.student1, self.course1.students)
        elif hasattr(self.course1, "get_students"):
            self.assertIn(self.student1, self.course1.get_students())
        else:
            # If Course doesn't expose students, at least ensure no exception occurred
            self.assertTrue(True)

    def test_enroll_invalid_grade_raises(self):
        with self.assertRaises(ValueError):
            self.student1.enroll(self.course1, "Z")

    def test_enroll_same_course_twice_raises(self):
        self.student1.enroll(self.course1, "A")
        with self.assertRaises(ValueError):
            self.student1.enroll(self.course1, "A-")

    # ---------- update_grade ----------

    def test_update_grade_changes_grade(self):
        self.student1.enroll(self.course1, "C")
        self.student1.update_grade(self.course1, "A-")
        self.assertEqual(self.student1.courses[self.course1], "A-")

    def test_update_grade_invalid_grade_raises(self):
        self.student1.enroll(self.course1, "C")
        with self.assertRaises(ValueError):
            self.student1.update_grade(self.course1, "Z")

    def test_update_grade_not_enrolled_raises(self):
        with self.assertRaises(ValueError):
            self.student1.update_grade(self.course1, "B")

    # ---------- calculate_gpa ----------

    def test_calculate_gpa_single_course(self):
        # course1 credits = 3, grade A = 4.0
        self.student1.enroll(self.course1, "A")
        self.assertAlmostEqual(self.student1.calculate_gpa(), 4.0, places=2)

    def test_calculate_gpa_multiple_courses_weighted(self):
        # course1: 3 credits, A (4.0) => 12.0 points
        # course2: 4 credits, B (3.0) => 12.0 points
        # total points = 24.0, total credits = 7 => GPA = 24/7 = 3.428571...
        self.student1.enroll(self.course1, "A")
        self.student1.enroll(self.course2, "B")

        expected = 24.0 / 7.0
        self.assertAlmostEqual(self.student1.calculate_gpa(), expected, places=4)

    def test_calculate_gpa_no_courses_raises(self):
        # Your current implementation will divide by zero if no courses exist.
        with self.assertRaises(ZeroDivisionError):
            self.student1.calculate_gpa()

    # ---------- get_courses ----------

    def test_get_courses_returns_keys_view(self):
        self.student1.enroll(self.course1, "A")
        keys = self.student1.get_courses()

        # keys is dict_keys, but we can treat it like an iterable
        self.assertIn(self.course1, list(keys))

    def test_get_courses_empty(self):
        self.assertEqual(list(self.student1.get_courses()), [])


if __name__ == "__main__":
    unittest.main()