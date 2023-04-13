#EXERCICIO 2 - Leonardo Santos de souza - rm#94873.

print(" \n Seja bem vindo, para o aplicativo que vai decidir por votação, qual dia melhor para as lives! ")

voto1 = input(" \n Voto 1 - Favor escolher 1 opção entre os 5 dias da semana: (SEGUNDA, TERÇA, QUARTA, QUINTA, SEXTA): ")
voto2 = input(" Voto 2 - Favor escolher 1 opção entre os 5 dias da semana: (SEGUNDA, TERÇA, QUARTA, QUINTA, SEXTA): ")
voto3 = input(" Voto 3 - Favor escolher 1 opção entre os 5 dias da semana: (SEGUNDA, TERÇA, QUARTA, QUINTA, SEXTA): ")
voto4 = input(" Voto 4 - Favor escolher 1 opção entre os 5 dias da semana: (SEGUNDA, TERÇA, QUARTA, QUINTA, SEXTA): ")
voto5 = input(" Voto 5 - Favor escolher 1 opção entre os 5 dias da semana: (SEGUNDA, TERÇA, QUARTA, QUINTA, SEXTA): ")

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

# VOTO 1:

if voto1.upper() == "SEGUNDA":
    segunda = segunda + 1

elif voto1.upper() == "TERÇA":
        terca = terca + 1

elif voto1.upper() == "QUARTA":
        quarta = quarta + 1

elif voto1.upper() == "QUINTA":
        quinta = quinta + 1

elif voto1.upper() == "SEXTA":
        sexta = sexta + 1

else:

    print(" Erro na escolha, favor escolher a opção correta. ")

# -----------------------------------------------------------------------------------------------------------------------
# VOTO 2:

if voto2.upper() == "SEGUNDA":
    segunda = segunda + 1

elif voto2.upper() == "TERÇA":
    terca = terca + 1

elif voto2.upper() == "QUARTA":
    quarta = quarta + 1

elif voto2.upper() == "QUINTA":
    quinta = quinta + 1

elif voto2.upper() == "SEXTA":
    sexta = sexta + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ----------------------------------------------------------------------------------------------------------------------
# VOTO 3:

if voto3.upper() == "SEGUNDA":
    segunda = segunda + 1

elif voto3.upper() == "TERÇA":
    terca = terca + 1

elif voto3.upper() == "QUARTA":
    quarta = quarta + 1

elif voto3.upper() == "QUINTA":
    quinta = quinta + 1

elif voto3.upper() == "SEXTA":
    sexta = sexta + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ---------------------------------------------------------------------------------------------------------------------
# VOTO 4:

if voto4.upper() == "SEGUNDA":
    segunda = segunda + 1

elif voto4.upper() == "TERÇA":
    terca = terca + 1

elif voto4.upper() == "QUARTA":
    quarta = quarta + 1

elif voto4.upper() == "QUINTA":
    quinta = quinta + 1

elif voto4.upper() == "SEXTA":
    sexta = sexta + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ---------------------------------------------------------------------------------------------------------------------
# VOTO 5:

if voto5.upper() == "SEGUNDA":
    segunda = segunda + 1

elif voto5.upper() == "TERÇA":
    terca = terca + 1

elif voto5.upper() == "QUARTA":
    quarta = quarta + 1

elif voto5.upper() == "QUINTA":
    quinta = quinta + 1

elif voto5.upper() == "SEXTA":
    sexta = sexta + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ---------------------------------------------------------------------------------------------------------------------
# VENCEDOR:

#SEDUNDA:
if ((segunda > terca) and (segunda > quarta) and (segunda > quinta) and (segunda > sexta)):
    print(" \n O vencedor foi o SEGUNDA.")
    print(" Quantidade de votos: SEGUNDA: {} TERÇA: {} QUARTA: {} QUINTA: {} SEXTA: {}.".format(segunda, terca, quarta, quinta, sexta))

#TERÇA:
elif ((terca > segunda) and (terca > quarta) and (terca > quinta) and (terca > sexta)):
    print(" \n O vencedor foi o TERÇA.")
    print(" Quantidade de votos: SEGUNDA: {} TERÇA: {} QUARTA: {} QUINTA: {} SEXTA: {}.".format(segunda, terca, quarta, quinta, sexta))

#QUARTA:
elif ((quarta > segunda) and (quarta > terca) and (quarta > quinta) and (quarta > sexta)):
    print(" \n O vencedor foi o QUARTA.")
    print(" Quantidade de votos: SEGUNDA: {} TERÇA: {} QUARTA: {} QUINTA: {} SEXTA: {}.".format(segunda, terca, quarta, quinta, sexta))

#QUINTA:
elif ((quinta > segunda) and (quinta > terca) and (quinta > quarta) and (quinta > sexta)):
    print(" \n O vencedor foi o QUINTA.")
    print(" Quantidade de votos: SEGUNDA: {} TERÇA: {} QUARTA: {} QUINTA: {} SEXTA: {}.".format(segunda, terca, quarta, quinta, sexta))

#SEXTA:
elif ((sexta > segunda) and (sexta > terca) and (sexta > quarta) and (sexta > quinta)):
    print(" \n O vencedor foi o SEXTA.")
    print(" Quantidade de votos: SEGUNDA: {} TERÇA: {} QUARTA: {} QUINTA: {} SEXTA: {}.".format(segunda, terca, quarta, quinta, sexta))

else:
    print(" \n votos empatados, favor refazer a votação")
