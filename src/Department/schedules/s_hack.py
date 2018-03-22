# -*- coding: utf-8 -*-
"""Module for getting plone to recognize content types.
"""

from zope import schema
from plone.supermodel import model
from Department.schedules import _
from Department.schedules.schemas.add_attribute import IAddAttribute
from Department.schedules.schemas.add_component import IAddComponent
from Department.schedules.schemas.add_course import IAddCourse
from Department.schedules.schemas.add_department import IAddDepartment
from Department.schedules.schemas.add_faculty import IAddFaculty
from Department.schedules.schemas.add_title_rank import IAddTitleRank
from Department.schedules.schemas.schedule import ISchedule


ADD_ATTRIBUTE = IAddAttribute()
ADD_COMPONENT = IAddComponent()
ADD_COURSE = IAddCourse()
ADD_DEPARTMENT = IAddDepartment()
ADD_FACULTY = IAddFaculty()
ADD_TITLE_RANK = IAddTitleRank()
ADD_SCHEDULE = ISchedule()
