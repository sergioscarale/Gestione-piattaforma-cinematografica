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

    data_modifica=data_inserimento=gestioneData.dataInsMod().strftime("%Y-%m-%d")

    visualizzazioni=0

    record={
        'titolo': titolo,
        'genere': genere, #print se ci sono più generi?
        'tipo': tipo,
        'durata': durata,
        'episodi': episodi,
        'data_inserimento': data_inserimento,
        'data_modifica': data_modifica,
        'visualizzazioni': visualizzazioni
    }
    catalogo.append(record)
    print(f"Perfetto!\nHai inserito correttamente {titolo} al catalogo!")

def modificaCatalogo(catalogo):
    #rivedi
    print("<--- MODIFICA CATALOGO --->\n")
    nTitolo=input("Quale titolo si vuole modificare?").lower().capitalize()
    for record in catalogo:
        for chiave in record:
            if(chiave['titolo']==nTitolo):
                chiave['titolo']=nTitolo
                #meglio fare un menù o continuare così?

def eliminaCatalogo(catalogo):
    #rivedi
    print("<--- ELIMINA ELEMENTO DAL CATALOGO --->\n")
    nTitolo=input("Quale titolo vuoi cancellare?").lower().capitalize()
    for record in catalogo:
        for chiave in record:
            if(chiave==nTitolo):
                record.popitem()

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
            case 2: modificaCatalogo(catalogo)
            case 3: eliminaCatalogo(catalogo)
            case 4: printCatalogo(catalogo)
            case __: print("errore!")

if(__name__=="__main__"):
    main()