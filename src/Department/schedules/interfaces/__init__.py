# -*- coding: utf-8 -*-
"""Module where all models, interfaces, events and exceptions live.

Every package used in the models are imported here so Plone can find them.
"""

from datetime import time
from Department.schedules import _
from zope import schema
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.autoform import model, directives
from plone.directives import form
from plone.supermodel import model

from collective.z3cform.datagridfield import DictRow
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes

from Department.schedules.models.schemas import WEEKDAY_SCHEMA, WEEKEND_SCHEMA
from Department.schedules.resources.vocabulary import (
    GetFaculty,
    CourseSubjectVocab,
    GET_DEPARTMENTS,
    GET_ATTRIBUTES,
    GET_COMPONENTS,
    GET_RANKS,
    GET_SCHOOLS
)
from Department.schedules.resources.vocab_source import (
    DAYS,
    HOURS,
    MINUTES,
    TIME_OF_DAY,
    SEMESTERS,
    WEEK_DAYS,
    WEEKEND,
)


class IDepartmentSchedulesLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
