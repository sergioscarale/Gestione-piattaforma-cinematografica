from datetime import datetime
def dataInsMod():
    return datetime.now()

def dataUscita():
    while True:
        try:
            data=input("Inserisci la data di uscita\n> ")
            formato="%Y-%m-%d"
            return datetime.strptime(data,formato).date()
        except ValueError:
            print("data non valida")
