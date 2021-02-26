# 01. Leia um numero inteiro positivo N, e faça um contagem em ordem crescente de 0 até N
n = int(input('Digite o valor de N: '))
for i in range(n+1):
    print(i, end=' ')

# 12. Leia um numero inteiro positivo N, e faça um contagem em ordem decrescente de 0 até N
n = int(input('Digite o valor de N: '))
for i in range(n, -1, -1):
     print(i, end=' ')

# 13. Leia um numero inteiro positivo par N, e inprima todos os numeros pares de 0 até N em ordem crescente.
n = int(input('Digite o valor de N: '))
if n % 2 == 0:
    for i in range(0, n+1, 2):
        print(i, end=' ')
else:
    print('Valor inválido.')

# 14. Leia um numero inteiro positivo par N, e inprima todos os numeros pares de 0 até N em ordem decrescente.
n = int(input('Digite o valor de N: '))
if n % 2 == 0:
    for i in range(n, -1, -2):
        print(i, end=' ')
else:
    print('Valor inválido.')

# 15. Leia um valor inteiro positivo impar N, e inprima todos os numeros impares de 1 até N em ordem crescente.
n = int(input('Digite o valor de N: '))
if not n % 2 == 0:
    for i in range(1, n+1, 2):
        print(i, end=' ')
else:
    print('Valor inválido.')

# 16. Leia um valor inteiro positivo impar N, e inprima todos os numeros impares de 1 até N em ordem decrescente.
n = int(input('Digite o valor de N: '))
if not n % 2 == 0:
    for i in range(n, 0, -2):
        print(i, end=' ')
else:
    print('Valor inválido.')

# 17. Leia um numero inteiro positivo N, e mostre a soma dos N primeiros numeros naturais.
n = int(input("Digite o valor de N: "))
soma = 0
for i in range(n):
    soma += i

print(f"A soma dos {n} primeiros números naturais é: {soma}")

# 18. Faça um programa que receba N valores e por fim apresente o maior deles.
n = int(input("Informe quantos valores serão declarados: "))
lista = list()
for i in range(n):
    valor = int(input(f'Digite o {i+1}/{n} valor: '))
    lista.append(valor)

print(f'O maior valor declarado é: {max(lista)}')

# 19. Leia um valor de tres digitos e imprima cada algorismo de seu valor.
valor = str(input('Digite um valor de 100 à 999: '))
for i in valor:
    print(i)

# 20. Ler uma sequencia de numeros dados e determinar se são pares ou não. Devera por fim informar a quantidade de
# valor lidos e quanto deles são pares, o programa se finaliza quando for digitado o valor 1000.
lista = list()
pares = 0
while True:
    valor = int(input("Digite um valor: "))

    if valor == 1000:
        break
    elif valor % 2 == 0:
        pares += 1
        lista.append(valor)
    else:
        lista.append(valor)

print(f'Valores ditados: {lista}\n'
      f'Total: {len(lista)}\n'
      f'Quantidade de pares: {pares}')
