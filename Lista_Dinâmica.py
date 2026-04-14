#made by lazzion
import os
lista_compras = []

adicionar = ''
delete = ''
i = 1
opcoes = ['1', '2', '3', '4', '5']
nome_lista = '🛒 LISTA DE COMPRAS'
while True:

    print("Oque gostaria de fazer? \n [1] Adicionar um item à lista \n [2] Excluir um item da lista \n [3] Listar valores \n [4] Renomear lista \n [5] Sair")
    r1 = input()
    i = 1
    
    if r1 in opcoes:
        if r1 == '1':
            os.system('clear')
            adicionar = input("Digite oque você deseja adicionar á lista: ")
            lista_compras.append(adicionar)
        elif r1 == '2':
            os.system('clear')
            delete = input("Qual o número do item que você deseja remover? (Apenas número, por favor)").isdigit()
            del lista_compras[delete]
            continue
        elif r1 == '3':
            os.system('clear')
            print("\n" + "=" * 30)
            print(f"     {nome_lista}")
            print("=" * 30)
        
            if lista_compras:
                for i, item in enumerate(lista_compras, start=1):
                    print(f"{i:02d} | {item.capitalize()}")
                    print("=" * 30 + "\n")
            else:
                print("\nSua lista está vazia.\n")
        elif r1 == '4':
            print(f"Nome atual da sua lista: {nome_lista}")
            nome_lista = input("Digite o nome para substituir: ")
        else:
            break
    else:
        print("Escolha apenas uma das opções!")
        continue
print("\nAté mais!")
        print("Escolha apenas uma das opções!")
        continue
print("\nAté mais!")
