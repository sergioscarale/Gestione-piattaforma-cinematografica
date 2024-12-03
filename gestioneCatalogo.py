import gestioneData
def inserimentoCatalogo(catalogo):
    titolo=input("Titolo del film o serie tv\n> ").capitalize()

    #e se appartenesse a più generi?
    genereCatalogo={'Avventura','Azione','Commedia','Fantascienza','Fantasy','Horror','Musical','Thriller','Supereroi'}
    genere=input("Inserisci il genere del film o serie tv tra: {}\n> ".format(", ".join(genereCatalogo))).lower().capitalize()
    if genere not in genereCatalogo:
        print("Genere non valido!")
        return
    
    tipo=input("Inserisci il tipo (Film o Serie TV)\n> ").lower()
    if tipo not in {"film","serie tv"}:
        print("puoi inserire solo film o serie tv!")
        return
    
    durata=None
    episodi=None
    if(tipo=="film"):
        try:
            #fai un controllo per i minuti
            durata=input(f"Inserisci la durata del film {titolo} in minuti.\n> ")
        except ValueError:
            print("inserisci una durata valida!")
    elif(tipo=="serie tv"):
        try:
            episodi=int(input(f"Quanti episodi ha la serie {titolo}?\n> "))
        except ValueError:
            print("inserisci un numero di episodi valido!")

    data_modifica=data_inserimento=gestioneData.dataInsMod().strftime("%Y-%m-%d")

    #impostiamo a 0?
    visualizzazioni=0

    record={
        'titolo': titolo,
        'genere': genere,
        'tipo': tipo,
        'durata': durata,
        'episodi': episodi,
        'data_inserimento': data_inserimento,
        'data_modifica': data_modifica,
        'visualizzazioni': visualizzazioni
    }
    catalogo.append(record)
    print(f"Perfetto!\nHai inserito correttamente {titolo} al catalogo!")

def modificaCatalogo():
    print("ciao")

def eliminaCatalogo():
    print("ciao")    

def printCatalogo(catalogo):
    print("\n<--- PRINT CATALOGO --->\n")
    for record in catalogo:
        for chiave in record:
            print(f"{chiave}: {record[chiave]}")

def main():
    catalogo=[]
    scelta=1
    while scelta!=0:
        print("0 - Esci")
        print("1 - Inserisci film o serie TV")
        print("2 - Modifica contenuto")
        print("3 - Rimuovi contenuto")
        print("4 - Print catalogo")
        scelta=int(input("\n> "))
        match(scelta):
            case 0: print("ciao ciao")
            case 1: inserimentoCatalogo(catalogo)
            case 2: modificaCatalogo()
            case 3: eliminaCatalogo()
            case 4: printCatalogo(catalogo)
            case __: print("errore!")

if(__name__=="__main__"):
    main()