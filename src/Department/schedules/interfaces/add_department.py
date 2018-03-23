# -*- coding: utf-8 -*-
"""Module for Zope Schema models used for Department.schedules"""

from Department.schedules import _
from zope import schema
from plone.autoform import model
from Department.schedules.resources.vocabulary import GET_SCHOOLS


class IAddDepartment(model.Schema):
    """Schema for main course datagrid."""

    title = schema.TextLine(
        title=(u'Department Name'),
        description=(u"Do not add the word 'Department'"),
        required=True
    )

    school = schema.Choice(
        title=(u'Course Number'),
        required=True,
        source=GET_SCHOOLS
    )
