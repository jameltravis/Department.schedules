# -*- coding: utf-8 -*-
"""Vacubularies used for choice fields.

Please note: many functions below are cached using ```plone.memoize``` . To change
the caching, modify/change the argument passed to the ```ram.cache()``` decorator.
"""

# from collections import Counter
from time import time
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from plone import api
from plone.momoize import ram
from Department.schedules import _
from Department.schedules.resources import cachekeys 
from Department.schedules.resources.vocab_source import (
    DEPARTMENT_SUBJECTS,
    FACULTY,
    COURSE_COMPONENTS
    )

# Cache Keys

def __catalog_count_cachekey():
    """Returns a cache key based on catalog updates"""

    catalog = api.portal.get_tool('portal_catalog')
    return str(catalog.getCounter())

def __course_component_cachekey():
    """Returns number of AddCourse content types in the catalog as a string.

    Args:
        None.
    
    Returns:
        str: 'this is a string'

    Example:
        >>>__course_component_cachekey()
        '9420'
    """
    catalog = api.portal.get_tool('portal_catalog')
    results = catalog.searchResults(**{'portal_type': 'AddCourse'})
    return str(len(results))


# Vocabularies below

@ram.cache(__course_component_cachekey)
def get_components():
    """Returns the course components.

    Course components are cached according to 

    Args:
        None.
    
    Returns:
        list: [u'foo', u'bar', u'spam']

    Example:
        >>>get_components()
        [u'a', u'very', u'long', u'list']
    """
    catalog = api.portal.get_tool('portal_catalog')
    getComponents = catalog.searchResults(**{'portal_type': 'AddComponent'})
    components = [item['courseComponent'] for item in getComponents]

    if components:
        return SimpleVocabulary.fromValues(sorted(COURSE_COMPONENTS.extend(getComponents)))
    return COURSE_COMPONENTS


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
        results = [
            item['facultyName'] for item in findFaculty
            if item['facultyName'] not in vocabulary
            ]

        if not results:
            return SimpleVocabulary.fromValues(sorted(map(unicode, vocabulary)))
        else:
            return SimpleVocabulary.fromValues(sorted(map(unicode, vocabulary.extend(results))))



class CourseSubjectVocab(object):
    """Source for schema.Choice fields.
    
    Provides a list of faculty members and makes them a vocabulary.
    Searches the catalog for new courses, if new courses are present,
    ```extend()``` is called to extend the list of courses. Strings
    converted to unicode (this is Python 2, after all) then passed
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
    @ram.cache()
    def __call__(self, context, vocabulary):
        vocabulary = [courses[context] for courses in DEPARTMENT_SUBJECTS][0]
        return SimpleVocabulary.fromValues(sorted(vocabulary))
