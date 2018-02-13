# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from Department.schedules.interfaces import ISchedule
from Department.schedules.testing import DEPARTMENT_SCHEDULES_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ScheduleIntegrationTest(unittest.TestCase):

    layer = DEPARTMENT_SCHEDULES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Schedule')
        schema = fti.lookupSchema()
        self.assertEqual(ISchedule, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Schedule')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Schedule')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ISchedule.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Schedule',
            id='Schedule',
        )
        self.assertTrue(ISchedule.providedBy(obj))
