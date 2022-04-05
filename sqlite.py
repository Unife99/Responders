#!/usr/bin/env python3
# encoding: utf-8


from cortexutils.responder import Responder
import sqlite3

class Sqlite(Responder):
    def __init__(self):
        Responder.__init__(self)

    def run(self):
        Responder.run(self)
        
        hash = self.get_param('data.hash', None, 'hash is missing')
        dat = self.get_param('data.dat', None, 'dat is missing')
        punteggio = self.get_param('data.punteggio', None, 'punteggio is missing')
        stato = self.get_param('data.stato', None, 'stato is missing')
        utente = self.get_param('utente.hash', None, 'utente is missing')
    
        
 
         #Otteniamo l'oggeto connection che permetterà di interagire con database
        connection = sqlite3.connect("Mail.db")
        #Otteniamo l'oggetto ch permetterà di popolare il nostro database
        cursor = connection.cursor()
        #Istruzione SQL che crea una tabella nel caso non esista
        cursor.execute("CREATE TABLE IF NOT EXISTS CASI (Hash TEXT, DataScansione TEXT, Pericolosità TEXT, StatoScansione TEXT, SvoltaDa TEXT)")
        #Inserisco i dati nella tabella:
        cursor.execute('INSERT INTO CASI ( Hash, DataScansione, Pericolosità, StatoScansione, SvoltaDa) VALUES ("{}","{}","{}","{}","{}")'.format( hash, dat, punteggio, stato, utente))
        connection.commit()
        #Leggo i dati inseriti nella tabella:
        for rows in  cursor.execute("SELECT * FROM CASI "):
                                                             print("DATI INSERITI:")
                                                             print(rows)
                           
if __name__ == "__main__":
    Sqlite().run()
