pessoa = []
for x in range (3):
    sex = input(f'Qual o sexo da {x+1} pessoa (M/F): ').upper().strip()
    while sex not in 'MF':
        print('Inválido!')
        sex = input(f'Qual o sexo da {x+1} pessoa (M/F): ').upper().strip()
    pessoa.append(sex)
    
    homens = pessoa.count('M')
    mulheres = pessoa.count('F')
    print(f'Homens: {homens} \nMulheres: {mulheres}')