# jogo da forca feito por lazaro
import random
import os

erros = 0
acertos = 0
jogadas = 0
resposta_final = ''
acerto_direto = 0

#                 #0123456
r2 = ''
limite_erros = 8
base_palavras = ['cachorro', 'bicicleta', 'picole', 'maça', 'computador', 'fazenda', 'borboleta', 'trabalho', 'escola', 'carro', 'motor']
palavra_secreta = random.choice(base_palavras)
while resposta_final != palavra_secreta:
    
    r1 = input("Digite uma letra ou a palavra secreta: ")
    
    # pra verificar entrada
    if erros > (limite_erros - 1):
        os.system('clear')
        print("Acabou suas tentativas! ")
        sair = input("Deseja recomeçar? [sim]/[nao] ").lower().startswith("n")
        if sair is True:
            break
        else:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
    
    if len(r1) <= 0:
        print("Digite no minimo uma letra!")
        continue
    
    if len(r1) > 1 and r1 != palavra_secreta:
        os.system('clear')
        print("Você errou a palavra secreta")
        sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("n")
                
        if sair is True:
            break
        else:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        
    if r1.isdigit():
        os.system('clear')
        print("Por favor, digite apenas letras!")
        
        sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("n")
                
        if sair is True:
            break
        else:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue 
        

    ###############
    
    if r1 == palavra_secreta:
        os.system('clear')
        acerto_direto += 1
        print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acerto_direto} acerto direto!\nA palavra era {palavra_secreta.upper()}")
        sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("n")
        if sair is True:
            break
        else:
            resposta_final = ''
            r1 = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
    else:
        if r1 in palavra_secreta: 
            print(f"'{r1}' está na palavra secreta!") 
            jogadas += 1
            acertos += 1
            print(f"Tentativas: {jogadas}")
            print(f"Erros: [{erros}/{limite_erros}]")
            
            r2 += r1 
            resposta_final = '' 
            for letra in palavra_secreta: 
                if letra in r2: 
                    resposta_final += letra 
                else:
                    resposta_final += '*' 
            print(f'Palavra formada: {resposta_final}')
            if resposta_final == palavra_secreta:
                os.system('clear')
                print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acertos} acertos!")
                sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("n")
                
                if sair is True:
                    break
                else:
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    palavra_secreta = random.choice(base_palavras)
                    continue
        else: 
            print(f"'{r1}' não está na palavra secreta!")
            jogadas += 1
            erros += 1
            print(f"Tentativas: {jogadas}")
            print(f"Erros: [{erros}/{limite_erros}]")
            
            continue

print("\nAté mais! \n\n\nby: Lazz")
