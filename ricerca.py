def ricercaPerGenere(catalogo, genere):
    risultati = [record for record in catalogo if genere in record['genere']]
    if risultati:
        print(f"\nRisultati per il genere '{genere}':")
        for record in risultati:
            print(f"- {record['titolo']} ({record['tipo']})")
    else:
        print(f"\nNessun risultato trovato per il genere '{genere}'.")


def ricercaPerProtagonista(catalogo, protagonista):
    risultati = [record for record in catalogo if protagonista.lower() in record['protagonista'].lower()]
    if risultati:
        print(f"\nRisultati per il protagonista '{protagonista}':")
        for record in risultati:
            print(f"- {record['titolo']} ({record['tipo']})")
    else:
        print(f"\nNessun risultato trovato per il protagonista '{protagonista}'.")


def ricercaPerAnno(catalogo, anno):
    risultati = [record for record in catalogo if record['data_uscita'].year == anno]
    if risultati:
        print(f"\nRisultati per l'anno {anno}:")
        for record in risultati:
            print(f"- {record['titolo']} ({record['tipo']})")
    else:
        print(f"\nNessun risultato trovato per l'anno {anno}.")


def menuRicerca(catalogo):
    print("\n<--- MENU RICERCA --->\n")
    while True:
        print("0 - Torna al menu principale")
        print("1 - Ricerca per genere")
        print("2 - Ricerca per protagonista")
        print("3 - Ricerca per anno di uscita")
        scelta = input("> ")

        match scelta:
            case "0":
                break
            case "1":
                genere = input("Inserisci il genere da cercare: ").capitalize()
                ricercaPerGenere(catalogo, genere)
            case "2":
                protagonista = input("Inserisci il nome del protagonista: ")
                ricercaPerProtagonista(catalogo, protagonista)
            case "3":
                try:
                    anno = int(input("Inserisci l'anno di uscita (formato AAAA): "))
                    ricercaPerAnno(catalogo, anno)
                except ValueError:
                    print("Inserisci un anno valido!")
            case _:
                print("Scelta non valida! Riprovare.")
