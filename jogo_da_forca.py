# jogo da forca feito por lazzionn
import random
import os

erros = 0
acertos = 0
jogadas = 0
resposta_final = ''
acerto_direto = 0
r2 = ''
limite_erros = 8
base_palavras = [
    # animais
    'cachorro', 'borboleta', 'elefante', 'jacare', 'papagaio',
    'tartaruga', 'hamster', 'camaleao', 'tubarao', 'pinguim',
    
    # tecnologia
    'computador', 'teclado', 'monitor', 'impressora', 'notebook',
    'algoritmo', 'programa', 'internet', 'servidor', 'software',
    
    # objetos
    'bicicleta', 'cadeira', 'geladeira', 'televisao', 'microfone',
    'mochila', 'guarda-chuva', 'calendario', 'calculadora', 'lanterna',
    
    # natureza
    'fazenda', 'cachoeira', 'montanha', 'floresta', 'vulcao',
    'tempestade', 'arco-iris', 'deserto', 'oceano', 'peninsula',
    
    # cotidiano
    'trabalho', 'escola', 'mercado', 'restaurante', 'hospital',
    'biblioteca', 'academia', 'farmacia', 'padaria', 'aeroporto'
]
palavra_secreta = random.choice(base_palavras)
while resposta_final != palavra_secreta:
    
    r1 = input("Digite uma letra ou a palavra secreta: ")
    
    # pra verificar entrada
    
    
    if len(r1) <= 0:
        print("Digite no minimo uma letra!")
        continue
    
    if len(r1) > 1 and r1 != palavra_secreta:
        os.system('clear')
        print("Você errou a palavra secreta")
        sair = input("Deseja recomeçar o jogo? [sim]/[nao] ").lower().startswith("s")
        if sair is True:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        else:
            break
        
    if r1.isdigit():
        os.system('clear')
        print("Por favor, digite apenas letras!")
        
        sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("s")
        if sair is True:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        else:
            break
        

    ###############
    
    if r1 == palavra_secreta:
        os.system('clear')
        acerto_direto += 1
        print(f"Caramba! Você acertou a palavra secreta completa com \n{jogadas} jogadas e {erros} erro(s)!\nA palavra era {palavra_secreta.upper()}")
        sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("s")
        if sair is True:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            palavra_secreta = random.choice(base_palavras)
            continue
        else:
            break
    else:
        if r1 in palavra_secreta: 
            os.system('clear')
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
                    resposta_final += '_ ' 
            print(f'Palavra formada: {resposta_final}')
            if resposta_final == palavra_secreta:
                os.system('clear')
                print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acertos} acertos!")
                sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("s")
                if sair is True:
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    palavra_secreta = random.choice(base_palavras)
                    continue
                else:
                    break
        else: 
            os.system('clear')
            print(f"'{r1}' não está na palavra secreta!")
            print(f'Palavra formada: {resposta_final}')
            jogadas += 1
            erros += 1
            print(f"Tentativas: {jogadas}")
            print(f"Erros: [{erros}/{limite_erros}]")
            if erros > (limite_erros - 1):
                os.system('clear')
                print(f"Acabou suas tentativas! \nA palavra era {palavra_secreta.upper()}")
                sair = input("Deseja continuar? [sim]/[nao] ").lower().startswith("s")
                if sair is True:
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    palavra_secreta = random.choice(base_palavras)
                    continue
                else:
                    break
            

print("\nAté mais! \n\n\nby: lazzion")
