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
        List: ['old school 1', 'old school 2', 'old school 3']
    
    Example:
        >>>SCHOOL_LIST = ['school1', 'school2', 'school3']
        >>>school_vocab(AddNewSchools, SCHOOL_LIST)
        [u'School 1', u'School 2', u'School 3', u'New School From ContentType']
    """
    catalog = api.portal.get_tool('portal_catalog')
    query = catalog.searchResults(**{'portal_type': contentType})
    results = [item['title'] for item in query]

    if not query:
        return SimpleVocabulary.fromValues(
            map(unicode.title, sorted(vocabularyVar))
        )

    if query:
        return SimpleVocabulary.fromValues(
            map(unicode.title, sorted(vocabularyVar.extend(results)))
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

        if not results:
            return SimpleVocabulary.fromValues(
                sorted(map(unicode, vocabulary.title()))
            )
        else:
            return SimpleVocabulary.fromValues(
                sorted(map(unicode, vocabulary.extend(results).title()))
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

