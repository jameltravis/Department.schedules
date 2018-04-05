# -*- coding: utf-8 -*-
"""Module for configuring the control panel stuffs.

For the purposes of keeping class names brief, CS == Course Scheduling.
"""

from Department.schedules import _
from zope import schema
from zope.interface import Interface


class ICSVocubulary(Interface):
    """Creates fields that will create vocabularies.
    """

    courseAttributes = schema.Tuple(
        title=u'York College Course Components',
        default=(
            u'Add Smart Room',
            u'Hybrid',
            u'Fully Online',
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    courseComponents = schema.Tuple(
        title=u'York College Course Attributes',
        default=(
            u'None',
            u'Clinical',
            u'Experimental',
            u'Field Studies',
            u'Independent Study',
            u'Internship',
            u'Lab',
            u'Lecture',
            u'Recitation',
            u'Seminar',
            u'Writing Intensive'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    dayCourseTimes = schema.Tuple(
        title=u'Add a new course number',
        description=u'Add a new Course number to course vocabulary',
        default=(
            u'7:00 am',
            u'7:50 am',
            u'8:00 am',
            u'8:50 am',
            u'9:00 am',
            u'9:50 am',
            u'10:00 am',
            u'10:50 am',
            u'11:00 am',
            u'11:50 am',
            u'12:00 pm',
            u'12:50 pm',
            u'1:00 pm',
            u'1:50 pm',
            u'2:00 pm',
            u'2:50 pm',
            u'3:00 pm',
            u'3:50 pm',
            u'4:00 pm',
            u'4:50 pm',
            u'5:00 pm',
            u'5:50 pm'
        ),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    nightCourseTimes = schema.Tuple(
        title=u'Add a new course number',
        description=u'Add a new Course number to course vocabulary',
        default=(
            u'4:00 pm',
            u'4:50 pm',
            u'5:00 pm',
            u'5:50 pm',
            u'6:00 pm',
            u'6:50 pm',
            u'7:00 pm',
            u'7:50 pm',
            u'8:00 pm',
            u'8:50 pm',
            u'9:00 pm',
            u'9:50 pm',
            u'10:00 pm',
            u'10:50 pm',
        ),
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

    newCourseSubject = schema.Tuple(
        title=u'Add new course subject',
        description=u'Add new course subject to course vocabulary',
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
        default=(
            u'Arts and Sciences',
            u'Business and Information Systems',
            u'Health Sciences and Professional Programs'
        ),
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

