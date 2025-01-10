from gestioneCatalogo import *
from catalogo import *
from ricerca import menuRicerca 
from statistiche import menuStatistiche
from genera_raccomandazioni import genera_raccomandazioni, analizza_generi_preferiti

def main():
    catalogo=[]
    scelta=1
    while scelta!=0:
        print("\n<--- MENU PRINCIPALE --->")
        print("0 - Esci")
        print("1 - Inserisci film o serie TV")
        print("2 - Modifica contenuto")
        print("3 - Rimuovi contenuto")
        print("4 - Print catalogo")
        print("5 - Ricerca nel catalogo")
        print("6 - Visualizza statistiche")
        print("7 - Genera raccomandazioni")
        print("8 - Analizza generi preferiti")
        
        try:
            scelta=int(input("\n> "))
        except ValueError:
            print("Inserisci un numero valido!")
            continue

        match scelta:
            case 0:
                print("Ciao ciao!")
            case 1:
                inserimentoCatalogo(catalogo)
            case 2:
                menuModificaCatalogo(catalogo)
            case 3:
                eliminaCatalogo(catalogo)
            case 4:
                printCatalogo(catalogo)
            case 5:  
                menuRicerca(catalogo)
            case 6:  
                menuStatistiche(catalogo)
            case 7:
                genera_raccomandazioni(catalogo)
            case 8:
                analizza_generi_preferiti(catalogo)
            case __:
                print("Errore! Opzione non valida.")

if __name__ == "__main__":
    main()