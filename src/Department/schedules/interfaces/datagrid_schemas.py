# -*- coding: utf-8 -*-
"""Schema used for datagrid fields."""

from Department.schedules import _
from zope import schema
from plone.autoform import model, directives
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from Department.schedules.resources.vocabulary import (
    GetFaculty,
    CourseSubjectVocab,
    GET_DEPARTMENTS,
    GET_ATTRIBUTES,
    GET_COMPONENTS,
    GET_RANKS,
    GET_SCHOOLS
)
from Department.schedules.resources.vocab_source import (
    DAYS,
    HOURS,
    MINUTES,
    TIME_OF_DAY,
    SEMESTERS,
    WEEK_DAYS,
    WEEKEND,
)

# ICourses is used to create intances for Weekday and
# weekend datagrids

class ICourses(model.Schema):
    """Schema for main course datagrid."""

    title = schema.Choice(
        title=(u"What semester is this for?"),
        default=(u'Select One'),
        values=SEMESTERS,
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
    directives.widget(courseDays=checkboxes)
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


    directives.widget(component=checkboxes)
    component = schema.List(
        title=(u'Course Component'),
        required=False,
        value_type=schema.Choice(
            values=GET_COMPONENTS,
        )
    )

    directives.widget(attributes=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        required=False,
        value_type=schema.Choice(
            values=GET_ATTRIBUTES,
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


# Schema that feeds Weekday CourseGrid
WEEKDAY_SCHEMA = ICourses('Morning', 'Weekday')

WEEKDAY_SCHEMA.courseDays = schema.List(
    title=(u'Days'),
    value_type=schema.Choice(
        values=WEEK_DAYS,
        default=(u'Select One')
    )
)

# Schema that feeds Weekend CourseGrid
WEEKEND_SCHEMA = ICourses('Morning', 'Weekend')

WEEKEND_SCHEMA.courseDays = schema.List(
    title=(u'Days'),
    value_type=schema.Choice(
        values=WEEKEND,
        default=(u'Select One')
    )
)


class IAddFaculty(model.Schema):
    """Adds new faculty to the portal.
    """

    title = schema.TextLine(
        title=(u"New Faculty Member's Name"),
        required=True
    )

    department =  schema.Choice(
        title=(u'Department'),
        required=True,
        source=GET_DEPARTMENTS,
    )

    facultyName = schema.TextLine(
        title=(u'Faculty Name'),
        description=(u'Please add the first and last name of the faculty member'),
        required=True,
    )

    titleRank = schema.Choice(
        title=(u'Please select your title'),
        required=True,
        source=GET_RANKS,
    )

    tenure = schema.Choice(
        title=(u'Do you currently hold tenure?'),
        required=True,
        values=[
            u'Select One',
            u'Yes',
            u'No'
        ],
    )

    school = schema.Choice(
        title=(u'Select your Academic School?'),
        required=True,
        source=GET_SCHOOLS,
    )
