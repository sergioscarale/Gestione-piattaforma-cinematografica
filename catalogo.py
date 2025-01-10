from datetime import datetime,timedelta
def ottieniCatalogo():
    return []

def creaRecord(titolo,genere,tipo,durataMinuti=None,episodi=None,visualizzazioni=0,protagonista="",data_uscita=""):
    return {
        'titolo': titolo,
        'genere': genere,
        'tipo': tipo,
        'durata': timedelta(minutes=durataMinuti) if durataMinuti else None,
        'episodi': episodi,
        'data_inserimento': datetime.now().date(),
        'data_modifica': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'visualizzazioni': visualizzazioni,
        'protagonista': protagonista,
        'data_uscita': data_uscita
    }