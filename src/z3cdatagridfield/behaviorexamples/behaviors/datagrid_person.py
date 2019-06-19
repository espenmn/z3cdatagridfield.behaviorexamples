# -*- coding: utf-8 -*-
#common stuff
from z3cdatagridfield.behaviorexamples import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.autoform.directives import widget

#relations
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
#from z3c.relationfield.schema import RelationList

#DataGridStuff
from collective.z3cform.datagridfield import DataGridFieldFactory
#Note: For control panel and registry you need to import from
#from collective.z3cform.datagridfield.registry import DictRow
from collective.z3cform.datagridfield import DictRow
#Alternative imports
#from collective.z3cform.datagridfield import BlockDataGridField

#stuff we probably dont need right now
#from z3c.form import form
#from z3c.form import field
#from z3c.form.form import extends
#from zope import component



class IPerson(Interface):
    """ Fields to be used with DataGridField below
    """

    first_name = schema.TextLine(
        title=_(u'First Name'),
        description=_(u'First Name'),
        required=False,
    )

    last_name = schema.TextLine(
        title=_(u'Last Name'),
        description=_(u'Family Name'),
        required=False,
    )

    #we probably need 'many relation fields', since one person can have
    #several relations to same person
    #Teoretically, your x-wife is not your brothers wife
    family_relation = RelationChoice(
        title=_(u"Realation"),
        source=CatalogSource(portal_type=['DatagridDemoType', 'Person', 'etc']),
        required=False,
    )


@provider(IFormFieldProvider)
class IDatagridPersons(model.Schema):
    """
    Here we use the fields defined in IPerson for field 'table'
    """

    group = schema.TextLine(
        title=_(u'Group name'),
        description=_(u'Group name for persons'),
        required=False,
    )

    widget(table=DataGridFieldFactory)
    table = schema.List(title=u"Persons",
        value_type=DictRow(title=u"personrow", schema=IPerson),
        required=False,
    )




#fields['table'].widgetFactory = DataGridFieldFactory
#
class IDatagridPersonsMarker(Interface):
    """dont need this"""


#       pass
#
#
# @implementer(IDatagridPersons)
# @adapter(IDatagridPersonsMarker)
# class DatagridPersons(object):
#     def __init__(self, context):
#         self.context = context

    # @property
    # def group(self):
    #     if hasattr(self.context, 'group'):
    #         return self.context.group
    #         return None
    #
    # @group.setter
    # def group(self, value):
    #       self.context.group = value
    #
    # @property
    # def table(self):
    #     if hasattr(self.context, 'table'):
    #         return self.context.table
    #         return None
    #
    # @table.setter
    # def table(self, value):
    #       self.context.table = value
