#exercicio pratico 1.


alimentos = int(input(" Informe quantos alimentos voce ingeriu: "))

print("\n Informe a quantidade de calorias dos alimento: \n")

n = 0
total_calorias = 0.0

for x in range(0,alimentos):

    n = n + 1

    calorias = float(input(" Informe a caloria do item {} ".format(n)))

    total_calorias = calorias + total_calorias


print(" \n voce ingeriu {} alimentos. e a caloria total de todos esses alimentos é {} ".format(alimentos,total_calorias))
