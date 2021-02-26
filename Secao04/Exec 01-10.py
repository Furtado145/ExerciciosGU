# 1. Faça um programa que leia e imprima um numero inteiro.
numI = input()
print(f'Inteiro: {numI}')

# 2. Faça um programa que leia e imprima um numero Real
numR = input()
print(f'Real: {numR}')

# 3. Peça ao usuário para digitar 3 valores inteiros e imprima a soma deles.
num1, num2, num3 = input('Valor 1?'), input('Valor 2?'), input('Valor 3?')
soma = int(num1) + int(num2) + int(num3)
print(soma)

# 4. Leia um numero Real e imprima o resultado do quadrado desse numero.
numR = input('Digite o valor a ser elevado: ')
quadrado = pow(float(numR), 2)
print(f'{numR} ao quadrado é {quadrado}')

# Leia um numero real e imprima a quinta parte deste numero.
numR = input()
quinta = float(numR) / 5
print(f'{numR} dividido por 5 é: {quinta}')

# 6. Leia uma temperatura em graus Celsius e converta-a em graus Fahrenheit.
celsius = input("6. Digite a temperatura: ")
fahrenheit = float(celsius) * (9/5) + 32
print(f'{celsius} graus Celsuis em graus Fahrenheit é: {fahrenheit}')

# 7. Leia uma temperatura em graus Fahrenheit e converta-a em graus Celsius.
fahrenheit = input("7. Digite a temperatura: ")
celsius = 5 * (float(fahrenheit) - 32) / 9
print(f'{fahrenheit} graus Celsuis em graus Fahrenheit é: {celsius}')

# 8. Leia uma temperatura em graus Kelvin e converta-a em graus Celsius.
kelvin = float(input('8. Digite a temperatura: '))
celsius = kelvin - 273.15
print(f'{kelvin} graus Kelvin em graus Celsius é: {celsius}')

# 9. Leia uma temperatura em graus Celsius e converta-a em graus Kelvin.
celsius = float(input('9. Digite a temperatura : '))
kelvin = celsius + 273.15
print(f'{celsius} graus Celsius em graus Kelvin é: {kelvin}')

# 10. Leia uma velocidade em Km/h e converta-a em m/s
kmh = float(input('10. Digite a velocidade: '))
ms = kmh / 3.6
print(f'{kmh}km/h é igual a {ms}m/s')
