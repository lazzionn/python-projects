
while True:
    print("Escreva uma frase para mim contar qual letra mais aparece: ")
    frase = input()
    
    if frase != str(frase):
        print("Por favor, digite uma frase sem números!")
        continue
    
    i = 0
    qtd_vezes = 0
    letra_mais_vezes = ''
    
    while i < len(frase):
        
        letra_atual = frase[i]
        qtd_vezes_atual = frase.count(letra_atual)
        
        if letra_atual == ' ':
            i += 1
            continue
        
        if qtd_vezes < qtd_vezes_atual:
            qtd_vezes = qtd_vezes_atual
            letra_mais_vezes = letra_atual
        
        i += 1
    
    print(f"A letra qua mais apareceu foi '{letra_mais_vezes}' que apareceu {qtd_vezes}x vezes")
    
    resp = input("Deseja continuar? [s]im  ").lower().startswith('s')
    if resp is False:
        break
print("Até mais!")