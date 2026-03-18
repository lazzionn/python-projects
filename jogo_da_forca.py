# jogo da forca feito por lazaro
erros = 0
acertos = 0
jogadas = 0
resposta_final = ''
palavra_secreta = 'cadeira'
#                 #0123456
r2 = ''
limite_jogadas = 15

while resposta_final != palavra_secreta:
    
    r1 = input("Digite uma letra ou a palavra secreta: ")
    
    # pra verificar entrada
    if jogadas > (limite_jogadas - 1):
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
            continue
    
    if len(r1) <= 0:
        print("Digite no minimo uma letra!")
        continue
    
    if len(r1) > 1 and r1 != palavra_secreta:
        print("Você errou a palavra secreta")
        sair = input("Deseja recomeçar? [sim]/[nao] ").lower().startswith("n")
                
        if sair is True:
            break
        else:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            continue
        
    if r1.isdigit():
        print("Por favor, digite apenas letras!")
        
        sair = input("Deseja recomeçar? [sim]/[nao] ").lower().startswith("n")
                
        if sair is True:
            break
        else:
            resposta_final = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            continue 
        

    ###############
    
    if r1 == palavra_secreta:
        acertos += 1
        print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acertos} acertos!\nA palavra era {palavra_secreta.upper()}")
        sair = input("Deseja recomeçar? [sim]/[nao] ").lower().startswith("n")
        if sair is True:
            break
        else:
            resposta_final = ''
            r1 = ''
            r2 = ''
            erros = 0
            acertos = 0
            jogadas = 0
            continue
    else:
        if r1 in palavra_secreta: 
            print(f"'{r1}' está na palavra secreta!") 
            jogadas += 1
            acertos += 1
            print(f'Jogadas: [{jogadas}/{limite_jogadas}]')
            r2 += r1 
            resposta_final = '' 
            for letra in palavra_secreta: 
                if letra in r2: 
                    resposta_final += letra 
                else:
                    resposta_final += '*' 
            print(f'Palavra formada: {resposta_final}')
            if resposta_final == palavra_secreta:
                print(f"Parabens!  Você acertou a palavra secreta, com o total de {jogadas} jogadas, {erros} erros e {acertos} acertos!")
                sair = input("Deseja recomeçar? [sim]/[nao] ").lower().startswith("n")
                
                if sair is True:
                    break
                else:
                    resposta_final = ''
                    r2 = ''
                    erros = 0
                    acertos = 0
                    jogadas = 0
                    continue
        else: 
            print(f"'{r1}' não está na palavra secreta!")
            jogadas += 1
            erros += 1
            print(f"Tentativa: [{jogadas}/{limite_jogadas}]")
            
            continue

print("\nAté mais! \n\n\nby: Lazz")
