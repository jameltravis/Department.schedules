# -*- coding: utf-8 -*-
"""Module for creating adding new faculty to the DB/portal"""

from zope import schema
from plone.supermodel import model
from Department.schedules import _
from Department.schedules.resources.vocabulary import get_vocabulary


# Need a list of release time variables

class IAddFaculty(model.Schema):
    """Adds new faculty to the portal.
    """

    title = schema.TextLine(
        title=(u"New Faculty Member's First and Last Name"),
        required=True
    )

    department =  schema.Choice(
        title=(u'Department'),
        required=True,
        source=get_departments,
    )

    emplID = schema.TextLine(
        title=(u'CUNYFirst Empl ID'),
        required=False,
    )

    titleRank = schema.Choice(
        title=(u'Please select your title'),
        required=True,
        source=get_vocabulary('AddFaculty', ),
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
        title=(u'Select your Academic School'),
        required=True,
        source=get_vocabulary(),
    )

    teachingHours = schema.Int(
        title=(u'Annual teaching hours'),
        required=False,
        min=0,
        max=30
    )
