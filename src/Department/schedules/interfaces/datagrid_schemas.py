# -*- coding: utf-8 -*-
"""Schema used for datagrid fields."""

from Department.schedules import _
from zope import schema
# from plone.autoform import directives
from plone.supermodel import model
# from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
# from Department.schedules.resources.vocabulary import (
#     CourseSubjectVocab,
#     GetFaculty,
#     GET_ATTRIBUTES,
#     GET_COMPONENTS,
#     GET_DEPARTMENTS,
#     GET_RANKS,
#     GET_SCHOOLS
# )
# from Department.schedules.resources.vocab_source import (
#     HOURS,
#     MINUTES,
#     SEMESTERS,
#     TIME_OF_DAY,
#     WEEK_DAYS,
#     WEEKEND,
# )

# ICourses is used to create intances for Weekday and
# weekend datagrids

class ICourses(model.Schema):
    """Schema for main course datagrid."""

    title = schema.Choice(
        title=(u"What semester is this for?"),
        values=[u'SEMESTERS', u'BLAHBLAH'],
    )

    subject = schema.Choice(
        title=(u'Course Subject'),
        values=[u'TEST',u'CourseSubjectVocab'],
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        default=(u"YY"),
    )

    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        max=500,
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        max=500,
    )

    # Days of the Week
    # directives.widget(courseDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            values=[u'DAYS', u'More days', u'even more days']
        ),
    )

    # Time field start
    # Create if statement 
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=True,
        values=[u'HOURS', u'LKLAM', u'KJBKJNAK'],
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=True,
        values=[u'MINUTES', u'LKNALSND'],
    )


    # directives.widget(component=checkboxes)
    component = schema.List(
        title=(u'Course Component'),
        required=False,
        value_type=schema.Choice(
            values=[u'GET_COMPONENTS', u'BKNLAKNS', u'KJASKJAD'],
        ),
    )

    # directives.widget(attributes=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        required=False,
        value_type=schema.Choice(
            values=[u'GET_ATTRIBUTES', u'ASNLAKND', u'None'],
            default=(u'None')
        )
    )

    instructor = schema.Choice(
        title=(u'Course Instructor'),
        required=False,
        values=[u'GetFaculty', u'BLASTERZ'],
    )

    # Lets re-use this. Lets instantiate this class
    # and add some information to help us know
    # what each instance is for.
    def __init__(self, name):
        self.name = name



# Schema that feeds Weekday CourseGrid
WEEKDAY_SCHEMA = ICourses('Weekday')

# Schema that feeds Weekend CourseGrid
WEEKEND_SCHEMA = ICourses('Weekend')

WEEKDAY_SCHEMA.courseDays = schema.List(
    title=(u'Days'),
    value_type=schema.Choice(
        values=[u'WEEK_DAYS', u'Select One'],
        default=(u'Select One')
    ),
)

WEEKEND_SCHEMA.courseDays = schema.List(
    title=(u'Days'),
    value_type=schema.Choice(
        values=[u'WEEKEND', u'Select One'],
        default=(u'Select One')
    ),
)
