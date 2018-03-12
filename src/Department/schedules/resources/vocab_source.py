# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies"""

from Department.courses import _

# Behavioral Science Full time faculty
DETAILED_FACULTY = [
    {
        'department': u"behavior",
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
        'behavior': ["POL", "PSY", "SOC"],
        'biology': ["BIO", "BTEC"],
        'chemistry':["CHEM", "PHS"],
        'physics': ["PHY", "EHS", "GEOL"],
        'English': ["ENG", "WRIT", "JOUR"],
        'history': ["ANTH", "BLST", "HIST", "CLDV", "PHIL"],
        'math': ["MATH", "CS"],
        'fine_arts': ["AC", "FA", "CT", "SPCH", "MUS", "TA"],
        'world_languages': ["FREN", "SPAN", "HUM", "CRE", "ESL", "FA", "TA", "ITAL", "PRST", "AAS", "WLIT"],
        'accounting_finance': ["ACC", "FINC"],
        'business_economics': ["ECON", "BUS", "MKT"],
        'physical_education': ["GERO", "HE", "PH", "PH"],
        'health_professions': ["HPGC", "CLS", "HS", "HPPA"],
        'nursing': ["NURS"],
        'occupational_therapy': ["OT"],
        'social_work': ["SCWK"],
        'teacher_ed': ["EDUC"],
    }
]
