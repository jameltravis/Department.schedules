# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

# Model/Schema Interface
from Department.schedules import _
from zope import schema
from zope.interface import implements
from plone.directives import form
from plone.supermodel import model
from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from Department.schedules.interfaces.datagrid_schemas import (
    WEEKDAY_SCHEMA,
    WEEKEND_SCHEMA
)


class ISchedule(model.schema):

    title = schema.TextLine(
        title=(u'Department and Semester'),
        description=(u'Ex: Biology Fall 2009'),
        required=True,
    )

    # Data grid for Daytime Course requests
    form.widget(dayCourses=DataGridFieldFactory)
    dayCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKDAY_SCHEMA
        ),
        required=True,
    )

    # Data grid for evening Course requests
    form.widget(eveningCourses=DataGridFieldFactory)
    eveningCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKDAY_SCHEMA
        ),
        required=True,
    )

    # Weekend Datagrid
    form.widget(weekendCourses=DataGridFieldFactory)
    weekendCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKEND_SCHEMA
        ),
        required=True,
    )
