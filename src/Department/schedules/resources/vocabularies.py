# -*- coding: utf-8 -*-
"""Module containing vocabularies/collections used for drop down menues.
"""

from plone import api
from plone.app.vocabularies.terms import (
    safe_simplevocabulary_from_values as safe_vocab)
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def attribute_vocabulary_factory(context):
    """Gets course attributes.
    """
    values = api.portal.get_registry_record('york.scheduling.courseAttributes')
    return safe_vocab(values)


@provider(IVocabularyFactory)
def component_vocabulary_factory(context):
    """Gets course components.
    """
    values = api.portal.get_registry_record('york.scheduling.courseComponents')
    return safe_vocab(values)


@provider(IVocabularyFactory)
def day_course_times_vocabulary_factory(context):
    """Gets day course times.
    """
    values = api.portal.get_registry_record('york.scheduling.dayCourseTimes')
    return safe_vocab(values)

@provider(IVocabularyFactory)
def night_course_times_factory(context):
    """Gets night course times.
    """
    values = api.portal.get_registry_record('york.scheduling.nightCourseTimes')
    return safe_vocab(values)


# get faculty from portal, should work, needs real life tests
# To Rafael: Here is where I try and get the faculty.
@provider(IVocabularyFactory)
def faculty_vocabulary_factory(context):
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


# Get ranks from registry
@provider(IVocabularyFactory)
def rank_vocabulary_factory(context):
    """Gets faculty rank.
    """
    values = api.portal.get_registry_record('york.scheduling.newTitle')
    return safe_vocab(values)


# Get ranks from registry
@provider(IVocabularyFactory)
def weekday_vocabulary_factory(context):
    """Gets days of week.
    """
    values = api.portal.get_registry_record('york.scheduling.weekdayDays')
    return safe_vocab(values)

# Get ranks from registry
@provider(IVocabularyFactory)
def weekend_vocabulary_factory(context):
    """Gets days of week.
    """
    values = api.portal.get_registry_record('york.scheduling.weekendDays')
    return safe_vocab(values)


# should work, needs test
@provider(IVocabularyFactory)
def subject_vocabulary_factory(context):
    """Provides dropdowns for the course subejcts.
    
    Searches the registry for course subjects then filters the results
    based on the department the current logged in user belongs to. Once
    the list is filtered, everything before ``': '`` is removed; thus,
    in order to return proper results, the admins MUST enter any new
    subjects in the control panel like so: ``foo: bar`` .

    TL;DR: this is the function that generates the Course Subject drop-down.

    Args:
        context (?): Plone handles this auto-magically.

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
