# -*- coding: utf-8 -*-





class ItemLista:

    def __init__(self, data=0, nextItem=None):

        self.data = data
        self.next = nextItem

 

    def __repr__(self):
        return '%s => %s' % (self.data, self.next)
    
class ListaEncadeada:

    def __init__(self):
        self.head = None

 

    def __repr__(self):
        return "%s" % (self.head)