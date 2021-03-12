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
while valor >= 1:
    valor = int(input('Digite o valor: '))
    print(f'{valor}^2: {valor ** 2}; {valor}^3: {valor ** 3}; Raiz Quadrada: {sqrt(valor)} ')

# 43.
idades = []
