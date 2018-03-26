# -*- coding: utf-8 -*-
"""Module for adding attributes."""

from zope import schema
from plone.supermodel import model
from Department.schedules import _

class IAddAttribute(model.Schema):
    """Adds new attributes"""

    title = schema.TextLine(
        title=(u'Attribute name:'),
        required=True
    )
