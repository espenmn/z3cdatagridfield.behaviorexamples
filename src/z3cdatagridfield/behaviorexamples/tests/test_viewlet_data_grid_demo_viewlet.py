# -*- coding: utf-8 -*-
from z3cdatagridfield.behaviorexamples.interfaces import IZ3cdatagridfieldBehaviorexamplesLayer
from z3cdatagridfield.behaviorexamples.testing import Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FUNCTIONAL_TESTING
from z3cdatagridfield.behaviorexamples.testing import Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.Five.browser import BrowserView
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager

import unittest


class ViewletIntegrationTest(unittest.TestCase):

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Document', 'other-document')
        api.content.create(self.portal, 'News Item', 'newsitem')

    def test_data_grid_demo_viewlet_is_registered(self):
        view = BrowserView(self.portal['other-document'], self.request)
        manager_name = 'plone.abovecontenttitle'
        alsoProvides(self.request, IZ3cdatagridfieldBehaviorexamplesLayer)
        manager = queryMultiAdapter(
            (self.portal['other-document'], self.request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.assertIsNotNone(manager)
        manager.update()
        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'data-grid-demo-viewlet']  # NOQA: E501
        self.assertEqual(len(my_viewlet), 1)


class ViewletFunctionalTest(unittest.TestCase):

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
