# -*- coding: utf-8 -*-
"""Module for configuring the control panel stuffs.

For the purposes of keeping class names brief, CS == Course Scheduling.
"""

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface

# Need to add feilds that were originally going to be 
# content types


class ICSVocubulary(Interface):

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
            u'None'
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
        value_type=schema.Textline(),
    )

    newCourseNumber = schema.Tuple(
        title=u'Add a new course number',
        description=u'Add a new Course number to course vocabulary',
        default=(u'100', u'200', u'300', u'400'),
        missing_value=None,
        required=False,
        value_type=schema.Textline(),
    )

    newCourseSubject = schema.Tuple(
        title=u'Add new course subject',
        description=u'Add'
    )


class CScheduleControlPanelForm(RegistryEditForm):
    schema = ICSVocubulary
    schema_prefix = "scheduling"
    label = u'Course Scheduling Settings'


CSchedulingView = layout.wrap_form(
    CScheduleControlPanelForm, ControlPanelFormWrapper)
