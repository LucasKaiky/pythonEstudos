numero = int(input('Digite um número:'))
maior = 0

while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input('Digite um número:'))

print('O maior numero foi {}'.format(maior))