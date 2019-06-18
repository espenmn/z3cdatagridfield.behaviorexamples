# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import z3cdatagridfield.behaviorexamples


class Z3CdatagridfieldBehaviorexamplesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=z3cdatagridfield.behaviorexamples)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'z3cdatagridfield.behaviorexamples:default')


Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FIXTURE = Z3CdatagridfieldBehaviorexamplesLayer()


Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FIXTURE,),
    name='Z3CdatagridfieldBehaviorexamplesLayer:IntegrationTesting',
)


Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FIXTURE,),
    name='Z3CdatagridfieldBehaviorexamplesLayer:FunctionalTesting',
)


Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        Z3CDATAGRIDFIELD_BEHAVIOREXAMPLES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Z3CdatagridfieldBehaviorexamplesLayer:AcceptanceTesting',
)
