# 01. Faça um programa que determine e mostre os 5 primeiros multiplos de um valor dado (n>0)
num = int(input('Digite um valor positivo: '))
if num > 0:
    for _ in range(1, 6):
        print(f'{num * _}')
else:
    print('Numero invalido.')

# 02. Conte de 1 à 100, usando for while
lista = list[range(1, 101)]
for num in lista:
    print({num}, end=" ")

num = 1
while num <= 100:
    print({num}, end=" ")

# 03. Usando o while, faça uma contagem regressiva de 10 à 0, imprima "FIM" ao final da contagem.
num = 10
while num > 0:
    print(num)

# 04. Imprima uma contagem de iniciando em 0, contango de 1000 em 1000 e finalize em 100_000.
for _ in range(0,100_000, 1000):
    print({_})

# 05. Faça um programa que receba 10valores do  usuario e mostre a soma de todos ao final.
lista = list()
soma = 0
for _ in range(10):
    valor = int(input(f'Digite o {_+1}o valor: '))
    lista.append(valor)
    soma += valor

print(f'Valores inseridos: '
      f'    {lista}\n'
      f'Soma: {soma}')

# 06. Faça um programa que leia numeros inteiros e imprima sua media.
lista = list()
soma = 0
for _ in range(10):
    valor = int(input(f'Digite o {_+1}o valor: '))
    lista.append(valor)
    soma += valor

media = soma / len(lista)

print(f'Valores inseridos: {lista}\n'
      f'Média: {media}')

# 07. Faça um programa que receba 10 numeros inteiros, ignorando os não positivos, imprima sua média
lista = list()
soma = 0
for _ in range(10):
    valor = int(input(f'Digite o {_+1}o valor: '))
    if valor >= 0:
            lista.append(valor)
            soma += valor

media = soma / len(lista)

print(f'Valores validos inseridos: {lista}\n'
      f'Média: {media}')

# 08. Escreva um programa que leia 10 valores inseridos e por fim apresente o menor e o maior valor dado.
lista = list()
for _ in range(1, 11):
    valor = int(input(f'Digite o {_}o valor: '))
    lista.append(valor)

print(f'Valores inseridos: {lista}\n'
      f'Maior valor: {max(lista)}\n'
      f'Menor valor: {min(lista)}')

# 09. Faça um programa que leia um num inteiro N e imprima os N priemeiros numeros naturais impares.
n = int(input('Digite o valor: '))
for i in range(1, n*2, 2):
    print(i, end=' ')

# 10. Faça um programa que mostre a soma dos 50 primeiros numeros pares.
lista = list(range(0, 100, 2))
soma = 0
for n in lista:
    soma += n

print(f"Lista: {lista}\n"
      f"Soma: {soma}\n"
      f"Para confirmar = {len(lista)}")
