# -*- coding: utf-8 -*-
"""Module for Zope Schema models used for Department.schedules"""

from zope import schema
from plone import api
from plone.autoform import model, directives
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from Department.schedules import _
from Department.schedules.resources.vocabulary import GetFaculty


# Need vocabs for 'component', 'courseDays', 'attributes'
#  Also need to figure out how we are going to implement the course times

class ICourses(model.Schema):
    """Schema for main course datagrid."""

# Make title read only
    title = schema.TextLine(
        title=(u"What semester is this for?")
    )

    subject = schema.Choice(
        title=(u'Course Subject'),
        values=[],
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        default=101,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        default=(u"YY"),
    )

    # Maybe this should be ommitted?
    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        max=200,
        default=50
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

    instructor = schema.Choice(
        title=(u'Course Instructor'),
        source=GetFaculty,
    )
