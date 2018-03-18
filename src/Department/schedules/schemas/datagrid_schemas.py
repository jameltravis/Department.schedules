# -*- coding: utf-8 -*-
"""The ICourses class, used to produce the main datagrid field, is below."""

from zope import schema
from plone.autoform import model, directives
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from Department.schedules import _
from Department.schedules.resources.vocabulary import GetFaculty, CourseSubjectVocab
from Department.schedules.resources.vocab_source import (
    DAYS,
    HOURS,
    MINUTES,
    COURSE_ATTRIBUTES,
    COURSE_COMPONENTS,
    TIME_OF_DAY,
    SEMESTERS,
    WEEK_DAYS,
    WEEKEND,
    DAYTIME_HOURS
)

# The plan is to create a few datagrids:
# for the Day Classes, Evening classes and Weekend classes

# Create instances of ICourses to facilite that need, eliminating
# fields like courseTime for something more generic

class ICourses(model.Schema):
    """Schema for main course datagrid."""

    title = schema.Choice(
        title=(u"What semester is this for?"),
        default=(u'Select One'),
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

    enrollmentCapacity = schema.Int(
        title=(u'Enrollment Capacity'),
        max=500,
        default=50
    )

    waitList = schema.Int(
        title=(u'Wait List'),
        max=500,
    )

    # Days of the Week
    directives.widget(classDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            values=DAYS
        )
    )

    # Time field start
    # Create if statement 
    hourStart = schema.Choice(
        title=(u'Time Start'),
        required=True,
        values=HOURS,
    )

    minuteStart = schema.Choice(
        title='',
        required=True,
        values=MINUTES,
    )

    startTimeOfDay = schema.Choice(
        title='',
        required=True,
        values=TIME_OF_DAY
    )

    hoursEnd = schema.Choice(
        title=(u'Time End'),
        required=True,
        values=HOURS,
    )

    minutesEnd = schema.Choice(
        title='',
        required=True,
        values=MINUTES,
    )

    endTimeOfDay = schema.Choice(
        title='',
        values=TIME_OF_DAY
    )
# time field end


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

    def __init__(self, timeOfDay, weekend):
        self.timeOfDay = timeOfDay
        self.weekend = weekend


DAY_SCHEMA = ICourses('Moring', 'Weekday')

# Do more of these
DAY_SCHEMA.courseDays = schema.List(
    title=(u'Days'),
    value_type=schema.Choice(
        values=WEEK_DAYS,
        default=(u'Select One')
    )
)