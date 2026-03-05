#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data_handler.py
-------------

Description: Handles uploaded data, and data query's

Author: Lorenzo .S
Contributors:
Date Created: 03-04-2026
Status: Development (alpha)

"""


# ===== Imports =====

# Standard library
import csv

# Third-party


# Local application (your project modules)


# ===== Classes =====

class DataHandler():
    """
    Docstring for Course class
        - Description: The data_handler class for milestone one, handles loading data, and data query's for milestoneOne project
        - Author: Lorenzo .S
    """

    def __init__(self, university_data_path, course_catalog_path) -> None:
        """
        Docstring for __init__
            - Description: TBD
            - Author: Lorenzo .S

        """
        self.university_data_path = university_data_path
        self.course_catalog_path = course_catalog_path

