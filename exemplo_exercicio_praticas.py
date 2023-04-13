#EXERCICIO 1 - Leonardo Santos de souza - rm#94873.

print("      Seja bem vindo ao aplicativo de controle Multimidia para o YOUTUBE. \n ")

categoria = input(" Escolha entre as niveis desejados pelas categorias: (BASIC, SILVER, GOLD, PLATINUM) : ")


if categoria.upper() == "BASIC":

    print( " \n Selecionado a Categoria Basica: ")
    print( " INFORMAÇÕES SOBRE A PORCENTAGEM DO FATURAMENTO: 30 % sobre o faturamento. ")

    valor1 = int(input(" Favor, informar o valor do faturamento anual recebido: "))
    porcentagem1 = float(valor1) * 3.0
    bonus1 = float(valor1) - float(porcentagem1)

    print(" \n O valor total é de: {}". format(valor1))
    print(" A PORCENTAGEM do valor BASICO em cima do faturamento anual é de: {}". format(porcentagem1))
    print(" O valor a ser pago para o provedor: {}". format(bonus1))

elif categoria.upper() == "SILVER":

    print(" \n Selecionado a Categoria PRATA: ")
    print(" INFORMAÇÕES SOBRE A PORCENTAGEM DO FATURAMENTO: 20 % sobre o faturamento. ")

    valor2 = int(input(" Favor, informar o valor do faturamento anual recebido: "))
    porcentagem2 = float(valor2) * 2.0
    bonus2 = float(valor2) - float(porcentagem2)

    print(" \n O valor total é de: {}".format(valor2))
    print(" A PORCENTAGEM do valor PRATA em cima do faturamento anual é de: {}".format(porcentagem2))
    print(" O valor a ser pago para o provedor: {}". format(bonus2))

elif categoria.upper() == "GOLD":

    print(" \n Selecionado a Categoria OURO: ")
    print(" INFORMAÇÕES SOBRE A PORCENTAGEM DO FATURAMENTO: 10 % sobre o faturamento. ")

    valor3 = int(input(" Favor, informar o valor do faturamento anual recebido: "))
    porcentagem3 = float(valor3) * 1.0
    bonus3 = float(valor3) - float(porcentagem3)

    print(" \n O valor total é de: {}".format(valor3))
    print(" A PORCENTAGEM (bonus), do valor OURO em cima do faturamento anual é de: {}".format(porcentagem3))
    print(" O valor a ser pago para o provedor: {}". format(bonus3))

elif categoria.upper() == "PLATINUM":

    print(" \n Selecionado a Categoria PRATA: ")
    print(" INFORMAÇÕES SOBRE A PORCENTAGEM DO FATURAMENTO: 5 % sobre o faturamento. ")

    valor4 = int(input(" Favor, informar o valor do faturamento anual recebido: "))
    porcentagem4 = float(valor4) * 0.5
    bonus4 = float(valor4) - float(porcentagem4)

    print(" \n O valor total é de: {}".format(valor4))
    print(" A PORCENTAGEM do valor PLATINA em cima do faturamento anual é de: {}".format(porcentagem4))
    print(" O valor a ser pago para o provedor: {}". format(bonus4))

else:

    print(" Categoria incorreta, informar novamente a categoria. ")



