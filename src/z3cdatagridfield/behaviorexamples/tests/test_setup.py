# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from z3cdatagridfield.behaviorexamples.testing import Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that z3cdatagridfield.behaviorexamples is properly installed."""

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if z3cdatagridfield.behaviorexamples is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'z3cdatagridfield.behaviorexamples'))

    def test_browserlayer(self):
        """Test that IZ3CdatagridfieldBehaviorexamplesLayer is registered."""
        from z3cdatagridfield.behaviorexamples.interfaces import (
            IZ3CdatagridfieldBehaviorexamplesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IZ3CdatagridfieldBehaviorexamplesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['z3cdatagridfield.behaviorexamples'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if z3cdatagridfield.behaviorexamples is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'z3cdatagridfield.behaviorexamples'))

    def test_browserlayer_removed(self):
        """Test that IZ3CdatagridfieldBehaviorexamplesLayer is removed."""
        from z3cdatagridfield.behaviorexamples.interfaces import \
            IZ3CdatagridfieldBehaviorexamplesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IZ3CdatagridfieldBehaviorexamplesLayer,
            utils.registered_layers())
