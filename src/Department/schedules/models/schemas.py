# -*- coding: utf-8 -*-
"""Module for Zope Schema models used for Department.schedules"""

from Department.courses import _
from Department.courses.resources import vocabu
from plone.autoform import model
from zope import schema

class ICourses(model.Schema):
    """Schema for entering courses."""

    department = schema.Choice(
        title=(u'Department'),
        values=

    )
    