# -*- coding: utf-8 -*-
"""Module for creating adding new school to the DB/portal"""

from zope import schema
from plone.supermodel import model
from Department.schedules import _

class IAddSchool(model.Schema):
    """Adds new school to school vocabulary"""

    title = schema.TextLine(
        title=(u'School name'),
        description=(
            u"Do Not Write 'School of' before school name"
        ),
        required=True
    )
