valor = float(input(" Coloque o valor integral da viagem: "))
categoria = int(input(" Escolha a classe da sua viagem. ( 1.economica, 2.executiva ou 3.primeira classe): "))
pessoas = int(input(" Coloque a quantidade de pessoas que irão na viagem: "))

#ECONOMICA.

if (categoria) == 1:

    print(" Categoria: ECONOMICA. ")

    if ((pessoas > 0) and (pessoas <= 2)):

        valor_desconto1 = valor * 0.3
        valor_liquido1 = valor - valor_desconto1
        valor_medio1 = valor / pessoas

        print(" Valor bruto da passagem = {}".format(valor))
        print(" Valor de desconto = {}".format(valor_desconto1))
        print(" Valor liquido da viagem = {}".format(valor_liquido1))
        print(" Valor Medio por pessoa = {}".format(valor_medio1))

    else:

        if (pessoas >= 3):

            valor_desconto2 = valor * 0.4
            valor_liquido2 = valor - valor_desconto2
            valor_medio2 = valor / pessoas

            print(" Valor bruto da passagem = {}".format(valor))
            print(" Valor de desconto = {}".format(valor_desconto2))
            print(" Valor liquido da viagem = {}".format(valor_liquido2))
            print(" Valor Medio por pessoa = {}".format(valor_medio2))

        else:

            if (pessoas >= 4):

                valor_desconto3 = valor * 0.5
                valor_liquido3 = valor - valor_desconto3
                valor_medio3 = valor / pessoas

                print(" Valor bruto da passagem = {}".format(valor))
                print(" Valor de desconto = {}".format(valor_desconto3))
                print(" Valor liquido da viagem = {}".format(valor_liquido3))
                print(" Valor Medio por pessoa = {}".format(valor_medio3))


else:

# EXECUTIVA.

    if (categoria) == 2:

        print(" Categoria: EXECUTIVA. ")

        if ((pessoas > 0) and (pessoas <= 2)):

            valor_desconto1 = valor * 0.5
            valor_liquido1 = valor - valor_desconto1
            valor_medio1 = valor / pessoas

            print(" Valor bruto da passagem = {}".format(valor))
            print(" Valor de desconto = {}".format(valor_desconto1))
            print(" Valor liquido da viagem = {}".format(valor_liquido1))
            print(" Valor Medio por pessoa = {}".format(valor_medio1))

        else:

            if (pessoas >= 3):

                valor_desconto2 = valor * 0.7
                valor_liquido2 = valor - valor_desconto2
                valor_medio2 = valor / pessoas

                print(" Valor bruto da passagem = {}".format(valor))
                print(" Valor de desconto = {}".format(valor_desconto2))
                print(" Valor liquido da viagem = {}".format(valor_liquido2))
                print(" Valor Medio por pessoa = {}".format(valor_medio2))

            else:

                if (pessoas >= 4):
                    valor_desconto3 = valor * 0.8
                    valor_liquido3 = valor - valor_desconto3
                    valor_medio3 = valor / pessoas

                    print(" Valor bruto da passagem = {}".format(valor))
                    print(" Valor de desconto = {}".format(valor_desconto3))
                    print(" Valor liquido da viagem = {}".format(valor_liquido3))
                    print(" Valor Medio por pessoa = {}".format(valor_medio3))

    else:

# PRIMEIRA CLASSE.

        if (categoria) == 3:

            print(" Categoria: PRIMEIRA CLASSE. ")

            if ((pessoas > 0) and (pessoas <= 2)):

                valor_desconto1 = valor * 1.0
                valor_liquido1 = valor - valor_desconto1
                valor_medio1 = valor / pessoas

                print(" Valor bruto da passagem = {}".format(valor))
                print(" Valor de desconto = {}".format(valor_desconto1))
                print(" Valor liquido da viagem = {}".format(valor_liquido1))
                print(" Valor Medio por pessoa = {}".format(valor_medio1))

            else:

                if (pessoas >= 3):

                    valor_desconto2 = valor * 1.5
                    valor_liquido2 = valor - valor_desconto2
                    valor_medio2 = valor / pessoas

                    print(" Valor bruto da passagem = {}".format(valor))
                    print(" Valor de desconto = {}".format(valor_desconto2))
                    print(" Valor liquido da viagem = {}".format(valor_liquido2))
                    print(" Valor Medio por pessoa = {}".format(valor_medio2))

                else:

                    if (pessoas >= 4):
                        valor_desconto3 = valor * 2.0
                        valor_liquido3 = valor - valor_desconto3
                        valor_medio3 = valor / pessoas

                        print(" Valor bruto da passagem = {}".format(valor))
                        print(" Valor de desconto = {}".format(valor_desconto3))
                        print(" Valor liquido da viagem = {}".format(valor_liquido3))
                        print(" Valor Medio por pessoa = {}".format(valor_medio3))


        else:

            print(" Categoria invalida, favor escolher uma categoria valida. ( 1.economica, 2.executiva ou 3.primeira classe). ")