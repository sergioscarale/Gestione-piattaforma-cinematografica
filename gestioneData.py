from datetime import datetime
def dataInsMod():
    data=datetime.now()
    return data 

def dataUscita():
    data=input("Inserisci la data di uscita\n> ")
    formato="%Y-%m-%d"
    data_uscita=datetime.strptime(data,formato).date()
    return data_uscita
