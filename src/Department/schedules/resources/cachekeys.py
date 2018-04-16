# -*- coding: utf-8 -*-
"""Module containing cache keys.

I was originally using these as a method to cache vocabulary items that
were resoucee intensive. This was important, as users of
collective.z3cform.datagridfields reported that vocabularies generated
from a ``source`` would be called repeatedly. I didn't want to have
Plone lagging balls, so I created the cache keys below. Since then,
I have moved from ``source`` vocabularies to Named Vocabularies. These
are here just in case you may ever need them.

TL;DR: This is a resource just in case you need them. If you don't,
feel free to delete this module. 
"""

from plone import api
from Department.schedules import _

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
    if not results:
        results = '0'
        return results
    return str(len(results))

def __department_cachekey():
    """Returns number of AddDepartment content types as a string.

    Args:
        None.
    
    Returns:
        str: 'this is a string'

    Example:
        >>>__course_component_cachekey()
        '9420'
    """
    catalog = api.portal.get_tool('portal_catalog')
    results = catalog.searchResults(**{'portal_type': 'AddDepartment'})
    if not results:
        results = '0'
        return results
    return str(len(results))


def __attribute_cachekey():
    """Returns number of AddDepartment content types as a string.

    Args:
        None.
    
    Returns:
        str: 'this is a string'

    Example:
        >>>__course_component_cachekey()
        '9420'
    """
    catalog = api.portal.get_tool('portal_catalog')
    results = catalog.searchResults(**{'portal_type': 'Addattribute'})
    if not results:
        results = '0'
        return results
    return str(len(results))