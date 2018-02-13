# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import Department.schedules


class DepartmentSchedulesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=Department.schedules)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'Department.schedules:default')


DEPARTMENT_SCHEDULES_FIXTURE = DepartmentSchedulesLayer()


DEPARTMENT_SCHEDULES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DEPARTMENT_SCHEDULES_FIXTURE,),
    name='DepartmentSchedulesLayer:IntegrationTesting'
)


DEPARTMENT_SCHEDULES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DEPARTMENT_SCHEDULES_FIXTURE,),
    name='DepartmentSchedulesLayer:FunctionalTesting'
)


DEPARTMENT_SCHEDULES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DEPARTMENT_SCHEDULES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DepartmentSchedulesLayer:AcceptanceTesting'
)
