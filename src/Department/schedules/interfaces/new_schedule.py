# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

# Model/Schema Interface
from Department.schedules import _
from zope import schema
from zope.interface import implements
from plone.directives import form
from plone.supermodel import model
from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory
# from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from Department.schedules.interfaces.datagrid_schemas import (
    ICourses,
    EveningCourses,
    WeekendCourses
)
# from Department.schedules.interfaces.datagrid_schemas import (
#     ICourses,
#     WEEKDAY_SCHEMA,
#     WEEKEND_SCHEMA
# )

# WEEKDAY_SCHEMA.courseDays = schema.List(
#     title=(u'Days'),
#     value_type=schema.Choice(
#         values=[u'WEEK_DAYS', u'Select One', u'Another One'],
#         default=(u'Select One')
#     ),
# )

# WEEKEND_SCHEMA.courseDays = schema.List(
#     title=(u'Days'),
#     value_type=schema.Choice(
#         values=[u'WEEKEND', u'Select One', u'Another One'],
#         default=(u'Select One')
#     ),
# )

class ISchedule(model.Schema):

    title = schema.TextLine(
        title=(u'Department and Semester'),
        required=True,
    )

    # Data grid for Daytime Course requests
    form.widget(dayCourses=DataGridFieldFactory)
    dayCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=ICourses
        ),
        required=False,
    )

    # Data grid for evening Course requests
    form.widget(eveningCourses=DataGridFieldFactory)
    eveningCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=EveningCourses
        ),
        required=False,
    )

    # Weekend Datagrid
    form.widget(weekendCourses=DataGridFieldFactory)
    weekendCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(title=(u'Courses'), schema=WeekendCourses),
        required=False,
    )
