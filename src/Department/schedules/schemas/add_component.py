# -*- coding: utf-8 -*-
"""Module for adding Components."""

from zope import schema
from plone.supermodel import model
from Department.schedules import _

class IAddComponent(model.Schema):
    """Adds new attributes."""

    title = schema.TextLine(
        title=(u'New Component:'),
        description=(u'Ex: Request a Smartroom'),
        required=True
    )
