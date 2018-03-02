# -*- coding: utf-8 -*-
"""Initial lists used to generate vocabularies"""

from Department.courses import _
from plone import api

# Behavioral Science Full time faculty
DETAILED_FACULTY = [
    {
        'department': u"Behavioral Sciences",
        'name': u"Robert Duncan",
        'employment_status': u"Full-Time",
        'rank': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
    }
]
# need to decide if we should filter the different dictionary keys
FACULTY = [item[''] for item in DETAILED_FACULTY if item['']]