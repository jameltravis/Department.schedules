# -*- coding: utf-8 -*-
"""The ICourses class, used to produce the main datagrid field, is below."""

from zope import schema
from plone import api
from plone.autoform import model, directives
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from Department.schedules import _
from Department.schedules.resources.vocabulary import (
    GetFaculty,
    CourseSubjectVocab,
    DAYS,
    HOURS,
    MINUTES,
    COURSE_ATTRIBUTES,
    COURSE_COMPONENTS,
    TIME_OF_DAY
    )


# Need vocabs for 'component', 'courseDays', 'attributes'
#  Also need to figure out how we are going to implement the course times

class ICourses(model.Schema):
    """Schema for main course datagrid."""

# Make title read only, unless you intend on making a custom view
# (which will probably happen)
    title = schema.TextLine(
        title=(u"What semester is this for?")
    )

    subject = schema.Choice(
        title=(u'Course Subject'),
        source=CourseSubjectVocab,
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


# Days of the Week
    directives.widget(classDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            values=DAYS
        ),
    )

    hourStart = schema.Choice(
        title=(u'Time Start'),
        values=HOURS,
    )

    minuteStart = schema.Choice(
        title='',
        values=MINUTES,
    )

    startTimeOfDay = schema.Choice(
        title='',
        required=True,
        values=TIME_OF_DAY
    )

    hoursEnd = schema.Choice(
        title=(u'Time End'),
        values=HOURS,
    )

    minutesEnd = schema.Choice(
        title='',
        values=MINUTES,
    )

    endTimeOfDay = schema.Choice(
        title='',
        values=TIME_OF_DAY
    )

    directives.widget(classDays=checkboxes)
    component = schema.List(
        title=(u'Course Component'),
        required=False,
        value_type=schema.Choice(
            values=COURSE_COMPONENTS,
        )
    )

    directives.widget(classDays=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        value_type=schema.Choice(
            values=COURSE_ATTRIBUTES,
            default=(u'None')
        )
    )

    instructor = schema.Choice(
        title=(u'Course Instructor'),
        required=False,
        source=GetFaculty,
    )
