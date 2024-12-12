from gestioneCatalogo import * 
def menu():
    catalogo=[]
    while True:
        print("\n<--- MENU PRINCIPALE --->")
        print("0 - Esci")
        print("1 - Inserisci film o serie TV")
        print("2 - Modifica contenuto")
        print("3 - Rimuovi contenuto")
        print("4 - Stampa catalogo")
        
        try:
            scelta = int(input("\n> "))
        except ValueError:
            print("Inserisci un numero valido!")
            continue

        match scelta:
            case 0:
                print("Uscita dal programma. Ciao!")
                break
            case 1:
                inserimentoCatalogo(catalogo)
            case 2:
                menuModificaCatalogo(catalogo)
            case 3:
                eliminaCatalogo(catalogo)
            case 4:
                printCatalogo(catalogo)
            case _:
                print("Errore! Scegli un'opzione valida.")

if __name__ == "__main__":
    menu()
