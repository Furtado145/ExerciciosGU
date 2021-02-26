import math

# 11. Receba um valor e imprima asoma de seus algarismos, Caso o numero dado seja negativo, informe "Valor invalido."

num = int(input('11. Digite um valor: '))
soma, cad = 0
resto = num // (10**cad) % 10
if num > 0:
    while resto > 0:
        resto = num // (10**cad) % 10
        cad += 1
        soma += resto

    print(soma)
else:
    print('Valor invalido.')

# 12. Leia um numero inteiro, se o valor for negativo, informe "Valor invalido", caso seja positivo imprima o
# logaritmo deste numero.
num = int(input('11. Digite um valor: '))
if num > 0:
    msg = math.log(num)
else:
    msg = "Valor invalido"

print(msg)

# 13. Leia a media ponderada das notas de 3 provas, sabendo que a prova 1 e 2 tem peso 1, e a prova 3 tem peso 2.
# Inform se o aluno foi aprovado, tendo eo vista que a media para aprovação é de 60pontos.
nota1 = int(input('Nota 1:'))
nota2 = int(input('Nota 2:'))
nota3 = int(input('Nota 3:')) * 2
media = (nota1 + nota2 + nota3) / 4
if media >= 60:
    msg = 'Aprovado.'
else:
    msg = 'Reprovado.'

print(msg)

# 14. 