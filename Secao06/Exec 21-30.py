# 21. Faça um programa que receba dois numeros inteiros, calcule e apresente:(Ambos incluem os valores digitados)
#   - A soma dos numeros pares desse intervalo de números;
#   - A multiplicação dos numeros inpares desse intervalo.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
soma = 0
mult = 1

if num1 < num2:
    for i in range(num1+1, num2):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i
else:
    for i in range(num2+1, num1):
        if i % 2 == 0:
            soma += i
        else:
            mult *= i

soma += num1 + num2
mult *= num1 * num2

print(f'Valores inseridos: {num1} e {num2}\n'
      f'Soma: {soma}\n'
      f'Multiplicação: {mult}')

# 22. Escreva um programa para o aluno introduzir, pelo teclado, uma sequencia arbitrária de notas(vaidos somente
# valores entre 10 e 20), e apresente como resultado a média aritmética, o programa deve parar de executar e
# apresentar os resultados quando o aluno inserir um valor inválido.
notas = list()

while True:
    nt = float(input('Digite o valor da nota: '))
    if 10 <= nt <= 20:
        notas.append(nt)
    else:
        break

media = sum(notas) / len(notas)

print(f'Média: {media}')

# 23. Faça um programa que leia um valor inteiro e imprima seus divisores.
num = int(input('Difite um valor: '))
div = list()
for n in range(1, num+1):
    if num % n == 0:
        div.append(n)
    else:
        continue

print(f'D({num}) = {div}')

# 24. Faça um programa que leia um valor inteiro e imprima a soma de seus divisores, com exceção dele mesmo.
num = int(input('Difite um valor: '))
div = list()
for n in range(1, num):
    if num % n == 0:
        div.append(n)
    else:
        continue

print(f'A soma dos divisores de {num} é: {sum(div)}')

# 25. Faça um um programa que some todos os numeros naturais abaixo de 1000 e que são múltiplos de 3 e de 5.
soma = 0

for n in range(0, 1000, 3):
    soma += n

for n in range(0, 1000, 5):
    soma += n

print(F'A soma de todos os multiplos de 3 e de 5 abaixo de 1000 é: {soma}')

# 26. Encontre o primeiro número múltiplo de 11, 13 ou 17 após um valor dado.
teste = valor = int(input('Digite um valor: '))
mult = 0
while True:
    teste += 1

    if teste % 11 == 0:
        mult = 11
        break
    elif teste % 13 == 0:
        mult = 13
        break
    elif teste % 17 == 0:
        mult = 17
        break
    else:
        continue

print(f'Após dado o valor {valor}, encontramos {teste}, multiplo de {mult}.')

# 27. Em matemática, o número harmonico designado por H(n) defini-se como a soma da série harmonica:
#           H(n) = 1 + 1/2 + 1/3 + 1/4 + 1/5 + ... + 1/n
# Faça um  programa que leia um valor n inteiro positivo e apresente o valor de H(n).
num = int(input('Difite um valor: '))
harm = 0
for n in range(1, num+1):
    harm += 1/n

print(f'H({num}) = {harm}')

# 28 Faça um programa que neia um valor N inteiro positivo, Calcule e mostre o valor de E, conforme e formula a seguir:
#       E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
n = int(input('Digite o valor de N: '))
e = 0


def fatorial(n):
    nFat = 1

    for i in range(1, n + 1):
        nFat *= i

    return nFat


for _ in range(n + 1):
    e += 1 / fatorial(_)

print(e)

# 29.escreva um programa para calcular o valor da série, para 5, termos:
#       S = 0 + 1/2! + 2/4! + 3/6! + ...
s = 0

for i in range(1, 6):
    s += i / fatorial(2*i)

print(f'S(5) = {s}')

# 30. Faça programas para resolver as seguintes equações:
n = int(input('Digite o valor de N: '))

# A) 1 + 2 + 3 + 4 + 5 + ... + n
a = 0
for i in range(n+1):
    a += i

# B) 1 - 2 + 3 - 4 + 5 - ... + (2n -1)
b = 0
for i in range(2*n):
    if i % 2 == 0:
        b -= i
    else:
        b += i

# C) 1 + 3 + 5 + 7 + ... + (2n - 1)
c = 0
for i in range(1, 2*n, 2):
    c += i

print(f'A: {a}\n'
      f'B: {b}\n'
      f'C: {c}')

