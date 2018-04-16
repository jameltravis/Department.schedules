# -*- coding: utf-8 -*-
"""Module containing vocabularies/collections used for drop down menues.

#TODO: write proper docstrings. 
"""

from time import time
from plone import api
from plone.app.vocabularies.terms import (
    safe_simplevocabulary_from_values as safe_vocab)
from plone.memoize import ram
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
def course_section_vocabulary_factory(context):
    """Returns course sections.
    """
    values = api.portal.get_registry_record('york.scheduling.courseSections')
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
# @ram.cache(lambda *args: time() // 3600)
def faculty_vocabulary_factory(context):
    """Returns a list of faculty for drop downs.

    This operation is fairly intensive, especially if you end up adding faculty
    to the list (which you will). I added a caching decarator so that everytime
    the datagrid fields try to call the vocabulary, it is getting the value from
    the cached list.

    """
    #TODO Add types

    currentUser = api.user.get_current()
    crntUserDept = currentUser.getProperty('department')
    users = api.user.get_users()
    values = [
        user.upper() for user in users 
        if user.getProperty('department').lower() == crntUserDept.lower()
    ]

    # Get any added faculty from control panel
    newFaculty = api.portal.get_registry_record('york.scheduling.newFaculty')
    if not newFaculty or newFaculty is None:
        return safe_vocab(values)
    
    panelValues = [
        item.split(': ')[1].upper() for item in newFaculty 
        if crntUserDept.lower() in item.lower()
    ]
    extendedValues = values.extend(panelValues)
    return safe_vocab(extendedValues)


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
