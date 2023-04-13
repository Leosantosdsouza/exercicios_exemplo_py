#Verificação de batimento cardiaco.

idade = int(input(" Digite sua idade "))
batimento = float(input(" Digite seus batimentos cardiacos (BPM) "))

#RECÉM NASCIDO.

if ((idade > 0) and (idade <= 2)):

    print(" Idade dentro da tabela bpm ")

    if ((batimento >= 120) and (batimento <= 140)):

        print(" valor de batimento dentro do padrão")

    else:

        if (batimento < 120):

            print(" Valor abaixo  da faixa adequada ")

        else:

            if (batimento > 140):

                print(" Valor acima da faixa adequada ")

            else:

                print(" valor fora da faixa adequada ")

else:

#CRIANÇA PARA ADOLESCENTE.

    if ((idade >= 8) and (idade <= 17)):

        print(" Idade dentro da tabela bpm ")

        if ((batimento >= 80) and (batimento <= 100)):

            print(" valor de batimento dentro do padrão")

        else:

            if (batimento < 80):

                print(" Valor abaixo  da faixa adequada ")

            else:

                if (batimento > 100):

                    print(" Valor acima da faixa adequada ")

                else:

                    print(" valor fora da faixa adequada ")

    else:

#ADULTO SEDENTARIO

        if ((idade >= 18) and (idade <= 60)):

            print(" Idade dentro da tabela bpm ")

            if ((batimento >= 70) and (batimento <= 80)):

                print(" valor de batimento dentro do padrão")

            else:

                if (batimento < 70):

                    print(" Valor abaixo  da faixa adequada ")

                else:

                    if (batimento > 80):

                        print(" Valor acima da faixa adequada ")

                    else:

                        print(" valor fora da faixa adequada ")

        else:

#IDOSO.

            if ((idade >= 61) and (idade <= 100)):

                print(" Idade dentro da tabela bpm ")

                if ((batimento >= 50) and (batimento <= 60)):

                    print(" valor de batimento dentro do padrão")

                else:

                    if (batimento < 50):

                        print(" Valor abaixo  da faixa adequada ")

                    else:

                        if (batimento > 60):

                            print(" Valor acima da faixa adequada ")

                        else:

                            print(" valor fora da faixa adequada ")

            else:

                print(" Condições fora da tabela, por favor informe a idade corretamente. ")