import sys
try:
    value = input("Digite um número: ")
    index = int(value) 
except ValueError as error:
    print(f'Favor digitar apenas números inteiros, encerrando o programa.')
    sys.exit()    

lista = [0]

for i in range(0, index + 1):
    value_in_list = lista[i]
    lista.append(i + value_in_list)
if index in lista:
    print(f'\n{index} se encontra na lista')
else:
    print(f'\n{index} não se encontra na lista')
