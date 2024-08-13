# -*- coding: utf-8 -*-

from collections import deque #ila pronta para python
fila = deque() # instancia a  fila
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila
fila.append('X')# adiciona elemanto na fila
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila

fila.append('Y')# adiciona elemanto na fila
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila

fila.append('Z')# adiciona elemanto na fila
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila

#para remover elemento da fila ela remove e devolve o elemento em uma variavel
print('Removendo elementos da fila')
elemento_retirado = fila.popleft() #remove o primeiro elemento
print('Elemento removido da fila:\t', elemento_retirado)
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila

elemento_retirado = fila.popleft() #remove o primeiro elemento
print('Elemento removido da fila:\t', elemento_retirado)
print('\nMinha fila é:', list(fila)) #Imprimi valores da fila