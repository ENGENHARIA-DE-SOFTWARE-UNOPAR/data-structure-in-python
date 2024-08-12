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

    
    def remove(self, lista, valor):

        # Verifica se o item a ser removido é o head

        if lista.head and lista.head.data == valor:
            lista.head = lista.head.next

        else:

        #   Detecta a posição do elemento
            before = None
            navegar = lista.head

        # Navega pela lista para encontrar o elemento

        while navegar and navegar.data != valor:

            before = navegar
            navegar = navegar.next
            #print(navegar.data)

        # Remove o item se ele for encontrado
        if navegar:
            before.next = navegar.next
    
    def busca(lista, valor):

        navegar = lista.head

        while navegar and navegar.data != valor:

            navegar = navegar.next
            return navegar