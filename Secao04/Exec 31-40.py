import math

# 31. Leia um numero inteiro e imprima seu antecessor e seu sucessor.
num = int(input('Digite o valor: '))
print(f'{num -1} e {num + 1}')

# 32. Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
num = int(input('Digite o valor: '))
soma = (num * 3 + 1) + (num * 2 - 1)
print(f'Soma: {soma}')

# 33. Leia o tamanha do lado do quadrado e imprima sua area.
lado = int(input('Lado do quadrado: '))
area = lado ** 2
print(f'Quadrado de lado {lado} tem {area} de area')

# 34. Leia o valor do raio de um circulo e imprima sua area.
raio = int(input('Digite o valor do raio: '))
area = 3.14 * raio ** 2
print(f'Circunferencia de raio {raio} tem area {area}')

# 35. Obtenha os valores dos catetos e descubra o tamanho da hipotenusa de um triangulo retangulo
catetoA, catetoB = float(input('Cateto A: ')), float(input('Cateto B: '))
hipotenusa = math.sqrt(catetoA ** 2 + catetoB ** 2)
print(f'Um triangulo retangulo de lados {catetoA} e {catetoB} tem hipotenusa {hipotenusa}')

# 36. Leia a ltura e o raio de um cilindro circular e calcule seu volume.
raio = int(input('Digite o valor do raio: '))
altura = int(input('Digite o valor da altura: '))
pi = 3.141592
volume = pi * altura * raio ** 2
print(f'Volume do cilindro: {volume}')

# 37. Leia o valor de um produto e apresente o valor final com desconto de 12%
prod = float(input('Digite o valor do produto: '))
desc = 0.12
valorFinal = prod * (1 - desc)
print(f'Valor final: {valorFinal}')

# 38. leia o valor do salario de um funcionario e calcule seu novo salario, sabendo que ele recebeu um aumento de 25%
salario = float(input('Digite o valor do salario: '))
aumento = 0.25
novoSalario = salario * (1 + aumento)
print(f'O funcionario passará a receber R${novoSalario}')

# 39. A importancia de R$780_000.00 sera dividida entre 3 ganhadores. O primeiro ficara com 46%, o segundo com 32% e
# o terceiro com o restante.
impotancia = 780_000.00
primeiro = impotancia * 0.46
segundo = impotancia * 0.32
terceiro = impotancia - primeiro - segundo
print(f'O primeiro receberá R${primeiro}; o segundo R${segundo} e o terceiro com R${terceiro}')

# 40. Uma empresa contrata um encanador a R$30.00 por dia. Solicite a quantidade de dias trabalhados e imprima a
# quantia liquida que devará ser paga, sabendo-se que são descontados 08% de imposto de renda.
dias = int(input('Quantos dias foram trabalhados? '))
diaria = 30.00
imposto = 0.08
pagamento = dias * diaria * (1 - imposto)
print(f'Ao final de {dias} o encanador receberá R${pagamento}')