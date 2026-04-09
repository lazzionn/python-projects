import math
import cmath

def raiz_quadrada(numero):
    try:
        if numero >= 0:
            return math.sqrt(numero)
        else:
            return cmath.sqrt(numero)
    except (TypeError, ValueError):
        raise ValueError("Entrada inválida. Forneça um número real ou inteiro.")

print((' ' * 3), 'Calculadora 2° grau')
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))
delta = ((b ** 2) - (4 * a * c))
resultado_rq_d = raiz_quadrada(delta)
x1 = ((b * -1)+resultado_rq_d) / (2 * a)
x2 = ((b * -1)-resultado_rq_d) / (2 * a)

x1_r = str(x1)
x2_r = str(x2)

if (len(x1_r) > 3) or (len(x2_r) > 3):
    print(f'\nO resultado dessa equação de segundo grau é: {x1:.2f} e {x2:.2f}')
else:
    print(f'\nO resultado dessa equação de segundo grau é: X1 = {x1:.0f}  X2 = {x2:.0f}')
    
    
