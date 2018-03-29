# -*- coding: utf-8 -*-
"""Module for configuring the control panel stuffs.

For the purposes of keeping class names brief, CS == Course Scheduling.
"""
from Department.schedules import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope.interface import Interface
from Department.schedules.interfaces.controlpanel_schema import ICSVocubulary

# Need to add feilds that were originally going to be 
# content types

# Move this class to its own schema / model file
# Use instructions here: https://pypi.python.org/pypi/plone.app.registry



class CSControlPanelForm(RegistryEditForm):
    schema = ICSVocubulary
    schema_prefix = "york.scheduling"
    label = u'Course Scheduling Settings'


CSPanelView = layout.wrap_form(CSControlPanelForm, ControlPanelFormWrapper)
