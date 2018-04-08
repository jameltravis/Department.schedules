# -*- coding: utf-8 -*-
"""Schema used for datagrid fields."""

from Department.schedules import _
from zope import schema
from plone.autoform import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from z3c.form import form
# from Department.schedules.resources.vocab_source import (
#     HOURS,
#     MINUTES,
#     SEMESTERS,
#     TIME_OF_DAY,
#     WEEK_DAYS,
#     WEEKEND,
# )



# #################################################
# WORKING MAIN DATAGRID
# #############################################
class ICourses(model.Schema):
    """Schema for main course datagrid."""

    subject = schema.Choice(
        title=(u'Course Subject'),
        values=[u'TEST',u'CourseSubjectVocab'],
        required=False,
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=False,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        required=False,
        default=(u"YY"),
    )

    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        required=False,
        max=500,
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        required=False,
        max=500,
    )

    # Days of the Week
    # directives.widget(courseDays=acompWidget)
    courseDays = schema.TextLine(
        title=(u'Days'),
        required=False,
        default=(u"Mon, Tues, Wed, Thurs"),
    )

    # Time field start
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=False,
        values=[u'HOURS', u'LKLAM', u'KJBKJNAK'],
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=False,
        values=[u'MINUTES', u'LKNALSND'],
    )


    # directives.widget(component=acompWidget)
    component = schema.TextLine(
        title=(u'Course Component(s)'),
        default=(u"GET_COMPONENTS, BKNLAKNS, KJASKJAD"),
        required=False,
    )

    directives.widget(attributes=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        required=False,
        value_type=schema.Choice(
            values=[u'GET_ATTRIBUTES', u'ASNLAKND', u'None'],
            default=(u'None')
        ),
    )

    instructor = schema.Choice(
        title=(u'Course Instructor'),
        required=False,
        values=[u'GetFaculty', u'BLASTERZ'],
    )




# ###################################################
# Evening Course Schema
# ##########################
class EveningCourses(model.Schema):
    """renders the fields for the evening class datagrid."""

    subject = schema.Choice(
        title=(u'Course Subject'),
        required=False,
        values=[u'TEST',u'CourseSubjectVocab'],
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=False,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        required=False,
        default=(u"YY"),
    )

    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        required=False,
        max=500,
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        required=False,
        max=500,
    )

    # Days of the Week
    directives.widget(courseDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            values=[u'DAYS', u'More days', u'even more days']
        ),
    )

    # Time field start
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


    directives.widget(component=checkboxes)
    component = schema.List(
        title=(u'Course Component'),
        required=False,
        value_type=schema.Choice(
            values=[u'GET_COMPONENTS', u'BKNLAKNS', u'KJASKJAD'],
        ),
    )

    directives.widget(attributes=checkboxes)
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


# ##################################
# WORKING SCHEMA FOR THE WEEKEND DATA GRID
####################################
class WeekendCourses(model.Schema):
    """Renders fields for weekend datagrid field.
    """

    subject = schema.Choice(
        title=(u'Course Subject'),
        required=False,
        values=[u'TEST',u'CourseSubjectVocab'],
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=False,
    )

    courseSection = schema.TextLine(
        title=(u'Section'),
        required=False,
        default=(u"YY"),
    )

    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        required=False,
        max=500,
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        required=False,
        max=500,
    )

    # Days of the Week
    directives.widget(courseDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            values=[u'DAYS', u'More days', u'even more days']
        ),
    )

    # Time field start
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


    directives.widget(component=checkboxes)
    component = schema.List(
        title=(u'Course Component'),
        required=False,
        value_type=schema.Choice(
            values=[u'GET_COMPONENTS', u'BKNLAKNS', u'KJASKJAD'],
        ),
    )

    directives.widget(attributes=checkboxes)
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
