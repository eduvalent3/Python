""""Desenvolva o programa que cria uma lista vazia, lê vários números,
armazena na lista e mostre estas informações:

a- Mostre a lista;
b- Quantidade de elementos armazenados na lista;
c- Soma dos valores da lista;
d- Maior valor da lista;
e- Menor valor da lista;
f- Leia um valor e verificar se ele está na lista;
g- No item anterior, mostre também a posição (índice) do valor encontrado;
h- Mostre a lista na ordem crescente;
i- Insira (acrescente) o valor 33 na posição (índice) 1 da lista;
j- Mostre a lista na ordem decrescente;
k- Calcule e mostre a média dos valores da lista;
l- Mostre a média com três casas decimais;
m- Porcentagem dos números maiores que dez da lista."""

lista = []

print('Digite [-1] para sair!')

while True:
    valor = int(input('Digite um valor inteiro: '))
    if valor == -1:
        break
    lista.append(valor)

print(lista) # A

print(f'A quantidade de elementos na lista é: {len(lista)}') # B

print(f'Soma dos valores da lista: {sum(lista)}') # C

print(f'O valor máximo é: {max(lista)}') # D

print(f'O valor mínimo é: {min(lista)}') # E

consulta = int(input('verfique se um valor está na lista: ')) #F e #G
if consulta in lista:
    print(f'Seu valor está na lista e a sua posição é {lista.index(consulta)}')
else:
    print('Esta valor não está na lista')

lista2 = sorted(lista)
print(f'A lista na ordem crescente é: {lista2}') # H

lista.insert(1, 33) # i
print(lista)

lista2.reverse() #J
print(f'A lista na ordem decrescente é: {lista2}')

print(f'A média dos valores da lista é {sum(lista) / len(lista):.3f}') # K e L

ct = 0
for v in lista:
    if v > 10:
        ct = ct + 1

print(f'A porcentagem de valores maiores que 10 é: {ct / len(lista) * 100:.2f}%') #F
