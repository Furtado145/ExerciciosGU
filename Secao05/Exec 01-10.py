import math

# 01. Faça um programa que receba um numero e mostre qual deles é o maior.
num1 = int(input('01. Valor1: '))
num2 = int(input('Valor2: '))
print(max(num1, num2))

# 02. Receba um valor do usuario, caso seja positivo calcule a raiz quadrada dele, caso contrario informe que o valor
# é invalido.
num = int(input('02. Digite um valor:'))
if num > 0:
    msg = math.sqrt(num)
else:
    msg = 'Valor invalido.'

print(msg)

# 03. Leia um numero real, se ele for positivo imprima a raiz quadrada, se for negativo imprima o valor ao quadrado.
num = float(input('03. Digite um valor:'))
if num > 0:
    msg = math.sqrt(num)
else:
    msg = num.__pow__(2)

print(msg)

# 04. Leia um valor e caso ele seja positivo apresente o valor dele ao quadrado e sua raiz quadrada.
num = int(input('04. Digite um valor:'))
if num > 0:
    raiz = math.sqrt(num)
    exp = num.__pow__(2)
    print(f'Raiz quadrada: {raiz} \n Elevado ao quadrado: {exp}')

# 05. Receba um numero inteiro e verifique se ele é par ou impar.
num = int(input('05. Digite um valor:'))
if num % 2 == 0:
    msg = "É par."
else:
    msg = "É impar."

print(msg)

# 06. Receba 2 numeros inteiros, mostre qual é o maior e a diferença entre eles.
num1 = int(input('06. Valor1: '))
num2 = int(input('Valor2: '))
maior = max(num1, num2)
dif = maior - min(num1, num2)
print(f'Maior: {maior}\nDiferença: {dif}')

# 07. Receba dois valores e mostre o maior, caso sejam iguais imprima 'Valores iguais.'
num1 = int(input('07. Valor1: '))
num2 = int(input('Valor2: '))
if num1 == num2:
    print('Valores iguais.')
else:
    print(f'{max(num1, num2)}')

# 08. Leia 2 notas entre 0.0 e 10.0 e informe a media delas, caso alguma não esteja nesse escopo, informe.
nota1 = int(input('08. nota1: '))

if 0.0 <= nota1 <= 10.0:
    nota2 = int(input('nota2: '))
    if 0.0 <= nota2 <= 10.0:
        msg = (nota1 + nota2) / 2
    else:
        msg = "Notas invalidas, favor verificar."
else:
    msg = "Notas invalidas, favor verificar."

print(msg)

# 09. Leia o salario de um trabalhador e o valor do emprestimo solicitado, caso seja menor que 20% do salaraio,
# imprima "Emprestimo concedido", caso contraio, imprima "Emprestimo não concedido".
salario = float(input('09. Valor do salario: '))
emp = float(input('Emprestimo solicitado: '))
if emp < salario * 0.2:
    msg = "Emprestimo concedido"
else:
    msg = "Emprestimo não concedido"

print(msg)

# 10. Receba a altura e o sexo de uma pessoa e mostre o seu peso ideal.
altura = float(input('Digite sua altura: '))
sexo = input('Digite o sexo: ')
if 'M' or 'm' in sexo:
    pIdeal = (72.7 * altura) - 58
else:
    pIdeal = (62.1 * altura) - 44.7

print(f'Seu peso ideal é {pIdeal}')
