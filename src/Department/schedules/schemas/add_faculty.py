# -*- coding: utf-8 -*-
"""Module for creating adding new faculty to the DB/portal"""

from zope import schema
from plone.supermodel import model
from Department.courses import _


class IAddFaculty(model.Schema):
    """Adds new faculty to the portal.
    """

    title = schema.TextLine(
        title=(u"New Faculty Member's Name"),
        required=True
    )

    department =  schema.Choice(
        title=(u'Department'),
        required=True,
        source=[],
    )

    facultyName = schema.TextLine(
        title=(u'Faculty Name'),
        description=(u'Please add the first and last name of the faculty member'),
        required=True,
    )

    titleRank = schema.Choice(
        title=(u'Please select your title'),
        required=True,
        source=[],
    )

    tenure = schema.Choice(
        title=(u'Do you currently hold tenure?'),
        required=True,
        values=[
            u'Select One',
            u'Yes',
            u'No'
        ],
    )

    school = schema.Choice(
        title=(u'Select your Academic School?'),
        required=True,
        source=[],
    )
