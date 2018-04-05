# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies."""

from Department.schedules import _

# Faculty Vocabulary
DETAILED_FACULTY = [
    {
        'department': u"behavior",
        'facultyName': u"Robert Duncan",
        'titleRank': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
        'Full-Time': u"No"
    }
]



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
        'math': [u"MATH", u"CS"],
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

FACULTY = [
    {
        'behavior': [
            u"Apkarian, Jacob",
            u"Ashton, William",
            u"Austin, Susan",
            u"Berwid, Olga",
            u"Daniels, Ron",
            u"Davies, Kristin",
            u"Dietz, Joshua",
            u"Duncan, Robert",
            u"Elbulok-Charcape, Milushka",
            u"Elfers-Wygand, Patricia",
            u"Ellis, Tracey",
            u"Erlbaum, William",
            u"Giosan, Cezar",
            u"Gregory, Michele",
            u"Hamad, Mohammad",
            u"Hansen, Ian",
            u"Harper, Robin",
            u"Higgins, Kathryn",
            u"Hughes, Korey",
            u"Jenkins, Sharmayne",
            u"Levey, Tania",
            u"Majerovitz, Deborah",
            u"Mokrue, Kathariya",
            u"Ostholm, Shirley",
            u"Ranis, Peter",
            u"Sharpe, Michael",
            u"Swoboda, Debra",
            u"Villegas, Francisco",
            u"Zhang, Xiaodan"
        ],
        'biology': [
            u"Adams, Cheryl",
            u"Alter, Elizabeth",
            u"Arsov, Ivica",
            u"Beaton, Laura",
            u"Bradbury-Boyd, Louis",
            u"Casey, John",
            u"Criss, Andrew",
            u"Emtage, Lesley",
            u"Hua, Shao-Ying",
            u"Levinger, Louis",
            u"Lewis, Leslie",
            u"MacNeil, Margaret",
            u"McNeil, Gerard",
            u"Schlein, Jack",
        ],
        'chemistry':[
            u"Chakravarti, Deb",
            u"Chang, Emmanuel",
            u"Desamero, Ruel",
            u"Fay, Francois",
            u"Fearnley, Stephen",
            u"Foster, Catherine",
            u"Johnson, Lawrence",
            u"Lee, Jong-Ill",
            u"Musumeci, Daniele",
            u"Profit, Adam",
            u"Richards, Lynne",
            u"Robie, Daniel",
            u"Small, Yolanda"
        ],
        'physics': [
            u"Borenstein, Samuel",
            u"Dhar, Ratan",
            u"Khandaker, Nazrul",
            u"Lynch, Kevin",
            u"Paglione, Timothy",
            u"Popp, James",
            u"Roberts-Semple, Dawn",
            u"Schleifer, Stanley",
            u"Wolosin, Dora"
        ],
        'English': ["NAME"],
        'history': ["NAME"],
        'math': ["NAME"],
        'fine_arts': ["NAME"],
        'world_languages': ["NAME"],
        'accounting_finance': ["NAME"],
        'business_economics': ["NAME"],
        'physical_education': ["NAME"],
        'health_professions': ["NAME"],
        'nursing': ["NAME"],
        'occupational_therapy': ["NAME"],
        'social_work': ["NAME"],
        'teacher_ed': ["NAME"],
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

HOURS = [
    u'7:00am',
    u'7:30am',
    u'7:50am',
    u'8:00am',
    u'8'
]

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

SEMESTERS = [u'Winter', u'Spring', u'Summer', u'Fall']

FACULTY_RANKS = [
    u'Assistant Professor',
    u'Associate Professor',
    u'Professor'
]
