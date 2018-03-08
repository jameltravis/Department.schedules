# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies"""

from Department.courses import _

# Behavioral Science Full time faculty
DETAILED_FACULTY = [
    {
        'department': u"Behavioral_Sciences",
        'facultyName': u"Robert Duncan",
        'titleRank': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
    }
]
# need to decide if we should filter the different dictionary keys
FACULTY = [item['facultyName'] for item in DETAILED_FACULTY]

# Basic idea is this - 'department': ["subject1", "subject2", "subject3"]
DEPARTMENT_SUBJECTS = [
    {
        'Behavioral_Sciences': [],
        'Biology': [],
        'chemistry':[],
        'physics': [],
        'English': [],
        'history': [],
        'math': [],
        'fine_arts': [],
        'world_languages': [],
        'accounting_finance': [],
        'business_economics': [],
        'physical_education': [],
        'health_professions': [],
        'nursing': [],
        'occupational_therapy': [],
        'social_work': [],
        'teacher_education': [],
    }
]