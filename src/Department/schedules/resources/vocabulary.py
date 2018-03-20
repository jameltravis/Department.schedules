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
from plone.momoize import ram
from Department.schedules import _
from Department.schedules.resources.cachekeys import (
    __course_component_cachekey,
    __department_cachekey
)
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
@ram.cache(lambda *args: time() // 3600)
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

    if results:
        return SimpleVocabulary.fromValues(
            map(unicode.title, sorted(vocabularyVar.extend(results)))
        )
    return SimpleVocabulary.fromValues(
        map(unicode.title, sorted(vocabularyVar))
    )


GET_ATTRIBUTES = get_vocabulary('AddAttribute', COURSE_ATTRIBUTES)
GET_COMPONENTS = get_vocabulary('AddComponent', COURSE_COMPONENTS)
GET_DEPARTMENTS = get_vocabulary('AddDepartment', DEPARTMENTS)
GET_RANKS = get_vocabulary('AddTitleRank', FACULTY_RANKS)
GET_SCHOOLS = get_vocabulary('AddSchool', SCHOOLS)

# @ram.cache(__course_component_cachekey)
# def get_components():
#     """Returns the course components.

#     Course components are cached according to 

#     Args:
#         None.
    
#     Returns:
#         list: [u'foo', u'bar', u'spam']

#     Example:
#         >>>get_components()
#         [u'a', u'very', u'long', u'list']
#     """
#     catalog = api.portal.get_tool('portal_catalog')
#     getComponents = catalog.searchResults(**{'portal_type': 'AddComponent'})
#     components = [item['courseComponent'] for item in getComponents]

#     if components:
#         return SimpleVocabulary.fromValues(sorted(COURSE_COMPONENTS.extend(components)))
#     return SimpleVocabulary.fromValues(sorted(COURSE_COMPONENTS))

# @ram.cache(__department_cachekey)
# def get_schools():
#     """Provides list/vocabulary of Academic Schools.

#     Args:
#         None.
    
#     Returns:
#         list: [u'foo', u'bar', u'spam']

#     Example:
#         >>>get_schools()
#         [u'Arts and Sciences', u'Business and Information Systems', u'Health Sciences']
#     """
#     catalog = api.portal.get_tool('portal_catalog')
#     getSchools = catalog.searchResults(**{'portal_type': 'AddSchool'})
#     schools = [item['title'] for item in getSchools]

#     if schools:
#         return SimpleVocabulary.fromValues(sorted(SCHOOLS.extend(schools)))
#     return SimpleVocabulary.fromValues(sorted(SCHOOLS))


# @ram.cache(lambda *args: time() // 86400)
# def course_attributes():
#     """Returns course attributes.

#     Args:
#         None.
    
#     Returns:
#         list: [u'foo', u'bar', u'spam']

#     Example:
#         >>>course_attributes()
#         [u'a', u'very', u'long', u'list']
#     """
#     catalog = api.portal.get_tool('portal_catalog')
#     getAttributes = catalog.searchResults(**{'portal_type': 'AddAttribute'})
#     attributes = [item['title'] for item in getAttributes]

#     if attributes:
#         return SimpleVocabulary.fromValues(sorted(COURSE_ATTRIBUTES.extend(attributes)))
#     return SimpleVocabulary.fromValues(sorted(COURSE_ATTRIBUTES))

# # Delete this possibly
# def get_departments():
#     """Returns list as Plone vocabulary.
    
#     Args:
#         None.
    
#     Returns:
#         List: [u'foo', u'bar', u'eggs', u'parrot']
    
#     Example:
#         >>>school_vocab()
#         [u'foo', u'bar', u'eggs', u'parrot']
#     """
#     catalog = api.portal.get_tool('portal_catalog')
#     query = catalog.searchResults(**{'portal_type': 'AddDepartment'})
#     results = [item['title'] for item in query]

#     if results:
#         return SimpleVocabulary.fromValues(
#             map(unicode.title, sorted(DEPARTMENTS.extend(results)))
#         )
#     return SimpleVocabulary.fromValues(sorted(DEPARTMENTS))


# def get_ranks():
#     """Returns faculty ranks list as Plone vocabulary.
    
#     Args:
#         None.
    
#     Returns:
#         List: [u'foo', u'bar', u'eggs', u'parrot']
    
#     Example:
#         >>>school_vocab()
#         [u'foo', u'bar', u'eggs', u'parrot']
#     """
#     catalog = api.portal.get_tool('portal_catalog')
#     query = catalog.searchResults(**{'portal_type': 'AddDepartment'})
#     results = [item['title'] for item in query]

#     if results:
#         return SimpleVocabulary.fromValues(sorted(DEPARTMENTS.extend(results)))
#     return SimpleVocabulary.fromValues(sorted(DEPARTMENTS))



# Class based vocabularies below

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
        vocabulary = [
            item['name'] for item in FACULTYif item['department'] == context
        ]
        catalog = api.portal.get_tool('portal_catalog')
        findFaculty = catalog.searchResults(**{'portal_type': 'AddFaculty'})
        results = [
            item['title'] for item in findFaculty
            if item['facultyName'] not in vocabulary
            ]

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

