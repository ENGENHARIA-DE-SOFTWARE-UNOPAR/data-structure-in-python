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
    
    def insere(self, lista, data):

        # cria um objeto para armazenar um novo item da lista 
        item = ItemLista(data)

        # o head é apontado como próximo item
        item.next = lista.head

        # o item atual se torna o head
        lista.head = item

#minha_lista = ListaEncadeada()

#print(type(minha_lista))