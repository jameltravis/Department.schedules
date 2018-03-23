# -*- coding: utf-8 -*-
"""Module for Zope Schema models used for Department.schedules"""

from Department.schedules import _
from zope import schema
from plone.supermodel import model
from Department.schedules.resources.vocabulary import CourseSubjectVocab


class IAddCourse(model.Schema):
    """Schema for main course datagrid."""

    title = schema.TextLine(
        title=(u'Department Name and Semester'),
        description=(u'Ex: English Fall 2010'),
        required=True
    )

    subject = schema.Choice(
        title=(u'Course Subject'),
        required=True
        source=CourseSubjectVocab,
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=True,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        required=False,
    )
