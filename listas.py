# -*- coding: utf-8 -*-



#criação de variaveis com valores e tipos diferentes


lista_numerica = [1, 2, 3, 4, 5]
print(lista_numerica)

lista_mista = ['Natan', 2, True]
print(lista_mista)

dicionario = {
    'A' :   'adenina',
    'T' :   'citosina',
    'T' :   'timina',
    'G' :   'guanina'
}
print(dicionario)

tupla = (1, 2, 3, 4) #Uma vez criada não muda mais.
print(tupla)

lista_aninhada = [[1, 2, 3], [85, 56, 98, 101]]#uma lista dentro de outra lista
print(f'{lista_aninhada}\n')
#Acesso as variaveis criadas

primeiro_elemento_lista = lista_mista[1] #O python inicia em 0
print(f'Primeiro elemento da lista {primeiro_elemento_lista}\n')
print(f'Primeiro elemento da segunda linha da lista aninhada:\t{lista_aninhada[1][0]}\n')





#Alteração das variaveis criadas
print('\n\nAlterando valores')
lista_numerica[1] = 52
lista_mista[2] = False
print(f' Lista Numerica:\t{lista_numerica} e\n Lista mista:\t{lista_mista}')

#Inserindo elemento
print('\n\nInserindo elemento')
lista_numerica.append(6)
lista_mista.append('Ogliari')
print(f' Lista Numerica:\t{lista_numerica} e\n Lista mista:\t{lista_mista}')


#Removendo elementos
print('\n\nRemovendo elementos')
lista_numerica.remove(52)
lista_mista.remove('Ogliari')
print(f' Lista Numerica:\t{lista_numerica} e\n Lista mista:\t{lista_mista}')