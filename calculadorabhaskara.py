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

def formatar(z):
    if isinstance(z, complex):
        return f"{z.real:.2f} + {z.imag:.2f}j"
    if z == int(z):
        return int(z)
    else:
        return f"{z:.2f}"

while True:
    print((' ' * 3), 'Calculadora 2° grau')
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    if a == 0:
        print("Isso não é uma equação do segundo grau!")
        continue
    elif b == 0:
        print("Isso não é uma equação do segundo grau!")
        continue
    if c == 0:
        print("Isso não é uma equação do segundo grau!")
        continue

    delta = ((b ** 2) - (4 * a * c))
    resultado_rq_d = raiz_quadrada(delta)

    x1 = ((b * -1)+resultado_rq_d) / (2 * a)
    x2 = ((b * -1)-resultado_rq_d) / (2 * a)

    x1_r = str(x1)
    x2_r = str(x2)

    print(f"O resultado é: X¹ = {formatar(x1)} e X² = {formatar(x2)}")
    resp = input("Deseja calcular outra equação?").lower().startswith("s")

    if resp:
        continue
    else:
        break
