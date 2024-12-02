def inserimentoCatalogo():
    titolo=input("Titolo del film o serie tv\n> ")
    genereCatalogo={'Avventura','Azione','Commedia','Fantascienza','Fantasy','Horror','Musical','Thriller','Supereroi'}
    genere=input("Inserisci il genere del film o serie tv tra: {}\n> ".format(", ".join(genereCatalogo))).lower()
    controllo=False
    for var in genereCatalogo:
        if(var.lower()==genere):
            controllo=True
    if not controllo:
        return
    print("ciao")

def modificaCatalogo():
    print("ciao")

def eliminaCatalogo():
    print("ciao")    

def main():
    scelta=1
    while scelta!=0:
        print("0 - Esci")
        print("1 - Inserisci film o serie TV")
        print("2 - Modifica contenuto")
        print("3 - Rimuovi contenuto")
        scelta=int(input("\n> "))
        match(scelta):
            case 1: inserimentoCatalogo()
            case 2: modificaCatalogo()
            case 3: eliminaCatalogo()
main()