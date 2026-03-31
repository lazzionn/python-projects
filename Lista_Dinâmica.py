# AINDA EM CONSTRUÇÃO!!! PUBLIQUEI SÓ PRA DEIXAR SALVO AQUI
lista_compras = ['banana', 'maçã', 'ovos']

adicionar = ''
delete = ''
i = 1
opcoes = ['1', '2', '3', '4']
while True:

    print("Oque gostaria de fazer? \n [1] Adicionar um item à lista \n [2] Excluir um item da lista \n [3] Listar valores \n [4] Sair")
    r1 = input()
    i = 1
    
    if r1 in opcoes:
        if r1 == '1':
            adicionar = input("Digite oque você deseja adicionar á lista: ")
            lista_compras.append(adicionar)
            for item in lista_compras:
                print(f"{i}. {item}")
                i += 1
        elif r1 == '2':
            delete = input("Qual o número do item que você deseja remover? (Apenas número, por favor)").isdigit()
            del lista_compras[delete]
            continue
        elif r1 == '3':
            for item in lista_compras:
                print(f"\t {i}. {item.upper()}")
                i += 1
        else:
            break
    else:
        print("Escolha apenas uma das opções!")
        continue
    
