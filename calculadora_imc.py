print("    ", 21 * "-")
print(f'         Tela de Login')
print("    ", 21 * "-") 
print("  Crie um usuário e senha", end="\n")
usuario = input("  Usuario: ")
senha = input("  Senha: ")
resp = ''
print('')
print("Agora faça login: ")
us = input("  Usuario: ")
sen = input("  Senha: ")


while True:
    if (us != usuario or sen != senha):
        print("Nome de usuário ou senha inválido!")
        break
    print('')
    print(f"Seja bem-vindo {us}!")
    print('')
    print("    ----CÁLCULO DE IMC----")

    peso = float(input("  Seu peso: "))
    altura = float(input("  Sua altura: "))
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        print(f"Seu imc é de {imc:.2f}, você está abaixo do peso!")
    elif imc > 18.5 and imc < 24.9:
        print(f"Seu imc é de {imc:.2f}, você está no peso ideal!")
    elif imc > 24.9 and imc < 29.9:
        print(f"Seu imc é de {imc:.2f}, você está acima do peso ideal!")
    else:
        print(f"Seu imc é de {imc:.2f}, você está obeso!")
        
    resp = input("Deseja recomeçar? ").lower().startswith('s')
    if resp is True:
        continue
    else:
        print(f"Até mais {us}!")
        break

