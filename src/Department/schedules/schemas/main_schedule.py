# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

from zope import schema
from plone.directives import form
from plone.supermodel import model
from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from Department.schedules import _
from Department.schedules.models.schemas import ICourses


class ISchedule(model.schema):

    title = schema.TextLine(
        title=(u'Department and Semester'),
        description=(u'Ex: Biology Fall 2009'),
        required=True,
    )

    # Data grid for Course requests
    form.widget(newCourses=DataGridFieldFactory)
    newCourses = schema.List(
        title=(u'Please enter courses you would'),
        value_type=DictRow(title=(u'Courses'), schema=ICourses),
        required=False,
    )
