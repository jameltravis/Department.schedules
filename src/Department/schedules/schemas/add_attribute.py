# -*- coding: utf-8 -*-
"""Module for adding attributes."""

from zope import schema
from plone.autoform import model
from Department.schedules import _

class IAddAttribute(model.Schema):
    """Adds new attributes"""

    title = schema.Choice(
        title=(u'Human readable title'),
        description=(u'Ex: Request a Smartroom'),
        required=True
    )

    courseAttribute = schema.TextLine(
        title=(u'CUNYFirst Attribute Name'),
        required=True
    )

