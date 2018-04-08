# -*- coding: utf-8 -*-
"""Module for configuring the control panel stuffs.

For the purposes of keeping class names brief, CS == Course Scheduling.
"""

from Department.schedules import _
from zope import schema
from zope.interface import Interface
from Department.schedules.resources.vocab_source import (
    COURSE_ATTRIBUTES,
    COURSE_COMPONENTS,
    DAY_COURSE_TIMES,
    DEPARTMENT_SUBJECTS,
    NIGHT_COURSE_TIMES,
    SCHOOLS)


class ICSVocubulary(Interface):
    """Creates fields that will create vocabularies.
    """

    courseAttributes = schema.Tuple(
        title=u'York College Course Attributes',
        default=COURSE_ATTRIBUTES,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    courseComponents = schema.Tuple(
        title=u'York College Course Components',
        default=COURSE_COMPONENTS,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    dayCourseTimes = schema.Tuple(
        title=u'Times for day courses',
        description=(
            u'These values get used for '
            u'the Course Scheduling drop-down menus'),
        default=DAY_COURSE_TIMES,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    courseSubjects = schema.Tuple(
        title=u'York College Course Subjects',
        default=DEPARTMENT_SUBJECTS,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    nightCourseTimes = schema.Tuple(
        title=u'Add a new course number',
        description=u'Add a new Course number to course vocabulary',
        default=NIGHT_COURSE_TIMES,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    courseSections = schema.Tuple(
        title=u'Available Course Sections',
        description=u'Course sections to be used in vocabulary',
        default=(
            u'XX',
            u'YY',
            u'ZZ'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    newDepartment = schema.Tuple(
        title=u'New department',
        description=u'Add a new department to department vocabulary',
        default=(
            u"Behavioral Sciences",
            u"Biology",
            u"Chemistry",
            u"Earth and Physical Sciences",
            u"English",
            u"History, Philosophy, and Anthropology",
            u"Mathematics and Computer Science",
            u"Performing and Fine Arts",
            u"World Languages, Literature, and Humanities",
            u"Accounting and Finance",
            u"Business and Economics",
            u"Health and Physical Education",
            u"Health Professions",
            u"Nursing",
            u"Occupational Therapy",
            u"Social Work",
            u"Teacher Education"
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    newSchool = schema.Tuple(
        title=u'New Academic School',
        description=u'Add new academic school to vocabulary',
        default=SCHOOLS,
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    newTitle = schema.Tuple(
        title=u'New Title/Rank',
        description=u'Add new faculty title',
        default=(
            u'Assistant Professor',
            u'Associate Professor',
            u'Professor'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    semesters = schema.Tuple(
        title=u'Days of the week',
        default=(
            u'Winter',
            u'Spring',
            u'Summer',
            u'Fall'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    weekdayDays = schema.Tuple(
        title=u'Days of the week',
        default=(
            u'Mon',
            u'Tues',
            u'Wed',
            u'Thurs',
            u'Fri'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    weekendDays = schema.Tuple(
        title=u'Days of the Weekend',
        default=(
            u'Sat',
            u'Sun',
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )
