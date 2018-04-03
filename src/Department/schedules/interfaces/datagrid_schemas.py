# -*- coding: utf-8 -*-
"""Schema used for datagrid fields."""

from Department.schedules import _
from zope import schema
from plone.autoform import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
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

class MainTestGrid(model.schema):
    """Schema to end all schemas."""

    def __init__(self, title):
        """Init test datagrid.
        """
        self.title = title

        self.subject = schema.Choice(
            title=(u'Course Subject'),
            values=[u'TEST',u'CourseSubjectVocab'],
            required=False,
        )

        self.courseNumber = schema.TextLine(
            title=(u'Course Number'),
            required=False,
        )

        self.courseSection = schema.TextLine(
            title=(u'Section'),
            required=False,
        )

        self.enrollmentCapacity = schema.TextLine(
            title=(u'Enrollment Capacity'),
            required=False,
        )

        self.waitlist = schema.Int(
            title=(u'Wait List'),
            required=False,
            max=500,
        )

        self.courseDays = schema.TextLine(
            title(u'Days'),
            required=False,
            max=500,
        )

        self.timeStart = schema.Choice(
            title=(u'Days'),
            required=False,
            values=[u'Hours', u'mins', u'secs'],
        )

        self.timeEnd = schema.Choice(
            title=(u'Time End'),
            required=False,
            values=[u'Hours', u'mins', u'secs'],
        )

        self.component = schema.TextLine(
            title=(u'Course Component(s)'),
            default=(u"thing1, thing2, thing3"),
            required=False,
        )

        directives.widget(attributes=checkboxes)
        self.attributes = schema.List(
            title=(u'attributes'),
            required=False,
            value_type=schema.Choice(
                values=[u'value1', u'value2', u'value3' u'None'],
                default=(u'None')
            ),
        )

        self.instructor = schema.Choice(
            title=(u'Course instructor'),
            required=False,
            values=[u'instructor1', u'instructor2'],
        )


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

# Evening Course Schema
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
