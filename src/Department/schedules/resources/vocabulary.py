# -*- coding: utf-8 -*-
"""Vacubularies used for choice fields"""

from collections import Counter
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from plone import api
from plone.momoize import ram
from Department.courses import _
from Department.courses.resources.vocab_source import DEPARTMENT_SUBJECTS, FACULTY


def __catalog_count_cachekey():
    """Returns a cache key based on catalog updates"""

    catalog = api.portal.get_tool('portal_catalog')
    return str(catalog.getCounter())



class GetFaculty(object):
    """Source for schema.Choice fields.
    
    Provides a list of faculty members and makes them a vocabulary.
    Searches the catalog for new instructor names, if new instructors are present,
    extend method will be called. Strings converted to unicode (this is Python 2,
    after all) then passed to SimpleVocabulary.fromValues .

    Args:
        none.

    Returns:
        list: ['Professor Foo, Professor Bar']
    
    Example:
        >>>foo = schema.Choice(
            title=(u'List of Faculty Names'),
            source=GetFaculty,
        )
        [u'Robert Duncan', u'Robin Harper', u'Kirstin Davies']
    """

    implements(IContextSourceBinder)
    
    @ram.cache(__catalog_count_cachekey)
    def __call__(self, context, vocabulary):
        vocabulary = [item['name'] for item in FACULTY if item['department'] == context]
        catalog = api.portal.get_tool('portal_catalog')
        findFaculty = catalog.searchResults(**{
            'portal_type': 'AddFaculty'
            })
        results = [
            item['facultyName'] for item in findFaculty 
            if item['facultyName'] not in vocabulary
            ]
        if not results:
            return SimpleVocabulary.fromValues(sorted(map(unicode, vocabulary)))
        return SimpleVocabulary.fromValues(sorted(map(unicode, vocabulary.extend(results))))



class CourseSubjectVocab(object):
    """Source for schema.Choice fields.
    
    Provides a list of faculty members and makes them a vocabulary.
    Searches the catalog for new instructor names, if new instructors are present,
    extend method will be called. Strings converted to unicode (this is Python 2,
    after all) then passed to SimpleVocabulary.fromValues .

    Args:
        none.

    Returns:
        list: ['Professor Foo, Professor Bar']
    
    Example:
        >>>foo = schema.Choice(
            title=(u'List of Faculty Names'),
            source=GetFaculty,
        )
        [u'Robert Duncan', u'Robin Harper', u'Kirstin Davies']
    """

    implements(IContextSourceBinder)
    
    def __call__(self, context, vocabulary):
        vocabulary = [courses for department, courses in DEPARTMENT_SUBJECTS if department == context]
        return SimpleVocabulary.fromValues(sorted(map(unicode, vocabulary)))

