# -*- coding: utf-8 -*-
"""Schema used for datagrid fields."""

from Department.schedules import _
from zope import schema
from plone.autoform import directives
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes
from z3c.form import form


# #################################################
# OG DATAGRID CLASS
# #############################################
class ICourses(model.Schema):
    """original datagrid class.

    used for daytime classed. All other datagrids inherit from this one.
    """

    subject = schema.Choice(
        title=(u'Course Subject'),
        vocabulary="Course.Scheduling.Course_Subjects",
        required=False,
    )

    courseNumber = schema.TextLine(
        title=(u'Course Number'),
        required=False,
    )

    courseSection = schema.Choice(
        title=(u'Section'),
        required=False,
        vocabulary="Course.Scheduling.Course_Sections",
    )

    courseCredits = schema.TextLine(
        title=(u'Credits'),
        required=True,
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
            vocabulary="Course.Scheduling.Weekdays"
        ),
    )

    # Time field start
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=False,
        vocabulary="Course.Scheduling.Day_Course_Times",
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=False,
        vocabulary="Course.Scheduling.Day_Course_Times",
    )


    directives.widget(component=checkboxes)
    component = schema.List(
        title=(u'Course Component(s)'),
        required=False,
        value_type=schema.Choice(
            vocabulary="Course.Scheduling.Course_Components"
        )
    )

    directives.widget(attributes=checkboxes)
    attributes = schema.List(
        title=(u'attributes'),
        required=False,
        value_type=schema.Choice(
            vocabulary="Course.Scheduling.Course_Attributes",
        ),
    )

    instructor = schema.Choice(
        title=(u'Course Instructor'),
        required=False,
        vocabulary="Course.Scheduling.Department_Faculty",
    )




# ###################################################
# Evening Course Schema
# ##########################
class EveningCourses(ICourses):
    """renders the fields for the evening class datagrid."""

    # Time field start
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=False,
        vocabulary="Course.Scheduling.Night_Course_Times",
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=False,
        vocabulary="Course.Scheduling.Night_Course_Times",
    )



# ##################################
# WEEKEND DAYTIME DATAGRID
####################################
class WeekendCourses(ICourses):
    """Renders fields for weekend datagrid field.
    """

    # Days of the Week
    directives.widget(courseDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            vocabulary="Course.Scheduling.Weekend"
        ),
    )

    # Time field start
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=False,
        vocabulary="Course.Scheduling.Day_Course_Times",
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=False,
        vocabulary="Course.Scheduling.Day_Course_Times",
    )


########################################
# WEEKEND NIGHT DATAGRID
#######################################
class WeekendNightCourses(ICourses):
    """Schema for night courses at the college.
    """

    # Days of the Week
    directives.widget(courseDays=checkboxes)
    courseDays = schema.List(
        title=(u'Days'),
        required=False,
        value_type=schema.Choice(
            vocabulary="Course.Scheduling.Weekend"
        ),
    )

    # Time field start
    timeStart = schema.Choice(
        title=(u'Time Start'),
        required=False,
        vocabulary="Course.Scheduling.Night_Course_Times",
    )

    timeEnd = schema.Choice(
        title=(u'Time End'),
        required=False,
        vocabulary="Course.Scheduling.Night_Course_Times",
    )
