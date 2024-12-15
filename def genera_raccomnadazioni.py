def genera_raccomnadazioni(catalogo,cronologia): 
    frequenza={}

    for record in catalogo: 
        for genere in record['genere']:
            if genere in frequenza : 
                frequenza[genere] +=1 
            else: 
                frequenza[genere] =1

    print("\n<--- FREQUENZA DEI GENERI --->\n")
    for genere, frequenze in frequenza.items():
        print(f"{genere}: {frequenze}")


def analizza_generi_preferiti(catalogo,cronologia): 
    frequenza={}

    for record in catalogo: 
        for genere in record['genere']:
            if genere in frequenza : 
                frequenza[genere] +=1 
            else: 
                frequenza[genere] =1

    if frequenza: 
        genere_maggiore=max(frequenza,key=frequenza.get)
        print(f"\nIl genere più frequente è: {genere_maggiore} ({frequenza[genere_maggiore]} volte)")
    else:
        print("\nIl catalogo è vuoto, nessun genere trovato.")