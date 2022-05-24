import pysftp as sftp
import os
import zipfile

def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])
    return print("File compresso correttamente")


# Memorizzazione nome utente nella variabile User
User = os.getlogin()

percorso_cartella = input("Inserisci il percorso della cartella da zippare: ")
nome_file = input("Inserisci il nome da dare alla cartella zippata indicando l' estensione: ")
zipped_file_path = 'C:\\Users\\'+User+'\\Desktop\\'+nome_file
zip_directory(percorso_cartella, zipped_file_path)

#Hostname = '5.182.33.178'
#Username = 'bonamattia'
#Password = 'ciao123'

Hostname = input("Inserire l'ip numerico o simbolico del server a cui si vuole inviare il backup: ")
Username = input("Inserire lo username del server a cui inviare il file (Esempio: root): ")
Password = input("Password dell'utente inserito: ")

with sftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connessione stabilita con successo...")

    # Definisce una variabile che contiene il percorso del file da inviare
    localFilePath = 'C:\\Users\\'+User+'\\Desktop\\'+nome_file
    print(localFilePath)
    # Definisco il percorso nel server in cui allocare il file,
    # in questo caso dato che si sta usando un
    # server Ubuntu la directory dell' utente sarà /home/nomeutente,
    # nel caso di Windows C:/Users/nomeutente
    remoteFilePath = '/home/bonamattia/'+nome_file

    sftp.put(localFilePath, remoteFilePath)
    print("File inviato correttamente al server")
