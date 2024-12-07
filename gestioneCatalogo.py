import gestioneData
def printGeneri(genereCatalogo):
    listaGeneri=[]
    while True:
        genere=input("Inserisci il genere del film o serie tv tra: {}\n0 per uscire!\n> ".format(", ".join(genereCatalogo))).lower().capitalize()
        if genere in genereCatalogo:
            listaGeneri.append(genere)
            print("\ngenere inserito!\n")
        elif genere=="0":
            print("\nsei uscito correttamente!\n")
            break
    return listaGeneri
    
def inserimentoCatalogo(catalogo):
    titolo=input("Titolo del film o serie tv\n> ").capitalize()

    genereCatalogo={'Avventura','Azione','Commedia','Fantascienza','Fantasy','Horror','Musical','Thriller','Supereroi'}
    genere=printGeneri(genereCatalogo)
    
    tipo=input("Inserisci il tipo (Film o Serie TV)\n> ").lower()
    if tipo not in {"film","serie tv"}:
        print("puoi inserire solo film o serie tv!")
        return
    
    durata=None
    episodi=None
    if tipo == "film":
        while True:
            try:
                durata = int(input(f"Inserisci la durata del film {titolo} in minuti.\n> "))
                if durata <= 0 or durata > 600:
                    print("La durata deve essere un numero positivo tra 1 e 600 minuti.")
                else:
                    break
            except ValueError:

                print("Per favore, inserisci un numero valido per la durata!")
    elif(tipo=="serie tv"):
        try:
            episodi=int(input(f"Quanti episodi ha la serie {titolo}?\n> "))
        except ValueError:
            print("inserisci un numero di episodi valido!")

    protagonista=input("Inserisci il nome del protagonista\n> ")

    data_uscita=gestioneData.dataUscita()

    data_modifica=data_inserimento=gestioneData.dataInsMod().strftime("%Y-%m-%d")

    visualizzazioni=input("Inserisci il numero di visualizzazioni!\n> ")

    record={
        'titolo': titolo,
        'genere': genere, #print se ci sono più generi?
        'tipo': tipo,
        'durata': durata,
        'episodi': episodi,
        'protagonista': protagonista,
        'data_uscita' : data_uscita,
        'data_inserimento': data_inserimento,
        'data_modifica': data_modifica,
        'visualizzazioni': visualizzazioni
    }
    catalogo.append(record)
    print(f"Perfetto!\nHai inserito correttamente {titolo} al catalogo!")

def menuModificaCatalogo(catalogo):
    print("<--- MODIFICA CATALOGO --->\n")
    print("\n<--- MENU' --->")
    scelta=1
    while scelta!=0:
        print("0 - Esci")
        print("1 - Modifica titolo;")
        print("2 - Modifica genere;")
        print("3 - Modifica visualizzazioni;")
        scelta=int(input("> "))
        match scelta:
            case 0: break
            case 1: modificaTitolo(catalogo)
            case 2: modificaGenere(catalogo)
            case 3: modificaVisualizzazioni(catalogo)
            case __: print("numero non valido!")

def modificaTitolo(catalogo):
    print("<--- MODIFICA TITOLO --->\n")
    titolo=input("Quale titolo si vuole modificare?\n> ").lower().capitalize()
    nTitolo=input("Nuovo titolo > ")
    for record in catalogo:
        if(record['titolo']==titolo):
            record['titolo']=nTitolo
            print("Titolo modificato!")
            break
        else:
            print("Titolo insesistente!")

def modificaGenere(catalogo):
    print("<--- MODIFICA GENERE --->\n")
    titolo=input("Di quale titolo vuoi aggiornare il genere? ").lower().capitalize()
    for record in catalogo:
        if record['titolo']==titolo:
            print(f"Generi attuali per {titolo}: {', '.join(record['genere'])}")
            genereCatalogo={'Avventura','Azione','Commedia','Fantascienza','Fantasy','Horror','Musical','Thriller','Supereroi'}
            nuoviGeneri=printGeneri(genereCatalogo)
            record['genere']=nuoviGeneri 
            print("Genere modificato con successo!")
            break
    else:
        print("Titolo inesistente!")

def modificaVisualizzazioni(catalogo):
    print("<--- MODIFICA VISUALIZZAZIONI --->\n")
    titolo=input("Di quale titolo vuoi aggiornare il protagonista? ").lower().capitalize()
    for record in catalogo:
        if record['titolo']==titolo:
            print(f"Protagonista per {titolo}: {record['visualizzazioni']}")
            try:
                nProtagonista=input("Inserisci il nuovo protagonista\n> ")
            except ValueError():
                print("non valido!")
            record['protagonista']=nProtagonista
        else:
            print("Titolo inesistente!")

def eliminaCatalogo(catalogo):
    #rivedi
    print("<--- ELIMINA ELEMENTO DAL CATALOGO --->\n")
    titolo=input("Quale titolo vuoi cancellare?").lower().capitalize()
    for record in catalogo:
        if(record['titolo']==titolo):
                catalogo.remove(record)
                print(f"Titolo '{titolo}' rimosso!")
                break
        else:
            print("Titolo inesistente!")

def printCatalogo(catalogo):
    print("\n<--- PRINT CATALOGO --->\n")
    for record in catalogo:
        print(f"Titolo: {record['titolo']}")
        print(f"Genere: {', '.join(record['genere'])}")  
        print(f"Tipo: {record['tipo']}")
        if record['tipo'] == "film":
            print(f"Durata: {record['durata']} minuti")
        elif record['tipo'] == "serie tv":
            print(f"Episodi: {record['episodi']}")
        print(f"Data di inserimento: {record['data_inserimento']}")
        print(f"Data di modifica: {record['data_modifica']}")
        print(f"Visualizzazioni: {record['visualizzazioni']}")
       
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
            case 2: menuModificaCatalogo(catalogo)
            case 3: eliminaCatalogo(catalogo)
            case 4: printCatalogo(catalogo)
            case __: print("errore!")

if(__name__=="__main__"):
    main()