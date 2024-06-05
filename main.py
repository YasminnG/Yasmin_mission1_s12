def menu_principal():
    print("/n**Calculadora de Conversão de Unidades**")
    print("1. Conveter de Comprimento")
    print("2. converter de temperatura")
    print("3.sair ")

    opcao = input("Digite a opção desejada: ")
    return opcao


def sair():
    print('Encerrando o programado...')

escolha = menu_principal()

if escolha == '3':
        sair()
elif escolha == '2':
      from conversor_temperaturas import ConvertorTemperaturas
elif escolha == '1' : 
        from conversor_medidas import ConvertorMedidas 
