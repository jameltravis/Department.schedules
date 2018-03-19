# -*- coding: utf-8 -*-
"""Module for creating adding new faculty to the DB/portal"""

from zope import schema
from plone.supermodel import model
from Department.schedules import _
from Department.schedules.resources.vocab_source import SCHOOLS
from Department.schedules.resources.vocabulary import (
    get_schools,
    get_departments
    )



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
        source=,
    )

    emplID = schema.TextLine(
        title=(u'CUNYFirst Empl ID'),
        required=False,
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
        title=(u'Select your Academic School'),
        required=True,
        source=get_schools,
    )
