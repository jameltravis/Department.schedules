# -*- coding: utf-8 -*-
"""Vacubularies used for choice fields.

Please note: many functions below are cached using ```plone.memoize``` . To change
the caching, modify/change the argument passed to the ```ram.cache()``` decorator.
"""
from time import time
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from plone import api
from plone.memoize import ram
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from Department.schedules import _
from Department.schedules.resources.vocab_source import (
    COURSE_ATTRIBUTES,
    COURSE_COMPONENTS,
    DEPARTMENTS,
    DEPARTMENT_SUBJECTS,
    FACULTY,
    FACULTY_RANKS,
    SCHOOLS,
)

# Demo of subject_vocabulary_factory, see vocabularies.py
def get_subjects(context):
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
    """
    # get current user
    current_user = api.user.get_current()
    user_dept = current_user.getProperty('department')
    records = api.portal.get_registry_record('york.scheduling.courseSubjects')
    spam = []
    # values = [item.split(': ')[1] for item in records if user_dept.lower() in item.lower()]

    for items in records:
        if user_dept.lower() in items.lower():
            spam.extend(items)
    values = tuple([item.split(': ')[1] for item in spam])
    return safe_simplevocabulary_from_values(values)


# Vocabularies below

# Make sure that each content type is taken from the 'title' field
# @ram.cache(lambda *args: time() // 3600)
def get_vocabulary(contentType, vocabularyVar):
    """Returns list as Plone vocabulary.

    Searches the portal for a given content type and appends the 'title' field
    to the list, and returns it as a unicoded, TitleCased plone vocabulary.
    Note that despite the example below not being sorted, this function does
    indeed sort the returned list.
    
    Args:
        contentType(str): Name of the content type
        vocabularyVar(list)
    
    Returns:
        list: ['old school 1', 'old school 2', 'old school 3']
    
    Example:
        >>>SCHOOL_LIST = ['school1', 'school2', 'school3']
        >>>school_vocab(AddNewSchools, SCHOOL_LIST)
        [u'School 1', u'School 2', u'School 3', u'New School From ContentType']
    """
    catalog = api.portal.get_tool('portal_catalog')
    query = catalog.searchResults(**{'portal_type': contentType})
    results = [item['title'] for item in query]

    if query is None:
        return SimpleVocabulary.fromValues(
            map(unicode, sorted(vocabularyVar))
        )

    if query:
        return SimpleVocabulary.fromValues(
            map(unicode, sorted(vocabularyVar.extend(results)))
        )


GET_ATTRIBUTES = get_vocabulary('AddAttribute', COURSE_ATTRIBUTES)
GET_COMPONENTS = get_vocabulary('AddComponent', COURSE_COMPONENTS)
GET_DEPARTMENTS = get_vocabulary('AddDepartment', DEPARTMENTS)
GET_RANKS = get_vocabulary('AddTitleRank', FACULTY_RANKS)
GET_SCHOOLS = get_vocabulary('AddSchool', SCHOOLS)


class GetFaculty(object):
    """Source for schema.Choice fields.
    
    Provides a list of faculty members and makes them a vocabulary.
    Searches the catalog for new instructor names, if new instructors are present,
    the ```extend()``` method will be called. Strings converted to unicode
    then passed to ```SimpleVocabulary.fromValues``` .
    PS - By default, this function is limited to 1 call per day. To change that, modify
    the argument in the in the ```ram.cache()``` decorator. 

    Args:
        none.

    Returns:
        list: [u'Professor Foo', u'Professor Bar']
    
    Example:
        >>>foo = schema.Choice(
            title=(u'List of Faculty Names'),
            source=GetFaculty,
        )
        [u'Robert Duncan', u'Robin Harper', u'Kirstin Davies']
    """

    implements(IContextSourceBinder)
    
    @ram.cache(lambda *args: time() // 86400)
    def __call__(self, context, vocabulary):
        vocabulary = [item['name'] for item in FACULTY if item['department'] == context]
        catalog = api.portal.get_tool('portal_catalog')
        findFaculty = catalog.searchResults(**{'portal_type': 'AddFaculty'})
        results = [item['title'] for item in findFaculty if item['facultyName'] not in vocabulary]

        if results is None:
            return SimpleVocabulary.fromValues(
                sorted(map(unicode, vocabulary))
            )
        else:
            return SimpleVocabulary.fromValues(
                sorted(map(unicode, vocabulary.extend(results)))
            )



class CourseSubjectVocab(object):
    """Source for schema.Choice fields.
    
    Provides a list of faculty members and makes them a vocabulary.
    Searches the catalog for new courses, if new courses are present,
    ```extend()``` is called to extend the list of courses. Strings
    converted to unicode (this is Python2, after all) then passed
    to ```SimpleVocabulary.fromValues```.

    Args:
        none.

    Returns:
        list: [u'Professor Foo', u'Professor Bar']
    
    Example:
        >>>foo = schema.Choice(
            title=u'List of Faculty Names',
            source=CourseSubjectVocab,
        )
        [u'Robert Duncan', u'Robin Harper', u'Kirstin Davies']
    """

    implements(IContextSourceBinder)
    @ram.cache(lambda *args: time() // 86400)
    def __call__(self, context, vocabulary):
        vocabulary = [courses[context] for courses in DEPARTMENT_SUBJECTS][0]
        return SimpleVocabulary.fromValues(sorted(unicode(vocabulary.title())))

