idade = int(input('Digite sua idade: '))

if idade >=5 and idade <=10:
    print('Infantil')
elif idade >=11 and idade <=15:
    print('Juvenil')
elif idade >=16 and idade <=20:
    print('Júnior')
elif idade >=21 and idade <=25:
    print('Profissional')
else:
    print('ERRO')