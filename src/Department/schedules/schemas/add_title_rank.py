# -*- coding: utf-8 -*-
"""Module for adding new titles/ranks to existing vocabularies."""

from zope import schema
from plone.supermodel import model
from Department.schedules import _

class IAddTitleRank(model.Schema):
    """Adds New titles to vocabularies."""

    title = schema.TextLine(
        title=(u'New Title'),
        description=(
            u'Please write the name of the new title below'
            ),
        required=False,
    )
