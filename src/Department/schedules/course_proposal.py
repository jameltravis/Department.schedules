# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

from Department.courses import _
from Department.courses.models.schemas import ICourses
from plone.supermodel import model
from plone.directives import form
from zope import schema
from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory

class ISchedule(model.schema):

    title = schema.TextLine(
        title=(u'Department and Semester'),
        description=(u'Ex: Biology Fall 2009'),
        required=True,
    )

    # Data grid for Course requests
    form.widget(newCourses=DataGridFieldFactory)
    newCourses = schema.List(
        title=(u'Please enter your phone numbers'),
        value_type=DictRow(title=(u'Phone numbers'), schema=ICourses),
        required=False,
    )