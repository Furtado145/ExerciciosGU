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

# 42.
from math import sqrt

valor = 1
while valor > 0:

    valor = int(input('Digite o valor: '))

    if valor > 0:
        print(f'{valor}^2: {valor ** 2}; {valor}^3: {valor ** 3}; Raiz Quadrada: {sqrt(valor)} ')


# 43.
idades = []

id = 1
while id > 0:

    id = int(input('Digite a sua idade: '))

    if id > 0:
        idades.append(id)


print(idades)-
print(sum(idades) / len(idades))

# 44. Leia um numero positivo do usuario, então, calcule e imprima a sequencia de Fibonacci até o primeiro numero
# superior ao numero lido.
from math import sqrt


def fibo(x):
    if x <= 1:
        return x
    else:
        fx = fibo(x-1) + fibo(x-2)
        return fx


num = int(input('Digite o valor: '))
lFibo = ""
i = 0

while not fibo(i) > num:

    lFibo += f"{fibo(i)} "

    i += 1

print(lFibo)
"""

# 45.Faça um prog para convercões de velocidades, faça um menu com opções das converções e um opção de saída


def kmh2ms(v):
    vel = v / 3.6
    return f'{v}Km/h = {vel}m/s'


def ms2kmh(v):
    vel = v * 3.6
    return f'{v}m/s = {vel}Km/h'


choice = 0
while not choice == 3:
    choice = int(input(
        """
        1. Km/h para m/s
        2. ms para  Km/h
        3. Finalizar
        
        O que faremos: """))

    op = [kmh2ms, ms2kmh]

    if choice in range(1, 3):
        velocidade = float(input("Qual a velocidade a converter? "))
        print(op[choice-1](velocidade))

    else:
        print('Por favor selecione uma opção válida')

print('Até mais ')
