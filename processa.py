# -*- coding: utf-8 -*-

import lista_encadeada as le


lista  = le.ListaEncadeada()

print("Conteúdo da lista:", lista) # lista está vazia

#Como esta na CW1
#le.ListaEncadeada.insere(lista, 'shampoo')
#le.ListaEncadeada.insere(lista, 'biscoito')
#.....


lista.insere(lista, 'shampoo')
lista.insere(lista, 'biscoito')
lista.insere(lista, 'detergente') 
lista.insere(lista, 'abobrinha ')
lista.insere(lista, 'banana')

print(lista)

lista.remove(lista, "detergente")
print(lista)