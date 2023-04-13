voto1 = input(" Primeiro voto, escolha entre as 3 opções: playstation, xbox, nintendo: ")
voto2 = input(" Segundo voto, escolha entre as 3 opções: playstation, xbox, nintendo: ")
voto3 = input(" Terceiro voto, escolha entre as 3 opções: playstation, xbox, nintendo: ")
voto4 = input(" Quarto voto, escolha entre as 3 opções: playstation, xbox, nintendo: ")
voto5 = input(" Quinto voto, escolha entre as 3 opções: playstation, xbox, nintendo: ")

playstation = 0
xbox = 0
nintendo = 0

# VOTO 1:

if voto1 == "playstation":
    playstation = playstation + 1

elif voto1 == "xbox":
        xbox = xbox + 1

elif voto1 == "nintendo":
            nintendo = nintendo + 1

else:

    print(" Erro na escolha, favor escolher a opção correta. ")

# -----------------------------------------------------------------------------------------------------------------------
# VOTO 2:

if voto2 == "playstation":
    playstation = playstation + 1

elif voto2 == "xbox":
    xbox = xbox + 1

elif voto2 == "nintendo":
    nintendo = nintendo + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ----------------------------------------------------------------------------------------------------------------------
# VOTO 3:

if voto3 == "playstation":
    playstation = playstation + 1

elif voto3 == "xbox":
    xbox = xbox + 1

elif voto3 == "nintendo":
    nintendo = nintendo + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ---------------------------------------------------------------------------------------------------------------------
# VOTO 4:

if voto4 == "playstation":
    playstation = playstation + 1

elif voto4 == "xbox":
    xbox = xbox + 1

elif voto4 == "nintendo":
    nintendo = nintendo + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")

# ---------------------------------------------------------------------------------------------------------------------
# VOTO 5:

if voto5 == "playstation":
    playstation = playstation + 1

elif voto5 == "xbox":
    xbox = xbox + 1

elif voto5 == "nintendo":
    nintendo = nintendo + 1

else:

    print(" Erro na escolha, favor escolher a opção correta.")
# ---------------------------------------------------------------------------------------------------------------------
# Vencedor:

#PLAYSTATION:
if playstation > xbox and playstation > nintendo:
    print(" O vencedor foi o Playstation.")
    print(" Quantidade de votos: playstation: {} xbox: {} nintendo: {}.".format(playstation, xbox, nintendo))

#XBOX:
elif xbox > playstation and xbox > nintendo:
    print(" O vencedor foi o xbox.")
    print(" Quantidade de votos: playstation: {} xbox: {} nintendo: {}.".format(playstation, xbox, nintendo))

#NINTENDO:
elif nintendo > xbox and nintendo > playstation:
    print(" O vencedor foi o nintendo.")
    print(" Quantidade de votos: playstation: {} xbox: {} nintendo: {}.".format(playstation, xbox, nintendo))

else:
    print(" votos empatados, favor refazer a votação")