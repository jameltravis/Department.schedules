# -*- coding: utf-8 -*-
"""Vacubularies used for choice fields"""

from Department.courses import _
from plone import api

# Stock Faculty vocabularies
BEHAVIOR_FACULTY = ['Robert Duncan', 'Robin Harper']
SOCIOLOGY = ['foo', 'bar', 'spam']

def extend_faculty(department: str, vocabulary: list) -> list:
    """Extends list of instructors if necessary.

    Searches the catalog for new instructor names, if new instructors are present,
    extend method will be called. Strings are made unicode strings as last step.

    Args:
        department (str): name of the department (see Department.courses.add_faculty)
        vocabulary (list): list containing department specific faculty names

    Returns:
        list: ['Professor Foo, Professor Bar']
    
    Example:
        >>>extend_faculty('Behavioral Science', BEHAVIOR_FACULTY)
        [u'Robert Duncan', u'Robin Harper', u'Kirstin Davies']
    """
    catalog = api.portal.get_tool('portal_catalog')
    findFaculty = catalog.searchResults(**{
        'portal_type': 'AddFaculty',
        'department': department
        })
    results = [item for item in findFaculty if item['facultyName'] not in vocabulary]
    if not results:
        return sorted(map(unicode, vocabulary))
    return sorted(map(unicode, vocabulary.extend(results)))
