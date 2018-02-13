# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from Department.schedules.testing import DEPARTMENT_SCHEDULES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that Department.schedules is properly installed."""

    layer = DEPARTMENT_SCHEDULES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if Department.schedules is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'Department.schedules'))

    def test_browserlayer(self):
        """Test that IDepartmentSchedulesLayer is registered."""
        from Department.schedules.interfaces import (
            IDepartmentSchedulesLayer)
        from plone.browserlayer import utils
        self.assertIn(IDepartmentSchedulesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DEPARTMENT_SCHEDULES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['Department.schedules'])

    def test_product_uninstalled(self):
        """Test if Department.schedules is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'Department.schedules'))

    def test_browserlayer_removed(self):
        """Test that IDepartmentSchedulesLayer is removed."""
        from Department.schedules.interfaces import \
            IDepartmentSchedulesLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDepartmentSchedulesLayer, utils.registered_layers())
