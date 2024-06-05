def menu_principal():
    print("/n**Calculadora de Conversão de Unidades**")
    print("1. Conveter Comprimento")
    print("3. Sair")

    opcao = input("Digite a opção desejada: ")
    return opcao

def sair():
    print('Encerrando o programado...')

    escolha = menu_principal()

    if escolha == '3':
        sair()