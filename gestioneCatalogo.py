import gestioneData
from catalogo import *

def printGeneri(genereCatalogo):
    listaGeneri=[]
    while True:
        genere=input("Inserisci il genere del film o serie tv tra: {}\n0 per uscire!\n> ".format(", ".join(genereCatalogo))).lower().capitalize()
        if genere=="0":
            print("\nSei uscito correttamente!\n")
            break
        elif not genere:
            print("Inserisci un genere")
        elif genere in listaGeneri:
            print("Genere già inserito! Scegline un altro")
        elif genere in genereCatalogo:
            listaGeneri.append(genere)
            print("\nGenere inserito!\n")
        else:
            print("Genere non valido")
    return listaGeneri
    
def inserimentoCatalogo(catalogo):
    titolo=input("Titolo del film o serie tv\n> ").capitalize()
    if not titolo:
        print("inserisci un titolo valido")
        return

    genereCatalogo={'Avventura','Azione','Commedia','Fantascienza','Fantasy','Horror','Musical','Thriller','Supereroi'}
    genere=printGeneri(genereCatalogo)
    
    tipo=input("Inserisci il tipo (Film o Serie TV)\n> ").lower()
    if tipo not in {"film","serie tv"}:
        print("puoi inserire solo film o serie tv!")
        return
    
    durataMinuti=None
    episodi=None
    if tipo == "film":
        while True:
            try:
                durataMinuti=int(input(f"Inserisci la durata del film {titolo} in minuti.\n> "))
                if durataMinuti<=0 or durataMinuti>600:
                    print("La durata deve essere un numero positivo tra 1 e 600 minuti.")
                else:
                    break
            except ValueError:
                print("Per favore, inserisci un numero valido per la durata!")
    elif(tipo=="serie tv"):
        while True:
            try:
                episodi=int(input(f"Quanti episodi ha la serie {titolo}?\n> "))
                if episodi<=0:
                    print("Il numero degli episodi dev'essere positivo!")
                else:
                    break
            except ValueError:
                print("inserisci un numero di episodi valido!")

    protagonista=input("Inserisci il nome del protagonista\n> ")
    if not protagonista:
        print("Inserisci un protagonista valido")
        return

    data_uscita=gestioneData.dataUscita()

    data_modifica=data_inserimento=gestioneData.dataInsMod().strftime("%Y-%m-%d")
    while True:
        try:
            visualizzazioni=int(input("Inserisci il numero di visualizzazioni!\n> "))
            if(visualizzazioni<0):
                print("Il numero di visualizzazione non può essere negativo!")
            else:
                break
        except ValueError:
            print("Inserisci un numero valido!")

    record=creaRecord(titolo,set(genere),tipo,durataMinuti,episodi,visualizzazioni,protagonista,data_uscita)
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
        print("3 - Modifica il protagonista;")
        scelta=int(input("> "))
        match scelta:
            case 0: break
            case 1: modificaTitolo(catalogo)
            case 2: modificaGenere(catalogo)
            case 3: modificaProtagonista(catalogo)
            case __: print("numero non valido!")

def modificaTitolo(catalogo):
    print("<--- MODIFICA TITOLO --->\n")
    titolo=input("Quale titolo si vuole modificare?\n> ").lower().capitalize()
    for record in catalogo:
        if(record['titolo']==titolo):
            print(f"Titolo attuale: {record['titolo']}")
            nTitolo=input("Nuovo titolo > ").capitalize()
            record['titolo']=nTitolo
            record['data_modifica']=gestioneData.dataInsMod().strftime("%Y-%m-%d")
            print("Titolo modificato!")
            return
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
            record['data_modifica']=gestioneData.dataInsMod().strftime("%Y-%m-%d")
            print("Genere modificato con successo!")
            return
    print("Titolo inesistente!")

def modificaProtagonista(catalogo):
    print("<--- MODIFICA PROTAGONISTA --->\n")
    titolo=input("Di quale titolo vuoi aggiornare il protagonista? ").lower().capitalize()
    for record in catalogo:
        if record['titolo']==titolo:
            print(f"Protagonista per {titolo}: {record['protagonista']}")
            nProtagonista=input("Inserisci il nuovo protagonista\n> ")
            record['protagonista']=nProtagonista
            record['data_modifica']=gestioneData.dataInsMod().strftime("%Y-%m-%d")
            print("Protagonista aggiornato con successo!")
            return
    print("Titolo inesistente!")

def eliminaCatalogo(catalogo):
    print("<--- ELIMINA ELEMENTO DAL CATALOGO --->\n")
    titolo=input("Quale titolo vuoi cancellare?").lower().capitalize()
    for record in catalogo:
        if(record['titolo']==titolo):
                catalogo.remove(record)
                print(f"Titolo '{titolo}' rimosso!")
                return
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