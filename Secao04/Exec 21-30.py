# 21. Leia o valor de massa el libras e apresente-o em quilogramas.
libras = float(input('21. Digite o valor da massa: '))
kg = libras * 0.45
print(f'{libras}libras é equivalente a {kg}kg')

# 22. Leia o valor de comprimento em jardas e apresente-o em metros.
jardas = float(input('Digite o comprimento: '))
metros = jardas * 0.91
print(f'{jardas}jardas é equivalente a {metros}m')

# 23. Leia o valor de comprimento em metros e apresente-o em jardas.
metros = float(input('Digite o comprimento: '))
jardas = jardas / 0.91
print(f'{metros}m é equivalente a {jardas}jardas')

# 24. Leia um valor em metros quadrados  e apresente-o em acres.
m2 = float(input('Digite o valor da area: '))
acres = m2 * 0.000247
print(f'{m2}m2 é equivalente a {acres}acres')

# 25. Leia o valor em acres e apresente-o em metros quadrados.
acres = float(input('Digite o valor da area: '))
m2 = acres * 4048.58
print(f'{acres}acres é equivalente a {m2}m2')

# 26.Leia o valor da area em metros quadrados e apresente-o em hectares.
m2 = float(input('Digite o valor da area: '))
hec = m2 * 0.0001
print(f'{m2}m2 é equivalente a {hec}hectares')

# 27. Leia o valor de area em hectares e apresente-o para metros quadrados.
hec = float(input('Digite o valor da area: '))
m2 = hec * 1000
print(f'{hec}hectares é equivalente a {m2}m2')

# 28. Faça a leitura de 3valores e apresente como resultado a soma dos 3 valores ao quadrado
num1, num2, num3 = int(input('Valor1: ')), int(input('Valor2: ')), int(input('Valor3: '))
valor1, valor2, valor3 = num1 ** 2, num2 ** 2, num3 ** 2
soma = valor1 + valor2 + valor3
print(f'Resultado: {soma}')

# 29. Leia quatro notas e imprima a media aritmetica das mesmas.
nota1, nota2, nota3, nota4 = int(input('Nota1:')), int(input('Nota2:')), int(input('Nota3:')), int(input('Nota4:'))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Média: {media}')

# 30. Leia o valor em real da cotação do dolar
cotacao = float(input('Qual a cotação atual do USD? '))
real = float(input('Qual o valor a ser convertido? '))
dolar = real / cotacao
print(f'R${real} esta valendo US${dolar}')
