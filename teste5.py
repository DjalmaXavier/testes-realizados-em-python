#Usando string manipulation

string = input('Digite uma palavra ou frase: ')
print(f'{string[::-1]}')

#Usando For
lista = [
    l for l in string
]
palavra_invertida = ''
for i in range(len(lista), 0, -1):
    x = i - 1
    palavra_invertida += palavra_invertida.join(lista[x])

print(palavra_invertida)