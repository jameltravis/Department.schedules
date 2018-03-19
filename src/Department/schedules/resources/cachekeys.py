# -*- coding: utf-8 -*-
"""Module containing cache keys used in ```vocubulary.py``` or elsewhere.

There are more cache keys here than are currently in use. Based on the systems'
performance, or how often new things are being added to the catalog,
you may find it more beneficial to use these cache keys instead of
some of the lambda functions used in the ```vocabulary.py``` .
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