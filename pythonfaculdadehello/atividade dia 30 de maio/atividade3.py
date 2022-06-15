espectadores = []
for x in range(5):
    opiniao = int(input('Digite a sua opinião(Regular - 1 / Bom - 2 / Ótimo - 3): '))
    while opiniao not in (1,2,3):
        print('Opinião inválida!')
        opiniao = int(input('Digite a sua opinião(Regular - 1 / Bom - 2 / Ótimo - 3): '))
    espectadores.append(opiniao)
    
regular = espectadores.count(1)
bom = espectadores.count(2)
otimo = espectadores.count(3)
print(f'O número de pessoas que opinaram que o filme é regular é: {regular} \nO número de pessoas que opinaram que o filme é bom é: {bom} \nO número de pessoas que acharam o filme ótimo é: {otimo}')
        