# -*- coding: utf-8 -*-
"""Module containing vocabularies called from control panel."""

from plone import api
from plone.app.vocabularies.terms import (
    safe_simplevocabulary_from_values as safe_vocab)
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory




# Get ranks from registry
@provider(IVocabularyFactory)
def RankVocabularyFactory(context):
    values = api.portal.get_registry_record('york.scheduling.newTitle')
    return safe_vocab(values)


# Get the course subjects from registry
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
    currentUser = api.user.get_current()
    userDept = currentUser.getProperty('department')
    records = api.portal.get_registry_record('york.scheduling.courseSubjects')
    
    # get rid of everything before semicolon
    values = tuple(
        [item.split(': ')[1].upper() for item in records 
        if userDept.lower() in item.lower()]
    )
    return safe_vocab(values)


# get faculty from portal
@provider(IVocabularyFactory)
def FacultyVocabularyFactory(context):
    """insert good docstring here.
    """
    #TODO Add better docstring!
    currentUser = api.user.get_current()
    crntUserDept = currentUser.getProperty('department')
    users = api.user.get_users()
    values = tuple(
        [user.upper() for user in users 
        if user.getProperty('department').lower() == crntUserDept.lower()]
    )
    return safe_vocab(values)
