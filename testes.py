nota_1 = int(input("Digite a 1ª nota: "))
nota_2 = int(input("Digite a 2ª nota: "))
nota_3 = int(input("Digite a 3ª nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:

   print("Aprovado")
elif media >= 6 and media < 7:

   print("Recuperação")
else:

   print("Reprovado")