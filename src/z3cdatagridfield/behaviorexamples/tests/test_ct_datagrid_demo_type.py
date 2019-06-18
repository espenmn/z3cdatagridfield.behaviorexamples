# -*- coding: utf-8 -*-
from z3cdatagridfield.behaviorexamples.testing import Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class DatagridDemoTypeIntegrationTest(unittest.TestCase):

    layer = Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_datagrid_demo_type_schema(self):
        fti = queryUtility(IDexterityFTI, name='DatagridDemoType')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('DatagridDemoType')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_datagrid_demo_type_fti(self):
        fti = queryUtility(IDexterityFTI, name='DatagridDemoType')
        self.assertTrue(fti)

    def test_ct_datagrid_demo_type_factory(self):
        fti = queryUtility(IDexterityFTI, name='DatagridDemoType')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_datagrid_demo_type_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='DatagridDemoType',
            id='datagrid_demo_type',
        )


    def test_ct_datagrid_demo_type_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='DatagridDemoType')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
