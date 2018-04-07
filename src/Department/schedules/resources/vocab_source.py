# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies."""

from Department.schedules import _

# These are attributes needed for 
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
DEPARTMENT_SUBJECTS = (
        u"Behavioral Sciences: POL",
        u"Behavioral Sciences: PSY",
        u"Behavioral Sciences: SOC",
        u"Biology: BIO", u"Biology: BTEC",
        u"Chemistry: CHEM", u"Chemistry: PHS",
        u"Earth and Physical Sciences: PHY",
        u"Earth and Physical Sciences: EHS",
        u"Earth and Physical Sciences: GEOL",
        u"English: ENG",
        u"English: WRIT",
        u"English: JOUR",
        u"History and Philosophy: ANTH",
        u"History and Philosophy: BLST",
        u"History and Philosophy: HIST",
        u"History and Philosophy: CLDV",
        u"History and Philosophy: PHIL",
        u"Mathematics and Computer Science: MATH",
        u"Mathematics and Computer Science: CS",
        u"Performing and Fine Arts: AC",
        u"Performing and Fine Arts: FA",
        u"Performing and Fine Arts: CT",
        u"Performing and Fine Arts: SPCH",
        u"Performing and Fine Arts: MUS",
        u"Performing and Fine Arts: TA",
        u"Foreign Languages, ESL and Humanities: FREN",
        u"Foreign Languages, ESL and Humanities: SPAN",
        u"Foreign Languages, ESL and Humanities: HUM",
        u"Foreign Languages, ESL and Humanities: CRE",
        u"Foreign Languages, ESL and Humanities: ESL",
        u"Foreign Languages, ESL and Humanities: FA",
        u"Foreign Languages, ESL and Humanities: TA",
        u"Foreign Languages, ESL and Humanities: ITAL",
        u"Foreign Languages, ESL and Humanities: PRST",
        u"Foreign Languages, ESL and Humanities: AAS",
        u"Foreign Languages, ESL and Humanities: WLIT",
        u"Accounting and Finance: ACC",
        u"Accounting and Finance: FINC",
        u"Business and Economics: ECON",
        u"Business and Economics: BUS",
        u"Business and Economics: MKT",
        u"Health and Physical Education and Gerontological Studies: GERO",
        u"Health and Physical Education and Gerontological Studies: HE",
        u"Health and Physical Education and Gerontological Studies: PH",
        u"Health and Physical Education and Gerontological Studies: PH",
        u"Health Professions: HPGC",
        u"Health Professions: CLS",
        u"Health Professions: HS",
        u"Health Professions: HPPA",
        u"Nursing: NURS",
        u"Occupational Therapy: OT",
        u"Social Work: SCWK",
        u"Teacher Education: EDUC",
)

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
        u"Foreign Languages, ESL and Humanities",
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
            u"Behavioral Sciences: Apkarian, Jacob",
            u"Behavioral Sciences: Ashton, William",
            u"Behavioral Sciences: Austin, Susan",
            u"Behavioral Sciences: Berwid, Olga",
            u"Behavioral Sciences: Daniels, Ron",
            u"Behavioral Sciences: Davies, Kristin",
            u"Behavioral Sciences: Dietz, Joshua",
            u"Behavioral Sciences: Duncan, Robert",
            u"Behavioral Sciences: Elbulok-Charcape, Milushka",
            u"Behavioral Sciences: Elfers-Wygand, Patricia",
            u"Behavioral Sciences: Ellis, Tracey",
            u"Behavioral Sciences: Erlbaum, William",
            u"Behavioral Sciences: Giosan, Cezar",
            u"Behavioral Sciences: Gregory, Michele",
            u"Behavioral Sciences: Hamad, Mohammad",
            u"Behavioral Sciences: Hansen, Ian",
            u"Behavioral Sciences: Harper, Robin",
            u"Behavioral Sciences: Higgins, Kathryn",
            u"Behavioral Sciences: Hughes, Korey",
            u"Behavioral Sciences: Jenkins, Sharmayne",
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

FACULTY2 = (
        u"Behavioral Science: POL",
        u"Behavioral Science: PSY",
        u"Behavioral Science: SOC",
        u"Biology: BIO", u"Biology: BTEC",
        u"Chemistry: CHEM", u"Chemistry: PHS",
        u"Earth and Physical Sciences: PHY",
        u"Earth and Physical Sciences: EHS",
        u"Earth and Physical Sciences: GEOL",
        u"English: ENG",
        u"English: WRIT",
        u"English: JOUR",
        u"History and Philosophy: ANTH",
        u"History and Philosophy: BLST",
        u"History and Philosophy: HIST",
        u"History and Philosophy: CLDV",
        u"History and Philosophy: PHIL",
        u"Mathematics and Computer Science: MATH",
        u"Mathematics and Computer Science: CS",
        u"Performing and Fine Arts: AC",
        u"Performing and Fine Arts: FA",
        u"Performing and Fine Arts: CT",
        u"Performing and Fine Arts: SPCH",
        u"Performing and Fine Arts: MUS",
        u"Performing and Fine Arts: TA",
        u"Foreign Languages, ESL and Humanities: FREN",
        u"Foreign Languages, ESL and Humanities: SPAN",
        u"Foreign Languages, ESL and Humanities: HUM",
        u"Foreign Languages, ESL and Humanities: CRE",
        u"Foreign Languages, ESL and Humanities: ESL",
        u"Foreign Languages, ESL and Humanities: FA",
        u"Foreign Languages, ESL and Humanities: TA",
        u"Foreign Languages, ESL and Humanities: ITAL",
        u"Foreign Languages, ESL and Humanities: PRST",
        u"Foreign Languages, ESL and Humanities: AAS",
        u"Foreign Languages, ESL and Humanities: WLIT",
        u"Accounting and Finance: ACC",
        u"Accounting and Finance: FINC",
        u"Business and Economics: ECON",
        u"Business and Economics: BUS",
        u"Business and Economics: MKT",
        u"Health and Physical Education and Gerontological Studies: GERO",
        u"Health and Physical Education and Gerontological Studies: HE",
        u"Health and Physical Education and Gerontological Studies: PH",
        u"Health and Physical Education and Gerontological Studies: PH",
        u"Health Professions: HPGC",
        u"Health Professions: CLS",
        u"Health Professions: HS",
        u"Health Professions: HPPA",
        u"Nursing: NURS",
        u"Occupational Therapy: OT",
        u"Social Work: SCWK",
        u"Teacher Education: EDUC",
)


SCHOOLS = [
    u'Arts and Sciences',
    u'Business and Information Systems',
    u'Health Sciences and Professional Programs'
]
