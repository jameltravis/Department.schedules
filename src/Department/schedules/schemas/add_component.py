# -*- coding: utf-8 -*-
"""Module for adding Components."""

from zope import schema
from plone.autoform import model
from Department.schedules import _

class IAddComponent(model.Schema):
    """Adds new attributes"""

    title = schema.Choice(
        title=(u'Human readable title'),
        description=(u'Ex: Request a Smartroom'),
        required=True
    )

    courseComponent = schema.TextLine(
        title=(u'CUNYFirst Attribute Name'),
        required=True
    )
