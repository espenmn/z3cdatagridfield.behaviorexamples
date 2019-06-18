# -*- coding: utf-8 -*-

from z3cdatagridfield.behaviorexamples import _
from Products.Five.browser import BrowserView


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class DataGridDemoView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('data_grid_demo_view.pt')

    def __call__(self):
        return self.index()

    def get_table(self):
        return self.context.table

    def get_sorted_table(self):
        my_table = self.context.table
        return sorted(my_table, key=lambda k: k['last_name']) 
        #.sort()
