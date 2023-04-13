#EXERCICIO 4 - Leonardo Santos de souza - rm#94873.

print("                 SEJA BEM VINDO AO PROGRAMA "                     )
print(" ESTE PROGRAMA IRÁ GERAR SUA SENHA PARA DESBLOQUEAR O COMPUTADOR ")

minutos = int(input(" \n Por favor, coloque quantos minutos se passaram no seu computador: "))

fatorial = 1
count = 1

if minutos <= 60:

     for count in range(1, minutos + 1):

        fatorial *= count

        count = count + 1


     print(" A senha para liberar o computador é: LIBERDADE{}, ".format(fatorial))

else:

    print(" FAVOR, COLOCAR APENAS 60 MINUTOS ")