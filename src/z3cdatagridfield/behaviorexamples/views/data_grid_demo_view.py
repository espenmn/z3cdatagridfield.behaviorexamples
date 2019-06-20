# -*- coding: utf-8 -*-

from z3cdatagridfield.behaviorexamples import _
from Products.Five.browser import BrowserView
from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class DataGridDemoView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('data_grid_demo_view.pt')

    def __call__(self):
        return self.index()

    def get_table(self):
        #return self.context.table
        # I think we should get the relations here
        # by looking at the uid of the family relatioon
        # we should walk through all
        # and look up item object
        table_list = []
        for row in self.context.table:
            rel = row['family_relation'].UID()
            item = api.content.get(UID=rel)
            row.update({'uid': rel, 'item': item})
            table_list.append(row)
        return table_list


    def get_sorted_table(self):
        #my_table = self.context.table
        my_table = self.get_table()
        return sorted(my_table, key=lambda k: k['last_name'])
