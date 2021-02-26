"""
# 41. Faça um programa que leia o valor da hora de trabalho (em reais) e o numero de horas trabalhadas no mes.
# Imprima o valor a ser pago ao funcionario, adicionando 10% sobre o valor calculado.
valorHora = float(input('41. Qual o valor da hora trabalhada? '))
qtdHora = int(input('Quantas horas de trabalho? '))
bonus = 1.1
totalPag = valorHora * qtdHora * bonus
print(f'O valor a ser pago será: {totalPag}')

# 42. Receba o salario-base de um funario. Sabendo-se que esse funcionario recebe 5% de gratificação e paga 7% de
# imposto. Imprima o salario final dele.
salarioBase = float(input('42. Qual o salario base? '))
gratificacao = salarioBase * 0.05
imposto = salarioBase * 0.07
salarioFinal = salarioBase + gratificacao - imposto
print(f'O funcionario receberá R${salarioFinal}')

# 43. Faça um programa de ajuda para vendedores. A partir de um valor total lido, informe:
#   - A vista: Total a pagar com 10% de desconto;
#   - Parcelado 3x sem juros, valor de cada parcela;
#   - Comissão, caso seja a vista, 5% do valor com desconto;
#   - Comissão, caso parcelado, 5% do valor total;
precoProd = float(input('43. Qual o valor do produto? '))
precoAVista = precoProd * 0.9
precoParcelado = precoProd / 3
comissaoAVista = precoAVista * 0.05
comissaoParcelado = precoProd * 0.05
print(f'Formas de pagamento:\n'
      f'    - A vista: R${precoAVista}\n'
      f'    - 3x sem juros: R${precoParcelado} cada parcela\n'
      f'Comissão do verdedor:\n'
      f'    - A vista: R${comissaoAVista}\n'
      f'    - Parcelado: R${comissaoParcelado}')

# 44. Receba a altura do degrau de uma escada e a altura que o usuraio deseja alcançar, Calcule quantos degraus o
# usuario deverá subir para alcaiçar seu objetivo.
degrau = float(input('44. Qual a altura do degrau?(em metros) '))
altura = float(input('Qual a altura que deseja alcançar?(em metros) '))
qtdDegraus = int(altura / degrau)


# 46. Faça um programa que leia um numero inteiro positivo de 3digitos(100 - 999). Gere outro numero formado pelos
# digitos invertidos do numero lido.
num = int(input("Digite um valor de 3 digitos: "))
if num < 0 or num >= 1000:
    print('Valor invalido')
else:
    novoNum = str(num)
    print(novoNum[::-1])

# 47. Leia um numero inteiro de 4digitos(1000-9999) e imprima um algarismo por linha.
num4 = int(input('Digite um valor com 4 digitos: '))

if 1000 < num4 < 10000:
    strNum4 = str(num4)

    for n in strNum4:
        print(n)
else:
    print('Valor invalido')
"""

