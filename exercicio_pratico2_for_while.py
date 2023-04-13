#exercicio pratico 2.

transacao = int(input(" Informe quantas transações você fez durante o dia: "))

print("\n Informe o valor de cada transação: \n")

n = 0
total_transacao = 0.0

for x in range(0,transacao):

    n = n + 1

    valor = float(input(" Informe o valor do item {}: ".format(n)))

    total_transacao = valor + total_transacao

media = total_transacao/transacao

print(" \n voce fez um total de {}$ em transações, e a media total dos valores é {}$, por transações. ".format(total_transacao,media))
