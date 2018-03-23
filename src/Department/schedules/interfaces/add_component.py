# -*- coding: utf-8 -*-
"""Module for adding Components."""

from Department.schedules import _
from zope import schema
from plone.supermodel import model


class IAddComponent(model.Schema):
    """Adds new attributes."""

    title = schema.TextLine(
        title=(u'Component name:'),
        required=True
    )
