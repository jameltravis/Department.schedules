# -*- coding: utf-8 -*-
"""Module where all models, interfaces, events and exceptions live.

Every package used in the schema classes are imported here.
This is the only way Plone is able to find them.
"""

from datetime import time
from Department.schedules import _
from zope import schema
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from plone.autoform import directives
from plone.directives import form
from plone.supermodel import model

from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory
# from collective.z3cform.widgets.token_input_widget import (
#     TokenInputFieldWidget as tagWidget
# )
# from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from z3c.form.browser.checkbox import CheckBoxFieldWidget as checkboxes

# from Department.schedules.resources.vocabulary import (
    # GetFaculty,
    # CourseSubjectVocab,
    # GET_DEPARTMENTS,
    # GET_ATTRIBUTES,
    # GET_COMPONENTS,
    # GET_RANKS,
    # GET_SCHOOLS
# )
# from Department.schedules.resources.vocab_source import (
#     HOURS,
#     MINUTES,
#     TIME_OF_DAY,
#     SEMESTERS,
#     WEEK_DAYS,
#     WEEKEND,
# )
from Department.schedules.interfaces.add_faculty import IAddFaculty
# from Department.schedules.interfaces.add_course import IAddCourse
# from Department.schedules.interfaces.add_department import IAddDepartment
from Department.schedules.interfaces.datagrid_schemas import (
    ICourses,
    EveningCourses,
    WeekendCourses
)
# from Department.schedules.interfaces.datagrid_schemas import (
#     WEEKDAY_SCHEMA,
#     WEEKEND_SCHEMA
# )
from Department.schedules.interfaces.new_schedule import ISchedule


class IDepartmentSchedulesLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
