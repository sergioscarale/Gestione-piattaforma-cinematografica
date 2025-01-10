from collections import Counter

def calcolaStatistiche(catalogo):
    if not catalogo:
        print("Il catalogo è vuoto. Nessuna statistica disponibile.")
        return

    numero_film = sum(1 for record in catalogo if record['tipo'] == "film")
    numero_serie_tv = sum(1 for record in catalogo if record['tipo'] == "serie tv")
    print(f"Numero totale di film: {numero_film}")
    print(f"Numero totale di serie TV: {numero_serie_tv}")

    tutti_generi = [genere for record in catalogo for genere in record['genere']]
    if tutti_generi:
        genere_piu_comune = Counter(tutti_generi).most_common(1)[0][0]
        print(f"Genere più comune: {genere_piu_comune}")
    else:
        print("Nessun genere presente nel catalogo.")

    durate_film = [record['durata'] for record in catalogo if record['tipo'] == "film" and record['durata'] is not None]
    episodi_serie = [record['episodi'] for record in catalogo if record['tipo'] == "serie tv" and record['episodi'] is not None]

    if durate_film:
        durata_media_film = sum(durate_film) / len(durate_film)
        print(f"Durata media dei film: {durata_media_film:.2f} minuti")
    else:
        print("Nessun dato sulla durata dei film disponibile.")

    if episodi_serie:
        episodi_medi = sum(episodi_serie) / len(episodi_serie)
        print(f"Numero medio di episodi per serie TV: {episodi_medi:.2f}")
    else:
        print("Nessun dato sul numero di episodi delle serie TV disponibile.")


def menuStatistiche(catalogo):
    print("\n<--- STATISTICHE --->\n")
    calcolaStatistiche(catalogo)
