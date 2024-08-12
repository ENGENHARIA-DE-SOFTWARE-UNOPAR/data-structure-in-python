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
    'G' :   'guanina',
    'nome'  :   'NATAN'
}
print(dicionario)

tupla = (1, 2, 3, 4) #Uma vez criada não muda mais.
print(tupla)

lista_aninhada = [[1, 2, 3], [85, 56, 98, 101]]#uma lista dentro de outra lista
print(f'{lista_aninhada}\n')

lista_de_conjuntos = {1, 2, 3, 4, 5}#Conjunto de valores não duplicados


#Acesso as variaveis criadas

primeiro_elemento_lista = lista_mista[1] #O python inicia em 0
print(f'Primeiro elemento da lista {primeiro_elemento_lista}\n')
print(f'Primeiro elemento da segunda linha da lista aninhada:\t{lista_aninhada[1][0]}\n')
print(len(lista_aninhada))#Quantas linhas possui
print(len(lista_aninhada[0]))#Quantas elementos possui a linha de indice 0





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





#Operando dicionarios

chaves = dicionario.keys()
print(f'\nAs chaves do dicionario é:\t{chaves}\n')
valores = dicionario.values()
print(f'\nOs valores do dicionario é:\t{valores}\n')

#adicionando valores ao dic:
dicionario |= {'O' : 85, 'date' : '2024-2-25'} # observe o operador de atualização (|)
print(dicionario)

nome_dic = dicionario.get('O')#pega o valor do dic
print(nome_dic)
dicionario.pop('O')# remove o valor e a chave
print(dicionario)