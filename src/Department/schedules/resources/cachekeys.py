# -*- coding: utf-8 -*-
"""Module containing cache keys used in ```vocubulary.py``` or elsewhere."""

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
    return str(len(results))
