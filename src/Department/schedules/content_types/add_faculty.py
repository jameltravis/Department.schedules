# -*- coding: utf-8 -*-
"""Module for creating adding new faculty to the DB/portal"""

from zope import schema
from plone.supermodel import model
from Department.courses import _

DETAILED_FACULTY = [
    {
        'department': u"Behavioral Sciences",
        'facultyName': u"Robert Duncan",
        'title': u"Associate Professor",
        'tenure': u"Yes",
        'school': u"Arts and Sciences",
    }
]


class IAddFaculty(model.Schema):
    """Adds new faculty to the portal.
    """

    department =  schema.Choice(
        title=(u'Department'),
        required=True,
    )
