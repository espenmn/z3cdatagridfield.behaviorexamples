# -*- coding: utf-8 -*-
from z3cdatagridfield.behaviorexamples.behaviors.datagrid_person import IDatagridPersonMarker
from z3cdatagridfield.behaviorexamples.testing import Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DatagridPersonIntegrationTest(unittest.TestCase):

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_datagrid_person(self):
        behavior = getUtility(IBehavior, 'z3cdatagridfield.behaviorexamples.datagrid_person')
        self.assertEqual(
            behavior.marker,
            IDatagridPersonMarker,
        )
