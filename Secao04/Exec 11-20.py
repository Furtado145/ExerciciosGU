# 11. Leia uma velocidade em m/s e apresente-a em Km/h.
ms = float(input('11. Digite a velocidade: '))
kmh = ms * 3.6
print(f'{ms}m/s é igual a {kmh}Km/h')

# 12. Leia a distancia em Milhas e apresente-a em quilometros.
milhas = float(input('12. Digite a distancia: '))
km = milhas * 1.61
print(f'{milhas} milhas é igual a {km} quilometros.')

# 13. Leia uma distancia em quilometros e converta-a em milhas.
km = float(input('13. Digite a distancia: '))
milhas = km / 1.61
print(f'{km}km é igual a {milhas}milhas')

# 14. Leia um angulo em graus e apresente-o em radianos.
graus = float(input('14. Digite o angulo: '))
pi = 3.14
radianos = (graus * pi) / 180
print(f'{graus}º é igual a {radianos} radianos')

# 15. Leia um angulo em radianos e apresente-o em graus.
radianos = float(input('15. Digite o angulo: '))
pi = 3.14
graus = (radianos * 180) / pi
print(f'{radianos} radianos é igual a {graus}º')

# 16. Leia o comprimento em polegads em apresente-o em centimetros.
inch = float(input('16. Digite o comprimento: '))
cm = inch * 2.54
print(f'{inch} polegadas é igual a {cm}cm.')

# 17. Leia o comprimento em centimetros e apresente-o em polegadas.
cm = float(input('17. Digite o comprimento: '))
inch = cm / 2.54
print(f'{cm}cm é igual a {inch} polegadas.')

# 18. Leia o valor em volume em m3 e apresente-a em litros.
m3 = float(input('18. Digite o volume: '))
litros = m3 * 1000
print(f'{m3}m3 é igual a {litros}litros')

# 19. leia o volume em litros e apresente-o em m3.
litros = float(input('19. Digite o volume: '))
m3 = litros / 1000
print(f'{litros}litros é igual a {m3}m3')

# 20. Leia o valor de massa em Kg e apresente-o em libras.
kg = float(input('20. Digite a massa: '))
libras = kg / 0.45
print(f'{kg}Kg é igual a {libras}lib')
