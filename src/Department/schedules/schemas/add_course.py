# -*- coding: utf-8 -*-
"""Module for Zope Schema models used for Department.schedules"""

from zope import schema
from plone import api
from plone.autoform import model, directives
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from Department.courses import _
from ..resources.vocabulary import GetFaculty


class IAddCourse(model.Schema):
    """Schema for main course datagrid."""

    title = schema.TextLine(
        title=(u'Department Name and Semester'),
        description=(u'Ex: English Fall 2010'),
        required=True
    )

    subject = schema.Choice(
        title=(u'Course Subject'),
        values=['A value'],
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=True,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        required=False,
    )
