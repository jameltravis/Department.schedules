# -*- coding: utf-8 -*-
"""Module used for adding new courses"""

from zope import schema
from plone.directives import form
from plone.supermodel import model
from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from Department.courses import _
from Department.courses.models.schemas import ICourses


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

    # departmentComments = schema.Text(
    #     title=(u'Dpartmental Comments'),
    #     description=(u'Comment box for department members'),
    #     required=False,
    # )

    # deanComments = schema.Text(
    #     title=(u'Dean Comments'),
    #     required=False,
    # )

    # provostComments = schema.Text(
    #     title=(u'Provost Comment section'),
    #     required=False,
    # )