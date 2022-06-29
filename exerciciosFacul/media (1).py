
def notas ():
    nota1 = float(input('Digite sua 1° nota: '))
    nota2 = float(input('Digite sua 2° nota: '))
    nota3 = float(input('Digite sua 3° nota: '))
    media = (nota1 + nota2 + nota3) / 3
    return (media)

minhamedia = notas()
print(f'A sua média foi: {minhamedia :.2f}')


if minhamedia >= 7:
    print('Aprovado!')
if minhamedia < 7: 
    print('Reprovado!')



