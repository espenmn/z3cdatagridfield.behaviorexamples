# -*- coding: utf-8 -*-
#common stuff
from z3cdatagridfield.behaviorexamples import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.interface import Interface
from zope.interface import provider
from plone.autoform.directives import widget

#DataGridStuff
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow


class ISomefields(Interface):
    """ Fields to be used with DataGridField below
    """

    first_field = schema.TextLine(
        title=_(u'First Field'),
        description=_(u'FirstField here'),
        required=False,
    )

    second_field = schema.TextLine(
        title=_(u'Second field'),
        description=_(u'No good description'),
        required=False,
    )

@provider(IFormFieldProvider)
class IBasicstuff(model.Schema):
    """
    Here we use the fields defined in ISomefields
    """

    widget(simple_group=DataGridFieldFactory)
    simple_group = schema.List(title=u"Some simple fields",
        value_type=DictRow(title=u"My simple fields", schema=ISomefields),
        required=False,
    )
