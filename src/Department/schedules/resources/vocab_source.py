# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies"""

from Department.courses import _

# Behavioral Science Full time faculty
DETAILED_FACULTY = [
    {
        'department': u"Behavioral Sciences",
        'facultyName': u"Robert Duncan",
        'titleRank': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
    }
]
# need to decide if we should filter the different dictionary keys
FACULTY = [item['facultyName'] for item in DETAILED_FACULTY]

