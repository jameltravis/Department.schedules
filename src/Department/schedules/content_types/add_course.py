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

    subject = schema.Choice(
        title=(u'Course Subject'),
        values=[],
    )

    courseNumber = schema.Choice(
        title=(u'Course Number'),
        values=[],
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        values=[],
    )

    # Maybe this should be ommitted?
    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        max=200,
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        max=200,
    )

    component = schema.Choice(
        title=(u'Course Component'),
        values=[],
    )

    directives.widget(classDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        values=[],
    )

    directives.widget(courseTimes=checkboxes)
    courseTimes = schema.List(
        title=(u'Times'),
    )

    directives.widget(classDays=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        values=[],
    )