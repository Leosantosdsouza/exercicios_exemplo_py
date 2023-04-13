#EXERCICIO 3 - Leonardo Santos de souza - rm#94873.

x = 1
x1 = 1
x2 = 1
impar = 1
par = 0
lista1 = []
lista2 = []

print("                  DIGITE AS 50 NOTAS DOS ALUNOS                       ")
print(" \n---------------------------CUIDADO-----------------------------")
print(" \n      VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES:   \n ")

while x1 <= 25:

    n1 = float(input(" POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO: [ %s ]: " % impar))

    lista1.append(n1)

    x1 += 1

    impar = impar + 2

    media1 = sum(lista1) / len(lista1)

print(" \n---------------------------CUIDADO-----------------------------")
print(" \n      VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES:   \n ")

while x2 <= 25:

    n2 = float(input(" POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO [ %s ]: " % par))

    lista2.append(n2)

    x2 += 1

    par = par + 2

    media2 = sum(lista2) / len(lista2)

else:

    print(" \n SEGUE A BASE DE CALCULOS DAS NOTAS DOS ALUNOS")

    print(" \n O MAIOR VALOR DA TURMA IMPAR É: ")

    print(" O maior valor é: ", max(lista1))
    print(" Media {} ".format(media1))

    print(" \n O MAIOR VALOR DA TURMA PAR É: ")

    print(" O maior valor é: ", max(lista2))
    print(" Media {} ".format(media2))