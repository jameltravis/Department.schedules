# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies"""

from Department.schedules import _

# Faculty Vocabulary
DETAILED_FACULTY = [
    {
        'department': u"behavior",
        'facultyName': u"Robert Duncan",
        'titleRank': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
    }
]
FACULTY = [item['facultyName'] for item in DETAILED_FACULTY]


# Department Course Subjects
# for list of departments: DEPARTMENT_SUBJECTS[0].keys()
# Check to see if you can make a vocubulary out of the list below
# and their proper names. In other words, the programmatic names and
# u'labels'.
DEPARTMENT_SUBJECTS = [
    {
        'behavior': [u"POL", u"PSY", u"SOC"],
        'biology': [u"BIO", u"BTEC"],
        'chemistry':[u"CHEM", u"PHS"],
        'physics': [u"PHY", u"EHS", u"GEOL"],
        'English': [u"ENG", u"WRIT", u"JOUR"],
        'history': [u"ANTH", u"BLST", u"HIST", u"CLDV", u"PHIL"],
        'math': [u"MATH", "CS"],
        'fine_arts': [u"AC", u"FA", u"CT", u"SPCH", u"MUS", u"TA"],
        'world_languages': [
            u"FREN",
            u"SPAN",
            u"HUM",
            u"CRE",
            u"ESL",
            u"FA",
            u"TA",
            u"ITAL",
            u"PRST",
            u"AAS",
            u"WLIT"
            ],
        'accounting_finance': [u"ACC", u"FINC"],
        'business_economics': [u"ECON", u"BUS", u"MKT"],
        'physical_education': [u"GERO", u"HE", u"PH", u"PH"],
        'health_professions': [u"HPGC", u"CLS", u"HS", u"HPPA"],
        'nursing': [u"NURS"],
        'occupational_therapy': [u"OT"],
        'social_work': [u"SCWK"],
        'teacher_ed': [u"EDUC"],
    }
]

DEPARTMENTS = [
    {
        u"Behavioral Sciences",
        u"Biology",
        u"Chemistry",
        u"Earth and Physical Sciences",
        u"English",
        u"History, Philosophy, and Anthropology",
        u"Mathematics and Computer Science",
        u"Performing and Fine Arts",
        u"World Languages, Literature, and Humanities",
        u"Accounting and Finance",
        u"Business and Economics",
        u"Health and Physical Education",
        u"Health Professions",
        u"Nursing",
        u"Occupational Therapy",
        u"Social Work",
        u"Teacher Education",
    }
]

SCHOOLS = [
    u'Arts and Sciences',
    u'Business and Information Systems',
    u'Health Sciences and Professional Programs'
]

WEEK_DAYS = [u'Mon', u'Tues', u'Wed', u'Thurs', u'Fri']

WEEKEND = [u'Sat', u'Sun']

# DAYTIME_HOURS = [u'7', u'8', u'9', u'10', u'11', u'12', u'1', u'2', u'3', u'4', u'6'] 

HOURS = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'11', u'12']

MINUTES = [u'00', u'10', u'20', u'30', u'40', u'50']

COURSE_ATTRIBUTES = [
    u'Add Smart Room',
    u'Hybrid',
    u'Fully Online',
]

COURSE_COMPONENTS = [
    u'None'
    u'Clinical',
    u'Experimental',
    u'Field Studies',
    u'Independent Study',
    u'Internship',
    u'Lab',
    u'Lecture',
    u'Recitation',
    u'Seminar',
    u'Writing Intensive'
]

TIME_OF_DAY = [u'AM', u'PM']

SEMESTER = [u'Winter', u'Spring', u'Summer', u'Fall']
