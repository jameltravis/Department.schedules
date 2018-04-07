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

@provider(IVocabularyFactory)
def subject_vocabulary_factory(context):
    """Provides dropdowns for the course subejcts.
    
    Searches the registry for course subjects then filters the results
    based on the department the current logged in user belongs to. Once
    the list is filtered, everything before ``': '`` is removed; thus
    in order to return proper results, the admins MUST enter any new
    subjects in the control panel like so: ``foo: bar`` .

    TL;DR: this is the function that generates the Course Subject drop-down.

    Args:
        context(context): Plone handles this auto-magically.

    Returns:
        collection: (u'item1', u'item2', u'item3', u'etc')
    
    Example:
        >>>zope.schema.Choice(
            title=u'foo',
            vocabulary="whatever.named.vocabulary.this.becomes"
        )
    """
    # get current user
    current_user = api.user.get_current()
    user_dept = current_user.getProperty('department')
    records = api.portal.get_registry_record('york.scheduling.courseSubjects')
    
    # get rid of everything before semicolon
    values = tuple(
        [item.split(': ')[1].upper() for item in records 
        if user_dept.lower() in item.lower()]
    )
    return safe_simplevocabulary_from_values(values)




# @provider(IVocabularyFactory)
# def DepartmentVocabularyFactory(context):
#     current_user = api.user.get_current()
#     values = api.portal.get_registry_record('york.scheduling.department')