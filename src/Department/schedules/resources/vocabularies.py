# -*- coding: utf-8 -*-
"""Module containing vocabularies called from control panel."""

from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory





@provider(IVocabularyFactory)
def RankVocabularyFactory(context):
    values = api.portal.get_registry_record('york.scheduling.newTitle')
    return safe_simplevocabulary_from_values(values)

# @provider(IVocabularyFactory)
# def DepartmentVocabularyFactory(context):
#     current_user = api.user.get_current()
#     values = api.portal.get_registry_record('york.scheduling.department')