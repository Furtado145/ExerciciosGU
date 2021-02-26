"""# Faça um programaque calcule o valor de S:
#       S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
dividendo = 1
s = 0

for div in range(1, 51):
    s += dividendo / div
    dividendo += 2

print(f"O valor de S é: {s}")

# 32. Façaum programa que simula o lançamento de dois dados d1 e d2, n vezes. Por fim, apresente os valores e mostre
# a relação entre eles(<, >, =)
import random
import time
def relacao(a, b):
    if a > b:
        return f'{a} > {b}'
    elif a == b:
        return f'{a} = {b}'
    else:
        return f'{a} > {b}'

n = int(input('Quantas vezes os dados serão rolados? '))
print("Que rolem os dados!!!")
time.sleep(2)
for i in range(n):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    print(f'Dado 1: {d1} e Dado 2: {d2}; {relacao(d1, d2)}')
    time.sleep(2)

# 33. Dados n e dois numeros inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros
# naturais que são multiplos de i ou de j e/ou de ambos.
# Ex.: N = 6; i = 2; j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8

n = int(input('Digite quantos multiplos deverão ser encontrados: '))
i = int(input('Qual o primeiro valor? '))
j = int(input('Qual o segundo valor? '))
saida = list()

aux = 0

while len(saida) < n:

    if aux % i == 0:
        saida.append(aux)
    elif aux % j == 0:
        saida.append(aux)

    aux += 1

print(f'Tendo N: {n}, I: {i} e J: {j}, a saida é: {saida}')

# 34. Faça um programa que calcule o menor numero divisivel por cada um dos numeros de 1 a 20.
# Ex.: 2520 é o menor numero divisivel por todos o numeros de 1 a 10, sem sobrar resto


def divisivel(a, b):
    if a % b == 0:
        return True
    else:
        return False


valor = div = reset_div = 20

while True:

    if div == 1:
        break
    else:
        if divisivel(valor, div):
            div -= 1
        else:
            valor += 10
            div = reset_div

print(valor)

# 35. Faça um programa que faca a soma dos valores impares dentro de um intervalo declarado pelo usuario
inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))
Lista = []

if inicio > final:
    print('Intervalo de valores Invalidos!\nFavor declarar um range onde o valor final é maior que o inicial.')

if inicio % 2 == 0:
    Lista = range(inicio+1, final+1, 2)
else:
    Lista = range(inicio, final + 1, 2)

print(f'Valores: {inicio} e {final};\nSoma dos valores inpares no intervalo: {sum(Lista)}')

# 36. Calcule a soma dos quadrados dos primeiros 100 numeros naturais, e depois calcule o quadrado da soma.
soma_quad = 0
quad_soma = 0
for i in range(1, 101):
    soma_quad += i**2
    quad_soma += i

quad_soma = quad_soma.__pow__(2)
dif = soma_quad - quad_soma

print(f'A soma dos quadrados: {soma_quad}\n'
      f'O quadrado das somas: {quad_soma}\n'
      f'A diferença: {quad_soma - soma_quad}')

# 37. Faça um programa que verifique
Lista = []

for i in range(10, 100):
    for j in range(1, 100):
        quad = (i + j) ** 2
        mil = int(str(i) + str(j))

        if quad == mil:
            Lista.append(mil)

print(Lista)

# 38. PULEI SAPORRA


# 39. Faça um programa que mostre a area de um triangulo, cujo a altura e a base foram fornecidas pelo usuario.
# Não aceitar valores iguais a zero.

base = int(input('Digite o valor da base: '))
alt = int(input('Digite o valor da altura: '))

area = (base * alt) / 2

print(f'A área do triangulo é {area}')

# 40. Elabore um programa que faça a leitura de varios valores inteiros, ate que se digite um valor negativo,
# assim o programa imprime o maior valor digitado e finaliza.
Lista = []

while True:
    num = int(input("Digite um valor: "))
    if num > 0: Lista.append(num)
    else:
        print(max(Lista))
        break
"""
# 41. Calcule a associação em paralelo de 2 resistores R1 e R2, ambos fornecidos pelo usuario. Faça repetidas vezes,
# com a condição de saida sendo quando o usuario enviar o valor 0(zero)


def paralelo(a, b):
    c = (a * b) / (a + b)
    return c


r1 = r2 = 1

while True:
    r1 = int(input('Digite o valor de R1: '))
    r2 = int(input('Digite o valor de R2: '))

    if r1 == 0 or r2 == 0:
        print('Valores Invalidos!!!')
        break
    else:
        r = paralelo(r1, r2)

        print(f'Resistencia equivalente ({r1} // {r2}): {r} Ohms')
