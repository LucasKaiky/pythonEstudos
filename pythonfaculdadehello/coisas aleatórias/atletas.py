atletas = []
while True:
    nome = input("Digite o nome do atleta (ou enter para encerrar o programa): ")

    if nome == "":
        break

    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0,}

    for i in range(5):

        atleta.get("saltos").append(float(input(f"Distância do {i+1}º salto: ")))

    atleta.get("saltos").sort() 
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    atleta["melhor_salto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3

    print(
        f"\nMelhor salto: {atleta.get('melhor_salto'):.1f} m"
        f"\nPior salto: {atleta.get('pior_salto'):.1f} m"
        f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n"
    )
atletas.append(atleta)



print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")