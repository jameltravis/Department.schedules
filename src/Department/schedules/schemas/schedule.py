# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

from zope import schema
from plone.directives import form
from plone.supermodel import model
from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from Department.schedules import _
from Department.schedules.models.schemas import WEEKDAY_SCHEMA, WEEKEND_SCHEMA


class ISchedule(model.schema):

    title = schema.TextLine(
        title=(u'Department and Semester'),
        description=(u'Ex: Biology Fall 2009'),
        required=True,
    )

    # Data grid for Daytime Course requests
    form.widget(newCourses=DataGridFieldFactory)
    dayCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKDAY_SCHEMA
        ),
        required=True,
    )

    # Data grid for evening Course requests
    form.widget(newCourses=DataGridFieldFactory)
    eveningCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKDAY_SCHEMA
        ),
        required=True,
    )

    # Weekend Datagrid
    form.widget(newCourses=DataGridFieldFactory)
    weekendCourses = schema.List(
        title=(u'Please submit your requests for daytime courses'),
        value_type=DictRow(
            title=(u'Courses'),
            schema=WEEKEND_SCHEMA
        ),
        required=True,
    )
