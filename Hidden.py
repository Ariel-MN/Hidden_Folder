# -*- coding: utf-8 -*-
"""
todo: Documentation

    -*- A program that hide folders from Windows OS interface. -*-
    Project name: Hidden Folder
    File name: Hide
    Date created: 14/07/2019
    Date last modified: 29/01/2020
    Status: Stable
    Python version: 3.8
    Modules required: Pillow, dnspython, pymongo, cryptography
"""
__author__ = 'Ariel Montes Nogueira'
__website__ = 'http://www.montes.ml'
__email__ = 'arielmontes1989@gmail.com'

__copyright__ = 'Copyright © 2020-present Ariel Montes Nogueira'
__credits__ = []
__license__ = '''
                Licensed under the Apache License, Version 2.0 (the "License");
                you may not use this file except in compliance with the License.
                You may obtain a copy of the License at
                    http://www.apache.org/licenses/LICENSE-2.0
                Unless required by applicable law or agreed to in writing, software
                distributed under the License is distributed on an "AS IS" BASIS,
                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
                See the License for the specific language governing permissions and
                limitations under the License.'''
__recovery__ = 'https://github.com/Ariel-MN/Hidden_Folder'
__readme__ = '''HIDDEN FOLDER

A program that hide folders from Windows OS interface.


Information:

- Requirements: Windows OS


Documentation:

- https://github.com/Ariel-MN/Hidden_Folder/wiki'''
__version__ = '1.7'


from tkinter import (Listbox, PhotoImage, Scrollbar, Label, Button, Menu, Entry, messagebox, filedialog,
                     StringVar, Toplevel, VERTICAL, SUNKEN, END, Tk, N, S, E, W, NW)
from socket import setdefaulttimeout, AF_INET, SOCK_STREAM, socket as _socket
from os import system, remove, rename, mkdir
from os.path import isdir, isfile, join as join_p
from base64 import b64decode, decodebytes
from cryptography.fernet import Fernet
from PIL import ImageTk, Image as Img
from sys import exit as sys_exit
from webbrowser import open_new
from pymongo import MongoClient
from json import dumps, loads
from hashlib import sha3_512
from uuid import getnode


# Languages:
english = {
    'Guide: "How to use this program".': 'Guide: "How to use this program".',
    'UTILITY:': 'UTILITY:',
    'The usefulness of this program is to hide any folder effectively from Windows OS interface.':
        'The usefulness of this program is to hide any folder effectively from Windows OS interface.',
    'Even on USB devices, so that these folders remain hidden on different computers.':
        'Even on USB devices, so that these folders remain hidden on different computers.',
    'MENU FUNCTIONS:': 'MENU FUNCTIONS:',
    '● File > Clear All: Remove all folders from the list.':
        '● File > Clear All: Remove all folders from the list.',
    '● Edit > Hide All / Show All: All the folders in the list.':
        '● Edit > Hide All / Show All: All the folders in the list.',
    '● Backup > Activate / Deactivate: A backup of the configuration.':
        '● Backup > Activate / Deactivate: A backup of the configuration.',
    '● Backup > Save / Load: A backup of the configuration.': '● Backup > Save / Load: A backup of the configuration.',
    '● Security > Activate / Deactivate: A password access to the program.':
        '● Security > Activate / Deactivate: A password access to the program.',
    'normally the saving process is carried out automatically with each change made,':
        'normally the saving process is carried out automatically with each change made,',
    'unless it is deactivated.': 'unless it is deactivated.',
    'BUTTONS FUNCTIONS:': 'BUTTONS FUNCTIONS:',
    '● Add: Append a new folder to the list.': '● Add: Append a new folder to the list.',
    '● Delete: Remove a folder from the list.': '● Delete: Remove a folder from the list.',
    '● Hide: It will hide the folder selected in the list.': '● Hide: It will hide the folder selected in the list.',
    '● Show: It will un-hide the folder selected in the list.':
        '● Show: It will un-hide the folder selected in the list.',
    'SYMBOLS MEANING:': 'SYMBOLS MEANING:',
    'Internet connection': 'Internet connection',
    'Database connection': 'Database connection',
    'Disabled': 'Disabled',
    'Active connection': 'Active connection',
    'Absent connection': 'Absent connection',
    'REQUIREMENTS:': 'REQUIREMENTS:',
    '● OS: Windows': '● OS: Windows',
    'read more...': 'read more...',
    'Alert': 'Alert',
    'Reset the program for apply the changes.': 'Reset the program for apply the changes.',
    'All folders in the list will be permanently deleted.': 'All folders in the list will be permanently deleted.',
    'Are you sure you want to continue?': 'Are you sure you want to continue?',
    'Can not add the same directory twice.': 'Can not add the same directory twice.',
    "The inserted passwords don't match.": "The inserted passwords don't match.",
    'Incorrect password. Please try again.': 'Incorrect password. Please try again.',
    'Invalid password.': 'Invalid password.',
    'Cancel': 'Cancel',
    'Developed by:': 'Developed by:',
    'E-mail:': 'E-mail:',
    'Built on:': 'Built on:',
    'July': 'July',
    'Runtime version:': 'Runtime version:',
    'Login': 'Login',
    'password': 'password',
    'Create Password': 'Create Password',
    'new': 'new',
    'repeat': 'repeat',
    'Submit': 'Submit',
    'Folder List': 'Folder List',
    'Add': 'Add',
    'Delete': 'Delete',
    'Hide': 'Hide',
    'Show': 'Show',
    'Clear': 'Clear All',
    'Exit': 'Exit',
    'File': 'File',
    'Show All': 'Show All',
    'Hide All': 'Hide All',
    'Edit': 'Edit',
    'English': 'English',
    'Spanish': 'Spanish',
    'Italian': 'Italian',
    'Settings': 'Settings',
    'Language': 'Language',
    'Backup': 'Backup',
    'Security': 'Security',
    'Activate': 'Activate',
    'Deactivate': 'Deactivate',
    'Save Backup': 'Save Backup',
    'Load Backup': 'Load Backup',
    'Reset Password': 'Reset Password',
    '? Help': '? Help',
    'About': 'About',
    'Help': 'Help',
    'Folder hidden: ': 'Folder hidden: ',
    'Folder unhide: ': 'Folder unhide: ',
    'Folder deleted: ': 'Folder deleted: ',
    'Folder added: ': 'Folder added: ',
    'Folder not found: ': 'Folder not found: ',
    'Database': 'aGlkZW4tZm9sZGVyIGJhY2tVcDIwLQ0K',
    "Can't hide a system folder": "Can't hide a system folder",
    'All current folders will be configured as visible before emptying the list.':
        'All current folders will be configured as visible before emptying the list.',
    'Are you sure you want to load the backup right now?': 'Are you sure you want to load the backup right now?',
    'The backup has been loaded': 'The backup has been loaded',
    'The backup has been updated': 'The backup has been updated',
    'The backup has been activated': 'The backup has been activated',
    'The backup has been deactivate': 'The backup has been deactivate',
    'The backup is disabled': 'The backup is disabled',
    'The backup is empty.': 'The backup is empty.',
    'A backup has been created': 'A backup has been created',
    'Database connection failed': 'Database connection failed',
    'Could not establish a connection': 'Could not establish a connection',
    'All the folders has been hide': 'All the folders has been hide',
    'All the folders has been shown': 'All the folders has been shown',
    'All the unhide folders has been deleted': 'All the unhide folders has been deleted',
    "The folder is hide, it can't be deleted": "The folder is hide, it can't be deleted",
    'You must select a folder to hide': 'You must select a folder to hide',
    'You must select a folder to show': 'You must select a folder to show',
    'You must select a folder to delete': 'You must select a folder to delete',
    'A new config file has been made': 'A new config file has been made',
    'There are no folders to delete': 'There are no folders to delete',
    'There are no folders to hide': 'There are no folders to hide',
    'There are no folders to show': 'There are no folders to show'}
spanish = {
    'Guide: "How to use this program".': 'Guía: "Como usar este programa".',
    'UTILITY:': 'UTILIDAD:',
    'The usefulness of this program is to hide any folder effectively from Windows OS interface.':
        'La utilidad de este programa es ocultar cualquier carpeta de la interfaz de Windows OS.',
    'Even on USB devices, so that these folders remain hidden on different computers.':
        'Incluso en dispositivos USB, de modo que estas carpetas permanecen ocultas en diferentes computadoras.',
    'MENU FUNCTIONS:': 'FUNCIONES DE MENU:',
    '● File > Clear All: Remove all folders from the list.':
        '● Archivo > Borrar Todo: Borra todas las carpetas de la lista.',
    '● Edit > Hide All / Show All: All the folders in the list.':
        '● Editar > Ocultar Todo / Mostrar Todo: Todas las carpetas de la lista.',
    '● Backup > Activate / Deactivate: A backup of the configuration.':
        '● Respaldo > Activar / Desactivar: La copia de seguridad de la configuración.',
    '● Backup > Save / Load: A backup of the configuration.':
        '● Respaldo > Salvar / Cargar: La copia de seguridad de la configuración.',
    '● Security > Activate / Deactivate: A password access to the program.':
        '● Seguridad > Activar / Desactivar: El acceso con contraseña al programa.',
    'BUTTONS FUNCTIONS:': 'FUNCIONES DE BOTONES:',
    '● Add: Append a new folder to the list.': '● Agregar: Agrega una nueva carpeta a la lista.',
    '● Delete: Remove a folder from the list.': '● Eliminar: Elimina una carpeta de la lista.',
    '● Hide: It will hide the folder selected in the list.': '● Esconder: Esconde la carpeta seleccionada en la lista.',
    '● Show: It will un-hide the folder selected in the list.':
        '● Mostrar: Muestra la carpeta seleccionada en la lista.',
    'SYMBOLS MEANING:': 'SIGNIFICADO DE LOS SÍMBOLOS:',
    'Internet connection': 'Conexión a internet',
    'Database connection': 'Conexión a base de datos',
    'Disabled': 'Desactivado',
    'Active connection': 'Conexión activa',
    'Absent connection': 'Conexión ausente',
    'REQUIREMENTS:': 'REQUISITOS:',
    '● OS: Windows': '● OS: Windows',
    'read more...': 'leer más...',
    'Alert': 'Alerta',
    'Reset the program for apply the changes.': 'Reinicia el programa para aplicar los cambios.',
    'All folders in the list will be permanently deleted.':
        'Todas las carpetas en la lista serán eliminadas permanentemente.',
    'Are you sure you want to continue?': '¿Está seguro de querer continuar?',
    'Can not add the same directory twice.': 'No se puede agregar el mismo directorio dos veces.',
    "The inserted passwords don't match.": 'Las contraseñas insertadas no coinciden.',
    'Incorrect password. Please try again.': 'Contraseña incorrecta. Por favor inténtalo de nuevo.',
    'Invalid password.': 'Contraseña invalida.',
    'Cancel': 'Cancelar',
    'Developed by:': 'Desarrollado por:',
    'E-mail:': 'E-mail:',
    'Built on:': 'Echo en:',
    'July': 'Julio',
    'Runtime version:': 'Versión en ejecución:',
    'Login': 'Iniciar sesión',
    'password': 'contraseña',
    'Create Password': 'Crear contraseña',
    'new': 'nueva',
    'repeat': 'repetir',
    'Submit': 'Enviar',
    'Folder List': 'Lista de Carpetas',
    'Add': 'Nuevo',
    'Delete': 'Eliminar',
    'Hide': 'Esconder',
    'Show': 'Mostrar',
    'Clear': 'Borrar Todo',
    'Exit': 'Salir',
    'File': 'Archivo',
    'Show All': 'Mostrar Todo',
    'Hide All': 'Esconder Todo',
    'Edit': 'Editar',
    'English': 'Ingles',
    'Spanish': 'Español',
    'Italian': 'Italiano',
    'Settings': 'Ajustes',
    'Language': 'Idioma',
    'Backup': 'Respaldo',
    'Security': 'Seguridad',
    'Activate': 'Activar',
    'Deactivate': 'Desactivar',
    'Save Backup': 'Salvar Respaldo',
    'Load Backup': 'Cargar Respaldo',
    'Reset Password': 'Restablecer Contraseña',
    '? Help': '? Ayuda',
    'About': 'Información',
    'Help': 'Ayuda',
    'Folder hidden: ': 'Carpeta escondida: ',
    'Folder unhide: ': 'Carpeta mostrada: ',
    'Folder deleted: ': 'Carpeta eliminada: ',
    'Folder added: ': 'Carpeta añadida: ',
    'Folder not found: ': 'Carpeta no encontrada: ',
    "Can't hide a system folder": 'No se puede ocultar una carpeta del sistema',
    'All current folders will be configured as visible before emptying the list.':
        'Todas las carpetas actuales se configurarán como visibles antes de vaciar la lista.',
    'Are you sure you want to load the backup right now?': '¿Seguro que quiere cargar la copia de seguridad ahora?',
    'The backup has been loaded': 'La copia de seguridad ha sido cargada',
    'The backup has been updated': 'La copia de seguridad ha sido actualizada',
    'The backup has been activated': 'La copia de seguridad ha sido activada',
    'The backup has been deactivate': 'La copia de seguridad ha sido desactivada',
    'The backup is disabled': 'La copia de seguridad se encuentra desactivada',
    'The backup is empty.': 'La copia de seguridad se encuentra vacía.',
    'A backup has been created': 'Se ha creado una copia de seguridad.',
    'Database connection failed': 'Falló la conexión a la base de datos',
    'Could not establish a connection': 'No se pudo establecer una conexión',
    'All the folders has been hide': 'Se han escondido todas las carpetas',
    'All the folders has been shown': 'Se han mostrado todas las carpetas',
    'All the unhide folders has been deleted': 'Se han eliminado todas las carpetas no escondidas',
    "The folder is hide, it can't be deleted": 'La carpeta está oculta, no puede ser eliminada',
    'You must select a folder to hide': 'Debe seleccionar la carpeta a esconder',
    'You must select a folder to show': 'Debe seleccionar la carpeta a mostrar',
    'You must select a folder to delete': 'Debe seleccionar la carpeta a eliminar',
    'A new config file has been made': 'Se ha creado un nuevo archivo de configuración',
    'There are no folders to delete': 'No hay carpetas para eliminar',
    'There are no folders to hide': 'No hay carpetas para esconder',
    'There are no folders to show': 'No hay carpetas para mostrar'}
italian = {
    'Guide: "How to use this program".': 'Guida: "Come usare questo programma".',
    'UTILITY:': 'UTILITA:',
    'The usefulness of this program is to hide any folder effectively from Windows OS interface.':
        "L'utilità di questo programma è nascondere efficacemente qualsiasi cartella dall'interfaccia di Windows OS.",
    'Even on USB devices, so that these folders remain hidden on different computers.':
        'Anche su dispositivi USB, in modo che queste cartelle rimangano nascoste su computer diversi.',
    'MENU FUNCTIONS:': 'FUNZIONI DEL MENU:',
    '● File > Clear All: Remove all folders from the list.':
        "● Archivio > Ellimina Tutto: Rimuove dall'elenco tutte le cartelle.",
    '● Edit > Hide All / Show All: All the folders in the list.':
        "● Modifica > Nascondi Tutto / Mostra Tutto: Tutte le cartelle nell'elenco.",
    '● Backup > Activate / Deactivate: A backup of the configuration.':
        '● Backup > Attiva / Disattiva: Il backup della configurazione.',
    '● Backup > Save / Load: A backup of the configuration.':
        '● Backup > Salva / Carica: Il backup della configurazione.',
    '● Security > Activate / Deactivate: A password access to the program.':
        "● Sicurezza > Attiva / Disattiva: L'accesso con password al programma",
    'BUTTONS FUNCTIONS:': 'FUNZIONI DEI BOTTONI:',
    '● Add: Append a new folder to the list.': '● Aggiungi: Aggiunge una nuova cartella al elenco.',
    '● Delete: Remove a folder from the list.': "● Elimina: Rimuove una cartella all'elenco.",
    '● Hide: It will hide the folder selected in the list.':
        "● Nascondi: Nasconde la cartella selezionata nell'elenco.",
    '● Show: It will un-hide the folder selected in the list.':
        "● Mostra: Rende visibile la cartella selezionata nell'elenco.",
    'SYMBOLS MEANING:': 'SIGNIFICATO DEI SIMBOLI:',
    'Internet connection': 'Connessione internet',
    'Database connection': 'Connessione al database',
    'Disabled': 'Disabilitato',
    'Active connection': 'Connessione attiva',
    'Absent connection': 'Connessione assente',
    'REQUIREMENTS:': 'REQUISITI:',
    '● OS: Windows': '● OS: Windows',
    'read more...': 'leggi di più...',
    'Alert': 'Attenzione',
    'Reset the program for apply the changes.': 'Resetta il programma per applicare le modifiche.',
    'All folders in the list will be permanently deleted.':
        "Tutte le cartelle nell'elenco verranno eliminate in modo permanente.",
    'Are you sure you want to continue?': 'Sei sicuro di voler continuare?',
    'Can not add the same directory twice.': 'Impossibile aggiungere la stessa cartella due volte.',
    "The inserted passwords don't match.": 'Le password inserite non coincidono.',
    'Incorrect password. Please try again.': 'Password errata. Per favore riprova.',
    'Invalid password.': 'Password non valida.',
    'Cancel': 'Annulla',
    'Developed by:': 'Svilupato da:',
    'E-mail:': 'E-mail:',
    'Built on:': 'Costruito a:',
    'July': 'Luglio',
    'Runtime version:': 'Versione in esecuzione:',
    'Login': 'Accesso',
    'password': 'password',
    'Create Password': 'Crea password',
    'new': 'nuova',
    'repeat': 'ripetere',
    'Submit': 'Invio',
    'Folder List': 'Lista di Cartelle',
    'Add': 'Aggiungi',
    'Delete': 'Elimina',
    'Hide': 'Nascondi',
    'Show': 'Mostra',
    'Clear': 'Elimina Tutto',
    'Exit': 'Esci',
    'File': 'Archivio',
    'Show All': 'Mostra Tutto',
    'Hide All': 'Nasconde Tutto',
    'Edit': 'Modifica',
    'English': 'Inglese',
    'Spanish': 'Spagnolo',
    'Italian': 'Italiano',
    'Settings': 'Impostazioni',
    'Language': 'Lingua',
    'Backup': 'Backup',
    'Security': 'Sicurezza',
    'Activate': 'Attivare',
    'Deactivate': 'Disattivare',
    'Save Backup': 'Salvare Backup',
    'Load Backup': 'Caricare Backup',
    'Reset Password': 'Resettare Password',
    '? Help': '? Aiuto',
    'About': 'Informazioni',
    'Help': 'Aiuto',
    'Folder hidden: ': 'Cartella nascosta: ',
    'Folder unhide: ': 'Cartella mostrata: ',
    'Folder deleted: ': 'Cartella eliminata: ',
    'Folder added: ': 'Cartella aggiunta: ',
    'Folder not found: ': 'Cartella non trovata: ',
    "Can't hide a system folder": 'È impossibile nascondere una cartella di sistema',
    'All current folders will be configured as visible before emptying the list.':
        "Tutte le cartelle correnti verranno configurate come visibili prima di svuotare l'elenco.",
    'Are you sure you want to load the backup right now?': 'È sicuro di voler caricare il backup adesso?',
    'The backup has been loaded': 'Il backup è stato caricato',
    'The backup has been updated': 'Il backup è stato aggiornato',
    'The backup has been activated': 'Il backup è stato attivato',
    'The backup has been deactivate': 'Il backup è stato disattivato',
    'The backup is disabled': 'Il backup si trova disattivato',
    'The backup is empty.': 'Il backup si trova vuoto.',
    'A backup has been created': 'È stato creato un backup',
    'Database connection failed': 'Connessione al database non riuscita',
    'Could not establish a connection': 'Impossibile stabilire una connessione',
    'All the folders has been hide': 'Tutte le cartelle sono state nascoste',
    'All the folders has been shown': 'Tutte le cartelle sono state mostrate',
    'All the unhide folders has been deleted': 'Tutte le cartelle non nascoste sono state eliminate',
    "The folder is hide, it can't be deleted": 'La cartella è nascosta, non può essere eliminata',
    'You must select a folder to hide': 'Devi selezionare una cartella da nascondere',
    'You must select a folder to show': 'Devi selezionare una cartella da mostrare',
    'You must select a folder to delete': 'Devi selezionare una cartella da eliminare',
    'A new config file has been made': 'È stato creato un nuovo file di configurazione',
    'There are no folders to delete': 'Non ci sono cartelle da eliminare',
    'There are no folders to hide': 'Non ci sono cartelle da nascondere',
    'There are no folders to show': 'Non ci sono cartelle da mostrare'}

# Program configuration:
config = dict(Elements=[], Language='English', Backup=False, Security=False, Password=None)
base = english['Database']

# Current language:
lang = {}

# Backup connection status:
status_database = None

# Images files:
ico_main = """R0lGODlhMAAwAHAAACH5BAEAAAEALAAAAAAwADAAgQAAAAAAAAAAAAAAAAK6jI+py+0Po5y0Wgny
3Sh7wG2fF1ojWU4nmkKr1rpvLK/084JpDuch/zH4REDU0FQ0zpDJ3hIWaSptgWCtKXyOcFTrYbhc
hFlZanmrMJc7YTb6e0pDwfK3Gq4D6xK2O/yMRuYGxJCnBcUX54cXVyXIyLKo9+j4BohY2WgJiXnp
1OXF2cnp+dnZJjalKcgTZbhYGuoKKjXqMCnFtJqrG8jb61VUcnSTCltcityAqjxI2XwJffssXW19
LV0AADs="""
ico_help = """R0lGODlhEwATAHAAACH5BAEAADcALAAAAAATABMAhQAAAKWlpcrKyu7t79/f4qqqq87O2YuLqllZ
lmVlmRYWgAoKjwoKmRYWgr6+yiwsfQoKqjExk728vVRUvV9fraqqzri420REpOLi6YWFhff29z09
tRsbiRMTlPz8/PPz9iQko3d3sWlpwldXptXV53d3dwoKsxAQqpiYmFxcmIKCv6en0Hd3vYmJzJeX
uGxrx5mZ01lZWZeX0LW1turq6mZmZuXl6QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAblwJtw
WBAMBhhBYcgkDgwHBCJxMAyWzZsAg1AsGGCGIkEQNDGOxxfCYEPYHIKEaHi0IZNRxXJpdzgYGUIe
CGsbAw0dHh4dbwwhBDdFCm8QIh4jDBiYlR0GJQIHa28TjQMeDSdsDBUoBAhtJhCyEBuElWwqBVx3
s7IVIG+0ECwSArDCsxAIwrQMLQUFLr20jb6OFiUlBgrULzAnJsMnAzFaLL0QixfKbDJzNyUEfW0M
Ii7WbxHlQygY9KscMZjgoUSTDBhgdAgDBoSMAQaz1HAwwIKMFjIwYJBgLsuQGhkKSChQokaWIAA7"""
bkground = """R0lGODlh9AHmAPYAAAQEBAcIBwwMDA8QEBQUFBgXFxcYFxgYFxgXGBsbGx4gHyAgHx4eICAfIB8g
ICMjIyYoJycpKCsrKy4wLy8wMDIyMjY4Nzc5ODo7Oj1APz5BQEJDQ0VIR0VHSEZKSUpMTExQT05R
UVJUVFRYV1RXWFZaWVpcXFxgX15iYWFlZWNoZ2JnaGVramlubWZyaGpwbmpvcGxycnF2dnJ4d3N3
eHV7enl+fnqAf3p/gH2DgoGGhYKIh4GHiIWMiomOjYeQjYmRjoiYj4yUko+YlpGXlpGZl5Scm5ie
nZegn5ign5ehoJuko5+op5+pqKGnpqCop6Osq6ivrqewr6ixr6exsKu0s664t6+5uLC3trC5t7O9
u7i/v7bAv7jBv7fBwLvEw77Ix7/JyMHGxsDJx8PNy8nPzsbQzsjRz8fR0MrU083Y18/a2dDX1tDa
19Le3Nnf39Tg3tbi4Nnl493p59/q6OLt6+jv7uXw7+nw7+by8Ov09O349u/5+PH6+QAAAAAAACH5
BAAAAAAAIf8LSW1hZ2VNYWdpY2sHZ2FtbWE9MAAsAAAAAPQB5gAAB/6AAgYJDw8JBQOJAosDBI6O
AwIAk5OLjwQFBYMEkgCWjZiZmQiZA5kJCQyoh5yci56YBImYDQmdlAKNn5gJDaKHBavCsgkQqgUH
joPADBASExKFtY4JEtYFkgEECwmyuQQNELWHsw3SDRIQD9EQEAuyjainBwcMC6qsoLKhAwGUngN6
HUqwQN2CWgVaOULQTdIiAQEgLhKIShXCR5FMMUBkihMuAsLkEUpgYFGAeOMSkCJkqOKBQe0a2FtA
k1u3Agse3GuYyN+kiLEeRhSQiVdCRrG8mZIXaag3oqi8OXo4FaJPRf88PTQZYOhQARgfUorYtStY
Tl6zql3rSmylrP6LSq5VGxeBRwA+/0VchupAIkWWEkKC+M/So4QqCfjregmsKIaseIU8yhUoPLC9
sBVOujWUqEwGDGgKNg3kg43BNC3LtOAZtGi+qK2rla3AxW8Fx3G03e5BuAfOGqB714i0I1EMdHLj
CCpR0bwAV4GkOU7VcQMENj2M1Dm1PMlhNe7WXIkAQ4YtRxLAG5jk6pEVVYn+fU+VqmQBaR4DnPdk
0a2MCFYKd6aIUlwpEn3DiSnCJdRIU0ERNokudAlVlkmG/Sche9k4ZVVXc4VoiUO4wAXAVHilOBcj
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
QucvAtIgCpY7SpXO8JMknq5SJfO1S1IRoBc9iglKOunJR+vBI756t23jWTHKAmfB9wLAP5evTlZM
GM2vGTXaqKEKLHdDH3xLmeJvH3jB1YqEPRdwaMrwztO28k4s+jNG9+CCp4ezCE8vFWKDp7ZgNGWB
N3Vq9pAQ22Afv4Av67c53lhf1ZItRbUsPbxsiv7wstYyLUISbJ3aRXB7O+DoDuhuc0OSosCQCP+9
yJOWYPQewsOKd4KkJCODFVtkfmAH8EGsHbqsK8JmMkcBhbThPKL6bUWbGzwZmQrdbyv1r+09yYR/
KVMhoWZc2SQmehcT8yqvcpg8OJVOyZyy8aWN4pAV4Alj40g74KI+fUvCdM35cz5386NSTD0bOFyh
OOwoRhQGXnkveizRDxOIPBFydtUBDbrTdf1yOKeQegjKHzmhnpXUitFSYMhB0OK9HTyNRqQoarIc
4r+wuvIAD6xmI/FQDAeKginc9kEoyk7WK/6TyWesIRrL2PQN0Rry7twjE/+gg1wJCAUJCw8QEF0L
BIIEAAACA4kEBAOTk5CRBZGSiQkJkQkGCJycCJECjpkDmKaUpY4DAYyMAQKztLKPppGVA6sECAYC
sgGww66zqLqmyrCmsc6xyqazuMOwzgGPvLbPAgaYz7HFAYEAOw=="""
ico_wifi = """iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAAXNSR0IArs4c6QAAAARnQU1BAACx
jwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEdSURBVDhPzZG7UcNAFEW1pgG7A8gIFEAF2A0A
jqQQKgA3AHQADokwmTKgApsOCJTjDnBIohHnLGvGAnK4M8dXb2ffZ5+zP1NIHlWW5RA7gGPYhj6o
R1jCtKoqPSomk+SlSzgxRi+JVYyyzKKiZhQ49SOQuIc/gAVu4B5M8tyzFZcXqcEZXIHdx722bR2x
j4/xJ7iGV5iDRecktuncwvtgoeHm2I51Z4yc4BmcwLe7h3NQIyfxo+cPgZeOYNk0zQ5uognuQZ/C
ANyDo0d1tq2KopiEEC5SuO6sJjRxoi/Fzpsi8RDzr/FtjmiDGThZRz86r8UeXJbLXFBgFA+/6dfk
tMC3zyhqkPbS0Vbyjuq6fs/z3AK7cEuiz/g3yrIPyrRXknzoph4AAAAASUVORK5CYII="""
ico_db = """iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAAXNSR0IArs4c6QAAAARnQU1BAACx
jwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFlSURBVDhPhdI7L0NhGMDxt0rcbxVBBAmDimMT
EhIWow9wRovJh7DamCSmblaL+AgYugixsAmipIlbUdf/P+k7O8mv50l7nsv7nGbSNG0NIeQxi2VM
oQuN8LrCBY6wZ2zSGsE6evHfdY2NOj5W0IYqvvCLeBn/4Bv+3oHVbJIkkwRlvOAV7/is3St4wgMc
8xxnjlcgMKkJnsPu3rOwU2S3DHImXRIM4Bb3eMYbfMjEBrisQbigsuNNE3iWZvRgGGMYxQj60A7H
LaFopx2CD7TAirK6C3CseD6nsHDV+eewgAlY0S09wnO6BJPc7jhmsGinXYIldMLtmWQXefB4rnq4
zWOTtmtf+PAQrGoBv/OsLsWz3MFCFZNOCJzX9+C4Votd5Fm9/M1F9Zt0Q9ANO1lVxq7cB+3oAnx3
KrlyH5iH78DNOVoOVvVuQUe2o++yYNIpwT78M1rAf4bJrjuu+hBb2AwhHPwBtCRq+gEIZPUAAAAA
SUVORK5CYII="""
ico_copy = """iVBORw0KGgoAAAANSUhEUgAAABAAAAARCAYAAADUryzEAAAAAXNSR0IArs4c6QAAAARnQU1BAACx
jwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADQSURBVDhPY4yIjPpvYmrKQAx49vQpQ19vDyOU
CwaMmVnZ/93cPaBc/ODu3TsMJUWFKAYwQWkwACnAh0EuQAcoLgj090UxnRjAAqXhoKev/7+ysgqU
hx/s2rkD1QvkAAwXwMD79+8ZTp86CeWhAuRAx+mC79+/Mdy7excrRgY4XSAlJc2QkZUN5eEGOA0A
RduMaVOhPFTQ3dsPZVHBBTjD4MePHwx37wATEBaMDJhAoQ1LaciA2EDESHl0T0gUG4DhBVD5ICgo
COXhB/fu3mUAAM7mhza6UT2NAAAAAElFTkSuQmCC"""

# Create pillow images:
bg_bytes = b64decode(bkground)
bckground = ImageTk.BytesIO(bg_bytes)
copy_bytes = b64decode(ico_copy)
copy = ImageTk.BytesIO(copy_bytes)
wifi_bytes = b64decode(ico_wifi)
wifi = ImageTk.BytesIO(wifi_bytes)
db_bytes = b64decode(ico_db)
dbase = ImageTk.BytesIO(db_bytes)

# GUI palette colors:
black1 = 'gray13'    # dark
black2 = 'gray18'    # light
gray1 = 'gainsboro'  # light
gray2 = 'dimgray'    # dark
gray3 = 'ivory4'     # medium
red1 = 'OrangeRed2'  # dark
red2 = 'coral'       # light
green = 'forest green'


class Elem:
    """ Create elements for the list, useful for
     assign name to single path and hide status """

    def __init__(self, _name='', _path='', _fullpath='', _hide=False):
        self._name = _name
        self._path = _path
        self._fullpath = _fullpath
        self._hide = _hide


def file_gen():
    """  Create 'License.txt' and 'Info.txt' """

    # Make directory:
    if isdir('config') == 0:
        mkdir('config')

    # Create files:
    with open('License.txt', 'w') as lic, open('Info.txt', 'w') as inf, open('Readme.txt', 'w') as read:
        lic.write(f'Copyright: {__copyright__}\n\nLicense:{__license__}')
        inf.write(f'Author: {__author__}\n\nWeb Site: {__website__}\n\nEmail: {__email__}\n\nRecovery: {__recovery__}')
        read.write(__readme__)


def internet():
    """ Check internet connection """

    host = '8.8.8.8'    # Google public DNS
    port = 53           # TCP
    timeout = 3         # Seconds

    try:
        setdefaulttimeout(timeout)
        _socket(AF_INET, SOCK_STREAM).connect((host, port))
        return True
    except:
        return False


def set_ico(window_name, icon_data):
    """ Set the chosen icon to one window """

    # Config and set icon:
    icondata = b64decode(icon_data)
    tempfile = 'temp'
    try:
        remove(tempfile)  # remove any file with the same name
    except:
        pass  # prevent from error if there is no file

    try:
        iconfile = open(tempfile, 'wb')  # create the file
        system(f'attrib +H {tempfile} > nul')  # hide the file
        iconfile.write(icondata)  # create the icon
        iconfile.close()
        icon = PhotoImage(file=tempfile)
        root.tk.call('wm', 'iconphoto', window_name, icon)
        remove(tempfile)  # delete the tempfile
    except:
        pass  # prevent from error in case it can't create the icon file


def load_lang(refresh=False):
    """ Load the language """

    global lang

    if config['Language'] == 'English':
        lang = 'English', english

    elif config['Language'] == 'Italian':
        lang = 'Italian', italian

    elif config['Language'] == 'Spanish':
        lang = 'Spanish', spanish

    else:
        lang = 'English', english

    if refresh == 1:  # reset language after load config from backup

        # Restart the program loading new language:
        root.destroy()
        program_start(bckp_notf=True, login=False)  # 'bckp_notf=True' activate a message of 'load config correctly'


def lang_english():
    """ Save in the file json the chosen language """

    # Modify the list config[] for save it later in the json:
    config['Language'] = 'English'

    # Update the json file with the new language:
    save_data(db=True)

    # Restart the program loading new language:
    root.destroy()
    program_start(login=False)


def lang_italian():
    """ Save in the file json the chosen language """

    # Modify the list config[] for save it later in the json:
    config['Language'] = 'Italian'

    # Update the json file with the new language:
    save_data(db=True)

    # Restart the program loading new language:
    root.destroy()
    program_start(login=False)


def lang_spanish():
    """ Save in the file json the chosen language """

    # Modify the list config[] for save it later in the json:
    config['Language'] = 'Spanish'

    # Update the json file with the new language:
    save_data(db=True)

    # Restart the program loading new language:
    root.destroy()
    program_start(login=False)


def led(led1, led2):
    """ Labels of status led's in the main window """

    # Wifi image configuration:
    pil_wifi = Img.open(wifi)  # get the image with PIL
    tk_wifi = ImageTk.PhotoImage(pil_wifi)  # convert to an image Tkinter can handle

    # Database image configuration:
    pil_db = Img.open(dbase)  # get the image with PIL
    tk_db = ImageTk.PhotoImage(pil_db)  # convert to an image Tkinter can handle

    # Set wifi image:
    bg_l = Label(image=tk_wifi, bg=black1)
    bg_l.image = tk_wifi
    bg_l.grid(row=0, column=0, pady=5, sticky=E + N)

    # Connection Led:
    Label(text='● ', font=('', 8), fg=led1, bg=black1).grid(row=0, column=1, pady=4, padx=1, sticky=W + N)

    # Set database image:
    bg_l = Label(image=tk_db, bg=black1)
    bg_l.image = tk_db
    bg_l.grid(row=0, column=0, pady=24, padx=0, sticky=E + N)

    # Backup led:
    Label(text='● ', font=('', 8), fg=led2, bg=black1).grid(row=0, column=1, pady=22, padx=1, sticky=W + N)


def status_led():
    """ Update led status if backup is activated """

    if config['Backup'] == 1:
        if internet() == 1:
            if status_database is None:
                return led('green', gray2)
            elif status_database == 1:
                return led('green', 'green')
            else:
                return led('green', 'red')
        else:
            return led('red', 'red')
    led(led1=gray2, led2=gray2)


def bg_confg():
    """ Background configuration """

    pil_bg = Img.open(bckground)  # get the image with PIL
    tk_bg = ImageTk.PhotoImage(pil_bg)  # convert to an image Tkinter can handle
    return tk_bg


def prep_for_save():
    """ Prepare the information for the saving process """

    # Prepare folders object list:
    dct = [elem.__dict__ for elem in config['Elements']]

    return dct


def backup(_load=False, save=False, force=False, alert=False):
    """ Back up in a database of the config file """

    global lang, status_database
    u, p = decodebytes(base.encode()).decode("utf-8").split()

    if config['Backup'] or force == 1:  # proceed if the backup status is active

        if internet() == 1:  # proceed if there is an internet connection
            # Force is used only if config file is missing

            # Get the mac address of the current pc:
            mac = (':'.join(['{:02x}'.format((getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])).upper()

            # Encrypt the mac address for save it in the database:
            mac_hash = sha3_512(mac.encode()).hexdigest()

            # Connect to database:
            try:
                client = MongoClient(f'mongodb+srv://{u}:{p}@backup-wuq9k.mongodb.net/test?retryWrites=true&w=majority')
                db = client['Backup']
                del u, p, client
                database = db.get_collection('Hidden-Folder')
                status_database = True

                # Update led status:
                status_led()

            except:
                status_database = False
                return 'database error'

            # Load config from DB:
            if _load == 1:
                doc = database.find_one({'ID': mac_hash})

                if force == 0:  # avoid this for run if attribute force is set

                    if not doc['Config']['Elements']:  # if doc is empty []
                        # Show message for communicate that backup is empty:
                        msg = messagebox.askokcancel(title=lang[1]['Alert'],
                                                     message=f"{lang[1]['The backup is empty.']}\n\n"
                                                             f"{lang[1]['Are you sure you want to continue?']}",
                                                     icon='warning')
                        if msg == 0:
                            return

                # Protect the user from lose access to folders that still hidden:
                un_hide_all(save=False, alert=False)

                if doc is not None:
                    # Create 'class Elem' objects from json:
                    obj_list = [Elem(d['_name'], d['_path'], d['_fullpath'], d['_hide'])
                                for d in doc['Config']['Elements']]

                    # Clear list:
                    config['Elements'].clear()

                    # Load the objects of 'class Elem' into config list:
                    for obj in obj_list:
                        config['Elements'].append(obj)

                        # Hide the folders that had that configuration:
                        if obj._hide == 1:
                            hide(obj)  # hide the folder

                        # Show the folders that had that configuration:
                        if obj._hide == 0:
                            un_hide(obj)  # show the folder

                    # Update the listbox:
                    refresh_listbox()

                    # Load the language from json into config list:
                    config['Language'] = doc['Config']['Language']

                    # Save to file:
                    save_data(db=False)

                    if force == 0:
                        if lang[0] != config['Language']:
                            return load_lang(refresh=True)

                    return 'loaded'  # activate an alert in status bar

            # Save config to DB:
            if save == 1:

                # Prepare information for save:
                dct = prep_for_save()

                # Prepare data for database:
                data = (dict(Elements=dct, Language=config['Language']))

                # Control if current pc has a backup in the database:
                if database.find_one({'ID': mac_hash}) is not None:
                    database.update_one({'ID': mac_hash}, {'$set': {'Config': data}})  # update it
                    if alert == 1:
                        return 'updated'  # activate an alert in status bar
                    return

                # Create a new backup in the database if need:
                database.insert_one(dict(ID=mac_hash, Config=data))
                return 'created'  # activate an alert in status bar

        return 'no internet'  # activate an alert in status bar


def load_from_database():
    """ Call backup() giving the parameters for load """

    if config['Backup'] == 0:
        return refresh_status_bar(text=lang[1]['The backup is disabled'], color=red2)  # display error in status bar

    msg = messagebox.askokcancel(title=lang[1]['Alert'],
                                 message=
                                 f"{lang[1]['All current folders will be configured as visible before emptying the list.']}"
                                 f"\n\n{lang[1]['Are you sure you want to load the backup right now?']}",
                                 icon='warning')
    if msg == 1:
        status = backup(_load=True)  # 'messag=True' enable a second alert message when menubar button are clicked.

        if status == 'loaded':
            # Display message in status bar:
            refresh_status_bar(text=lang[1]['The backup has been loaded'], color=green)

        elif status == 'no internet':
            # Display error in status bar:
            refresh_status_bar(text=lang[1]['Could not establish a connection'], color=red2)

        elif status == 'database error':
            # Display error in status bar:
            refresh_status_bar(text=lang[1]['Database connection failed'], color=red2)

    # Update led status:
    status_led()


def save_to_database():
    """ Call backup() giving the parameters for save """

    if config['Backup'] == 0:
        return refresh_status_bar(text=lang[1]['The backup is disabled'], color=red2)  # display error in status bar

    status = backup(save=True, alert=True)  # 'alert=True' activate update alerts only when menubar button are clicked.

    if status == 'updated':
        # Display message in status bar:
        refresh_status_bar(text=lang[1]['The backup has been updated'], color=green)

    elif status == 'created':
        # Display message in status bar:
        refresh_status_bar(text=lang[1]['A backup has been created'], color=green)

    elif status == 'no internet':
        # Display error in status bar:
        refresh_status_bar(text=lang[1]['Could not establish a connection'], color=red2)

    elif status == 'database error':
        # Display error in status bar:
        refresh_status_bar(text=lang[1]['Database connection failed'], color=red2)

    # Update led status:
    status_led()


def activate_database():

    config['Backup'] = True

    save_data(db=False)  # save backup activation setting to file, avoid overwriting database

    # Display message in status bar:
    refresh_status_bar(text=lang[1]['The backup has been activated'], color=green)

    # Update led status:
    status_led()


def deactivate_database():

    global status_database
    config['Backup'] = False
    status_database = None

    save_data(db=False)  # save backup activation setting to file, avoid overwriting database

    # Display message in status bar:
    refresh_status_bar(text=lang[1]['The backup has been deactivate'], color=green)

    # Update led status:
    status_led()


def activate_security():

    config['Security'] = True
    if config['Password'] is None:
        login_w()
    save_data()


def deactivate_security():

    config['Password'] = None
    config['Security'] = False
    save_data()


def reset_password():

    config['Password'] = None
    config['Security'] = True
    login_w()
    save_data()


def alert_duplicate():
    """ Inform the user that the folders he is trying to add exist already in the list """

    messagebox.showerror(title=lang[1]['Alert'], message=lang[1]['Can not add the same directory twice.'],
                         icon='warning')


def alert_clear():
    """ Inform the user that he is about to eliminate all the non hide folders from the list """

    msg = messagebox.askokcancel(title=lang[1]['Alert'],
                                 message=f"{lang[1]['All folders in the list will be permanently deleted.']}\n\n"
                                         f"{lang[1]['Are you sure you want to continue?']}", icon='question')
    if msg == 1:
        delete_all()


def size_config(name, width, height):
    """ Config Size / Position of the windows: """

    # Update info about current screen size:
    name.update_idletasks()

    # Size:
    w = width  # get size width ↔
    h = height  # get size height ↕

    # Config position:
    ws = name.winfo_screenwidth()
    hs = name.winfo_screenheight()
    x = int((ws / 2) - (w / 2))  # get position x —→
    y = int((hs / 2) - (h / 2))  # get position y ↑

    # Set window size and position:
    name.geometry(f'{w}x{h}+{x}+{y}')


def new_window(name, title='', width=int(), height=int(), titlebar=True):
    """ Create a new window """

    # Create window:
    name = Toplevel(root)
    name.configure(background=black1)
    name.resizable(False, False)

    # Hide window for load all the components:
    name.withdraw()

    # Set size and position of the window:
    size_config(name=name, width=width, height=height)

    if titlebar == 0:
        name.overrideredirect(1)  # make disapear the title bar

    else:
        name.title(title)  # set title

    return name


def create_help_window():
    """ Create a window with information that help the user """

    def open_link(event):
        open_new('https://github.com/Ariel-MN/Hidden_Folder/wiki')

    # Create window, config size:
    if config['Language'] == 'English':
        window = new_window(name='help_w', title=lang[1]['Help'], width=570, height=660)
        set_ico(window_name=window, icon_data=ico_help)

    elif config['Language'] == 'Spanish':
        window = new_window(name='help_w', title=lang[1]['Help'], width=670, height=660)
        set_ico(window_name=window, icon_data=ico_help)

    elif config['Language'] == 'Italian':
        window = new_window(name='help_w', title=lang[1]['Help'], width=660, height=660)
        set_ico(window_name=window, icon_data=ico_help)
    else:
        return

    # Wifi image configuration:
    pil_wifi = Img.open(wifi)  # get the image with PIL
    tk_wifi = ImageTk.PhotoImage(pil_wifi)  # convert to an image Tkinter can handle

    # Database image configuration:
    pil_db = Img.open(dbase)  # get the image with PIL
    tk_db = ImageTk.PhotoImage(pil_db)  # convert to an image Tkinter can handle

    # Labels text and images:
    Label(window, text=lang[1]['Guide: "How to use this program".'], fg=gray1, bg=black1,
          font=('comicsans', 16)).grid(row=0, column=0, pady=10, padx=10)
    Label(window, text=lang[1]['UTILITY:'], fg=red2, bg=black1,
          font=('comicsans', 10)).grid(row=1, column=0, pady=10, padx=10)
    Label(window,
          text=lang[1]['The usefulness of this program is to hide any folder effectively from Windows OS interface.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=2, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['Even on USB devices, so that these folders remain hidden on different computers.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=3, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['MENU FUNCTIONS:'],
          fg=red2, bg=black1, font=('comicsans', 10)).grid(row=4, column=0, pady=10, padx=10)
    Label(window, text=lang[1]['● File > Clear All: Remove all folders from the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=5, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Edit > Hide All / Show All: All the folders in the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=6, column=0, pady=0, padx=20, sticky=W)

    Label(window, text=lang[1]['● Backup > Activate / Deactivate: A backup of the configuration.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=7, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Backup > Save / Load: A backup of the configuration.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=8, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Security > Activate / Deactivate: A password access to the program.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=9, column=0, pady=0, padx=20, sticky=W)

    Label(window, text=lang[1]['BUTTONS FUNCTIONS:'],
          fg=red2, bg=black1, font=('comicsans', 10)).grid(row=10, column=0, pady=10, padx=10)
    Label(window, text=lang[1]['● Add: Append a new folder to the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=11, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Delete: Remove a folder from the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=12, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Hide: It will hide the folder selected in the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=13, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['● Show: It will un-hide the folder selected in the list.'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=14, column=0, pady=0, padx=20, sticky=W)
    Label(window, text=lang[1]['SYMBOLS MEANING:'],
          fg=red2, bg=black1, font=('comicsans', 10)).grid(row=15, column=0, pady=10, padx=10)

    # Wifi image:
    bg_l = Label(window, image=tk_wifi, bg=black1)
    bg_l.image = tk_wifi
    bg_l.grid(row=16, column=0, padx=25, sticky=W)
    Label(window, text=lang[1]['Internet connection'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=16, column=0, pady=0, padx=45, sticky=W)

    # Database image:
    bg_l = Label(window, image=tk_db, bg=black1)
    bg_l.image = tk_db
    bg_l.grid(row=17, column=0, padx=25, sticky=W)
    Label(window, text=lang[1]['Database connection'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=17, column=0, pady=0, padx=45, sticky=W)

    # Leds:
    Label(window, text='●', font=('', 8), fg=gray2, bg=black1).grid(row=18, column=0, pady=0, padx=30, sticky=W)
    Label(window, text=lang[1]['Disabled'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=18, column=0, pady=0, padx=45, sticky=W)
    Label(window, text='●', font=('', 8), fg='green', bg=black1).grid(row=19, column=0, pady=0, padx=30, sticky=W)
    Label(window, text=lang[1]['Active connection'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=19, column=0, pady=0, padx=45, sticky=W)
    Label(window, text='●', font=('', 8), fg='red', bg=black1).grid(row=20, column=0, pady=0, padx=30, sticky=W)
    Label(window, text=lang[1]['Absent connection'],
          fg=gray1, bg=black1, font=('comicsans', 10)).grid(row=20, column=0, pady=0, padx=45, sticky=W)

    Label(window, text=lang[1]['REQUIREMENTS:'], fg=red2, bg=black1,
          font=('comicsans', 10)).grid(row=21, column=0, pady=10, padx=10)
    Label(window, text=lang[1]['● OS: Windows'], fg=gray1, bg=black1,
          font=('comicsans', 10)).grid(row=22, column=0, pady=0, padx=20, sticky=W)

    link = Label(window, text=lang[1]['read more...'], fg='royal blue', bg=black1,
                 font=('arial', 8), cursor='hand2')
    link.grid(row=23, column=0, pady=0, padx=20, sticky=E)
    link.bind('<Button-1>', open_link)

    # Prevents the user from opening more windows:
    window.transient(root)
    window.grab_set()

    # Show the window:
    window.deiconify()


def create_about_window():
    """ Create a window with information about the program and his creator """

    # Create window:
    window = new_window(name='about_w', width=500, height=230, titlebar=False)

    # Load the background config:
    tk_bg = bg_confg()

    # Symbol of copy configuration:
    pil_copy = Img.open(copy)  # get the image with PIL
    tk_copy = ImageTk.PhotoImage(pil_copy)  # convert to an image Tkinter can handle

    # Set background image:
    bg_l = Label(window, image=tk_bg, bg=black1)
    bg_l.image = tk_bg
    bg_l.place(x=0, y=0, relwidth=1, relheight=1)

    # Labels:
    Label(window, text='HIDDEN FOLDER', fg=gray1, bg=black1, font=('comicsans', 20)).grid(row=1, column=2, pady=20)
    Label(window, text=f"{lang[1]['Developed by:']} {__author__}", fg=gray2, anchor=W, bg=black1,
          font=('comicsans', 10)).grid(row=2, column=2, pady=0, sticky=W + E)
    Label(window, text=f"{lang[1]['E-mail:']} {__email__}", fg=gray2, bg=black1, anchor=W,
          font=('comicsans', 10)).grid(row=3, column=2, pady=0, sticky=W + E)
    Label(window, text=f"{lang[1]['Built on:']} {lang[1]['July']} 14, 2019", fg=gray2, bg=black1, anchor=W,
          font=('comicsans', 10)).grid(row=4, column=2, pady=0, sticky=W + E)
    Label(window, text=f"{lang[1]['Runtime version:']} {__version__}", fg=gray2, bg=black1, anchor=W,
          font=('comicsans', 10)).grid(row=5, column=2, pady=0, sticky=W + E)
    Label(window, text=__copyright__, fg=gray2, bg=black1, anchor=W,
          font=('comicsans', 7)).grid(row=6, column=2, pady=8, sticky=W + E)
    Label(window, fg=gray2, bg=black1, font=('', 1)).grid(row=6, column=1, pady=0, padx=40)

    # Set symbol image:
    copy_l = Label(window, image=tk_copy, bg=black1, cursor='hand2')
    copy_l.image = tk_copy
    copy_l.grid(row=5, column=3)

    # Prevents the user from opening more windows:
    window.transient(root)
    window.grab_set()

    # Show the window:
    window.deiconify()

    def copy_to_clipboard(event):
        """ Copy the info from 'about window' to clipboard """

        # Configure information:
        field_value = f"{lang[1]['Developed by:']} {__author__}\n\n" \
                      f"{lang[1]['E-mail:']} {__email__}\n\n" \
                      f"{lang[1]['Built on:']} {lang[1]['July']} 14, 2019\n\n" \
                      f"{lang[1]['Runtime version:']} {__version__}\n\n{__copyright__}"
        root.clipboard_clear()  # clear clipboard contents
        root.clipboard_append(field_value)  # append the new value to clipbaord

    def exit_w(event):
        # Close the 'about window':
        window.destroy()
        return

    # Detect click in label image and copy the information:
    copy_l.bind('<Button-1>', copy_to_clipboard)

    # Detect click in the window and close it:
    window.bind('<Button-1>', exit_w)  # close window when click on it
    root.bind('<Escape>', exit_w)  # close window when press Esc


def login_w():
    """ Program login """

    if config['Security'] is True:

        def submit():
            """ Submit button for login """

            if config['Password'] is not None:
                pwd = entry_pwd.get()
                pwd_hash = sha3_512(pwd.encode()).hexdigest()

                if pwd_hash == config['Password']:
                    login_w.destroy()

                    # Show the main window:
                    root.deiconify()
                else:
                    return messagebox.showerror(
                        title=lang[1]['Alert'],
                        message=lang[1]['Incorrect password. Please try again.'], icon='warning')

            else:
                pwd1, pwd2 = entry_pwd1.get(), entry_pwd2.get()

                if pwd1 == pwd2:
                    if pwd1 == '' or pwd2 == '':
                        return messagebox.showerror(title=lang[1]['Alert'], message=lang[1]['Invalid password.'],
                                                    icon='warning')

                    pwd_hash = sha3_512(pwd1.encode()).hexdigest()
                    config['Password'] = pwd_hash
                    save_data()
                    login_w.destroy()

                    # Show the main window:
                    root.deiconify()
                else:
                    messagebox.showerror(title=lang[1]['Alert'],
                                         message=lang[1]["The inserted passwords don't match."], icon='warning')

        # Shortcuts:
        def exit_login(event):
            if config['Password'] is None:
                login_w.destroy()

                # Show the main window:
                root.deiconify()
            else:
                # Close the program:
                root.destroy()

        def shortcut_9(event):
            submit()

        # Create window:
        login_w = new_window(name='login_w', width=300, height=150, titlebar=False)

        # Prevents the user from opening more windows:
        login_w.transient(root)
        login_w.grab_set()

        # Load the background config:
        tk_bg = bg_confg()

        # Set background image in Login window:
        bg_l = Label(login_w, image=tk_bg, bg=black1)
        bg_l.image = tk_bg
        bg_l.place(x=0, y=0)

        if config['Password'] is not None:
            Label(login_w, text=lang[1]['Login'], fg=gray1, bg=black1,
                  font=('comicsans', 14)).grid(row=0, column=1, pady=10, padx=0)
            Label(login_w, text=lang[1]['password'], fg=gray2, bg=black1,
                  font=('comicsans', 10)).grid(row=1, column=0, padx=10, pady=6, sticky=E)
            entry_pwd = Entry(login_w, width=20, show='●', font=('', 10), bg=gray2)
            entry_pwd.grid(row=1, column=1, pady=0, padx=0)
            entry_pwd.bind('<Return>', shortcut_9)  # submit when pressing 'Enter key'
            entry_pwd.focus_set()

        elif config['Password'] is None:
            Label(login_w, text=lang[1]['Create Password'], fg=gray1, bg=black1,
                  font=('comicsans', 14)).grid(row=0, column=1, pady=10, padx=0)
            Label(login_w, text=lang[1]['new'], fg=gray2, bg=black1,
                  font=('comicsans', 10)).grid(row=1, column=0, padx=10, sticky=E)
            entry_pwd1 = Entry(login_w, width=20, font=('', 11), bg=gray2)
            entry_pwd1.grid(row=1, column=1)
            Label(login_w, text=lang[1]['repeat'], fg=gray2, bg=black1,
                  font=('comicsans', 10)).grid(row=2, column=0, padx=10, sticky=E)
            entry_pwd2 = Entry(login_w, width=20, font=('', 11), bg=gray2)
            entry_pwd2.grid(row=2, column=1)
            entry_pwd1.bind('<Return>', shortcut_9)
            entry_pwd2.bind('<Return>', shortcut_9)
            entry_pwd1.focus_set()

        Button(login_w, text=lang[1]['Submit'], fg=gray3, bg=black2, cursor='hand2', font=('comicsans', 11),
               command=submit).grid(row=3, column=1, pady=15, padx=0)

        close_button = Label(login_w, text='X', fg=gray3, bg=black1, cursor='hand2', font=('comicsans', 10))
        close_button.place(x=285, y=0)

        # Detect click in label image and copy the information:
        close_button.bind('<Button-1>', exit_login)

        # Show the login window:
        login_w.deiconify()

    elif config['Security'] is False:

        # Show the main window:
        root.deiconify()


def load_data():
    """ Load all the configuration from the cfg file """

    # Open the file:
    with open(join_p('config', 'data.cfg'), 'rb') as f:
        data_encrypt = f.read()

        # Load Key:
        with open('.temp', 'rb') as k:
            key = k.read()

        if key != b'':
            # Decrypt Data:
            data = Fernet(key).decrypt(data_encrypt).decode()

            # Load the json format:
            data = loads(data)

            # Create 'class Elem' objects from json:
            obj_list = [Elem(d['_name'], d['_path'], d['_fullpath'], d['_hide']) for d in data['Elements']]

            # Load the objects of 'class Elem' (folders information):
            for obj in obj_list:
                config['Elements'].append(obj)

            # Load the language:
            config['Language'] = data['Language']

            # Load the backup activation status:
            config['Backup'] = data['Backup']

            # Load the Security activation status:
            config['Security'] = data['Security']

            # Load the password hash for the login:
            config['Password'] = data['Password']

            # Update the listbox:
            refresh_listbox()


def save_data(db=False):
    """ Save the config list in a cfg file """

    if db == 1:
        backup(save=True)  # proceed only if backup is enabled

    # Open the file:
    with open(join_p('config', 'data.cfg'), 'wb') as f:
        # Prepare information for save:
        dct = prep_for_save()

        def generate_key():

            with open('.temp', 'wb') as k:
                key = Fernet.generate_key()
                k.write(key)
                system(f'attrib +S +H ".temp" > nul')
            return key

        # Load or create key:
        if isfile('.temp') == 1:
            with open('.temp', 'rb') as k:
                key = k.read()

            if key == b'':
                key = generate_key()

        else:
            key = generate_key()

        # Give a json format and encode:
        data = dumps(dict(Elements=dct, Language=config['Language'], Backup=config['Backup'],
                          Security=config['Security'], Password=config['Password'])).encode()

        # Encrypt the data:
        data_encrypt = Fernet(key).encrypt(data)

        # Write to file:
        f.write(data_encrypt)

    # Update the led status from main window:
    status_led()  # proceed only if backup is enabled


def add_folder():
    """ Allow user to select a directory and store it in a global variable """

    global folder_path, path

    # Open a browser for select a folder:
    path = filedialog.askdirectory()
    folder_path.set(path)

    if path != '':

        i = path.rindex('/') + 1  # obtain index of the last '/'
        _path = path[:i]  # get the path of the folder from string
        _name = path[i:]  # get the name of the folder from path string

        # Control if the path already exist:
        for items in config['Elements']:
            if items._fullpath == path:
                alert_duplicate()  # display an alert to the user if the folder is already in the list
                return

        # Append the path to the list:
        temp_obj = Elem(_name=_name, _path=_path, _fullpath=path, _hide=False)  # create a temp object
        config['Elements'].append(temp_obj)  # append to the list

        # Update the listbox:
        refresh_listbox()

        # Update the json file:
        save_data(db=True)

        # Display message in status bar:
        refresh_status_bar(text=f"{lang[1]['Folder added: ']}'{temp_obj._name}'", color=green)


def delete_path(f_obj=None):
    """ Delete a selected item from the listbox """

    if f_obj is not None:
        index = config['Elements'].index(f_obj)
        # Remove one from list:
        del config['Elements'][index]
        # Remove one from listbox:
        mylistbox.delete(index)
        return

    # Index of the object:
    sel = mylistbox.curselection()

    if sel == ():
        # Display error in status bar:
        refresh_status_bar(text=lang[1]['You must select a folder to delete'], color=red2)
    else:
        # Control if the folder is hide:
        for index in reversed(sel):
            folder = config['Elements'][index]
            if folder._hide == 1:
                # Display error in status bar:
                return refresh_status_bar(text=lang[1]["The folder is hide, it can't be deleted"], color=red2)

            # Remove from listbox:
            mylistbox.delete(index)

            # # Remove from list:
            name = folder._name
            config['Elements'].remove(folder)

            # Display message in status bar:
            refresh_status_bar(text=f"{lang[1]['Folder deleted: ']}'{name}'", color=green)

            # Update the json file:
            save_data(db=True)


def hide(folder=None):
    """ Hide the selected folder from the OS Interface """

    if folder is not None:
        if folder._hide == 0:
            if isdir(folder._fullpath) == 1:  # control if the folder exist
                new_path = f'{folder._path}.{folder._name}'  # add a '.' to folder name
                try:
                    rename(folder._fullpath, new_path)  # rename folder
                    system(f'attrib +S +H "{new_path}" > nul')  # hide the folder
                    folder._hide = True  # change status
                except:
                    pass  # prevent from error if try to hide a system folder
        return

    sel = mylistbox.curselection()

    if sel == ():
        # Display error in status bar:
        return refresh_status_bar(text=lang[1]['You must select a folder to hide'], color=red2)

    for index in reversed(sel):
        folder = config['Elements'][index]
        if folder._hide == 0:
            if isdir(folder._fullpath) == 1:  # control if the folder exist
                new_path = f'{folder._path}.{folder._name}'  # add a '.' to folder name
                try:
                    rename(folder._fullpath, new_path)  # rename folder
                    system(f'attrib +S +H "{new_path}" > nul')  # hide the folder
                    folder._hide = True  # change status

                    # Display message in status bar:
                    refresh_status_bar(text=f"{lang[1]['Folder hidden: ']}'{folder._name}'", color=green)
                except:
                    # Display error in status bar:
                    refresh_status_bar(text=lang[1]["Can't hide a system folder"], color=red2)

            else:
                # Display error in status bar:
                refresh_status_bar(text=f"{lang[1]['Folder not found: ']}'{folder._name}'", color=red2)

            # Save hide status in json file:
            # save_data(db=True)
            save_data(db=True)

            # Update status of the folder in the listbox:
            refresh_listbox()


def hide_all():
    """ Hide all the folders in the list from the OS Interface """

    if not config['Elements']:
        # Display error in status bar:
        return refresh_status_bar(text=lang[1]['There are no folders to hide'], color=red2)

    for folder in config['Elements']:
        if folder._hide == 0:
            if isdir(folder._fullpath) == 1:
                new_path = f'{folder._path}.{folder._name}'  # add a '.' to folder name
                try:
                    rename(folder._fullpath, new_path)  # rename folder
                    system(f'attrib +S +H "{new_path}" > nul')  # hide the folder
                    folder._hide = True  # change status

                    # Display message in status bar:
                    refresh_status_bar(text=lang[1]['All the folders has been hide'], color=green)
                except:
                    # Display error in status bar:
                    refresh_status_bar(text=lang[1]["Can't hide a system folder"], color=red2)
            else:
                # Display error in status bar:
                refresh_status_bar(text=f"{lang[1]['Folder not found: ']}'{folder._name}'", color=red2)

    # Save hide status in json file:
    save_data(db=True)

    # Update status of the folder in the listbox:
    refresh_listbox()


def un_hide(folder=None):
    """ Show the selected folder in the OS Interface """

    if folder is not None:
        if folder._hide == 1:
            cur_path = f'{folder._path}.{folder._name}'  # the actual name of the folder have a '.'

            if isdir(cur_path) == 1:  # control if the folder exist
                try:
                    rename(cur_path, folder._fullpath)  # rename folder
                    system(f'attrib -S -H "{folder._fullpath}" > nul')  # show the folder
                    folder._hide = False  # change status
                except:
                    pass  # prevent from error if try to hide a system folder
        return

    sel = mylistbox.curselection()

    if sel == ():
        # Display error in status bar:
        return refresh_status_bar(text=lang[1]['You must select a folder to show'], color=red2)

    for index in reversed(sel):
        folder = config['Elements'][index]
        if folder._hide == 1:
            cur_path = f'{folder._path}.{folder._name}'  # the actual name of the folder have a '.'

            if isdir(cur_path) == 1:  # control if the folder exist
                rename(cur_path, folder._fullpath)  # rename folder
                system(f'attrib -S -H "{folder._fullpath}" > nul')  # show the folder
                folder._hide = False  # change status

                # Display message in status bar:
                refresh_status_bar(text=f"{lang[1]['Folder unhide: ']}'{folder._name}'", color=green)
            else:
                # Display error in status bar:
                refresh_status_bar(text=f"{lang[1]['Folder not found: ']}'{folder._name}'", color=red2)
                # Remove the folder from the list if it can no longer be found:

            # Save hide status in json file:
            save_data(db=True)

            # Update status of the folder in the listbox:
            refresh_listbox()


def un_hide_all(save=True, alert=True):
    """ Show all the folders in the list from the OS Interface """

    if not config['Elements']:
        if alert == 1:
            # Display error in status bar:
            return refresh_status_bar(text=lang[1]['There are no folders to show'], color=red2)

    # Get all the path in the list config[]:
    for folder in config['Elements']:
        if folder._hide == 1:
            cur_path = f'{folder._path}.{folder._name}'  # the actual name of the folder have a '.'

            if isdir(cur_path) == 1:  # control if the folder exist
                rename(cur_path, folder._fullpath)  # rename folder
                system(f'attrib -S -H "{folder._fullpath}" > nul')  # show the folder
                folder._hide = False  # change status

                if alert == 1:
                    # Display message in status bar:
                    refresh_status_bar(text=lang[1]['All the folders has been shown'], color=green)

            else:
                # Display error in status bar:
                refresh_status_bar(text=f"{lang[1]['Folder not found: ']}'{folder._name}'", color=red2)
                # Remove the folder from the list if it can no longer be found:

            # Save hide status in json file:
            if save == 1:
                save_data(db=True)

            # Update status of the folder in the listbox:
            refresh_listbox()


def delete_all():
    """ Clear the config list """

    def check_path(folder=None):
        """ Check if the folder exist and return boolean """
        return isdir(folder._fullpath)

    # Clear the config list:
    kill_list = [elem for elem in config['Elements'] if elem._hide == 0 or check_path(elem) == 0]
    if not kill_list:
        # Display error in status bar:
        return refresh_status_bar(text=lang[1]['There are no folders to delete'], color=red2)

    for elem in kill_list:
        config['Elements'].remove(elem)

    # Display message in status bar:
    refresh_status_bar(text=lang[1]['All the unhide folders has been deleted'], color=green)

    # Update the json:
    save_data(db=True)

    # Update the listbox
    refresh_listbox()


def listbox_path():
    """ Get the path of the selected folder in the list box """

    global sel_path

    sel = mylistbox.curselection()

    for index in reversed(sel):
        folder = config['Elements'][index]
        sel_path = folder._fullpath  # get path


def cur_selct(evt):
    """ Select an item from the listbox """

    try:
        # Get text from listbox (status symbol + name of the folder):
        # sel_listbox_text = str((mylistbox.get(mylistbox.curselection())))

        # Get path:
        sel = mylistbox.curselection()
        for index in reversed(sel):
            folder = config['Elements'][index]

            # Set folder path information into status bar:
            refresh_status_bar(text=folder._fullpath, color=gray1)
    except:
        # Refresh status bar:
        refresh_status_bar(text='', color=gray1)


def refresh_listbox():
    """ Update the listbox """

    # Try to clear the list:
    try: mylistbox.delete(0, END)  # clear list
    except:
        pass  # prevent from error if the list is empty

    # Load the items from config[] into listbox:
    for items in config['Elements']:
        if items._hide == 1:
            mylistbox.insert(END, '● ' + items._name)  # '●' symbol - hide status for the user

        elif items._hide == 0:
            mylistbox.insert(END, '○ ' + items._name)  # '○' symbol - un-hide status for the user


def refresh_status_bar(text, color):
    """ Refresh status bar """

    Label(root, text=text, bd=1, width=1, fg=color, bg=black2, relief=SUNKEN,
          anchor=W).grid(row=3, column=0, sticky=E + W)


def program_start(bckp_notf=False, login=True):  # 'bckp_notf=True' activate a message of 'load config correctly'
    """ Program main structure """

    # Tools:
    global root, mylistbox, folder_path
    root = Tk()
    folder_path = StringVar()

    # Load the background config:
    tk_bg = bg_confg()

    # Set background image in main window:
    # Up part:
    bg_l1 = Label(root, image=tk_bg, bg=black1)
    bg_l1.image = tk_bg
    bg_l1.place(x=0, y=0)
    # Down part:
    bg_l2 = Label(root, image=tk_bg, bg=black1)
    bg_l2.image = tk_bg
    bg_l2.place(x=0, y=80)

    # Hide main window for load all the components:
    root.withdraw()

    # List box:
    mylistbox = Listbox(root, width=31, height=8, font=('comicsans', 13), fg=gray1, bg=gray2)
    mylistbox.grid(row=2, column=0, sticky=N + S + E + W)
    mylistbox.bind('<<ListboxSelect>>', cur_selct)

    # List box vertical scroll bar:
    scrollbar1 = Scrollbar(orient=VERTICAL)
    scrollbar1.config(command=mylistbox.yview)
    scrollbar1.grid(row=2, column=1, padx=0, sticky=NW + S)
    mylistbox.config(yscrollcommand=scrollbar1.set)

    # Load status bar:
    refresh_status_bar(text='', color=gray2)

    if bckp_notf == 1:
        # Display message in status bar:
        refresh_status_bar(text=lang[1]['The backup has been loaded'], color=green)

    # Clear config['Elements']:
    config['Elements'] = []

    # Load config:
    try:
        load_data()

    except:
        # Try to recuperate configuration from backup database:
        if backup(_load=True, force=True) == 'no internet':  # load backup automatically

            # If backup fails with "no internet" then create a new config file:
            with open(join_p('config', 'data.cfg'), 'w'):
                # Message in english because without a config file it's not possible to know the language preference.
                # Display message in status bar:
                refresh_status_bar(text='A new config file has been made', color=gray1)

    # Load language dict:
    load_lang()

    # Windows style:
    root.title('Hidden Folder')
    root.configure(background=black1)
    root.resizable(False, False)

    # Set icon:
    set_ico(window_name=root, icon_data=ico_main)

    # Labels and buttons:
    def label_buttons(x1, x2, x3, x4, y):
        """ Label and buttons for main window """

        Label(text=lang[1]['Folder List'], fg=gray3, bg=black1, font=('comicsans', 14)).grid(row=0, column=0)
        Button(text=lang[1]['Add'], fg=gray3, bg=black2, cursor='hand2', font=('comicsans', 11),
               command=add_folder).place(x=x1, y=y)
        Button(text=lang[1]['Delete'], fg=red1, bg=black2, cursor='hand2', font=('comicsans', 11),
               command=delete_path).place(x=x2, y=y)
        Button(text=lang[1]['Hide'], fg=gray3, bg=black2, cursor='hand2', font=('comicsans', 11),
               command=hide).place(x=x3, y=y)
        Button(text=lang[1]['Show'], fg=gray3, bg=black2, cursor='hand2', font=('comicsans', 11),
               command=un_hide).place(x=x4, y=y)

    if config['Language'] == 'English':
        label_buttons(40, 90, 155, 210, 261)

    elif config['Language'] == 'Spanish':
        label_buttons(10, 73, 145, 230, 261)

    elif config['Language'] == 'Italian':
        label_buttons(10, 84, 152, 232, 261)

    # Call menu bar:
    menubar = Menu(root)

    # Menu bar - File (Add / Exit):
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label=lang[1]['Add'], command=add_folder, accelerator='Ctrl+A')
    filemenu.add_command(label=lang[1]['Clear'], command=alert_clear, accelerator='Ctrl+Alt+C')
    filemenu.add_separator()
    filemenu.add_command(label=lang[1]['Exit'], command=root.quit, accelerator='Ctrl+Q')
    menubar.add_cascade(label=lang[1]['File'], underline=0, menu=filemenu)

    # Menu bar - Edit (Show / Hide):
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label=lang[1]['Show'], command=un_hide, accelerator='Ctrl+D')
    editmenu.add_command(label=lang[1]['Show All'], command=un_hide_all, accelerator='Ctrl+Alt+D')
    editmenu.add_separator()
    editmenu.add_command(label=lang[1]['Hide'], command=hide, accelerator='Ctrl+H')
    editmenu.add_command(label=lang[1]['Hide All'], command=hide_all, accelerator='Ctrl+Alt+H')
    menubar.add_cascade(label=lang[1]['Edit'], underline=0, menu=editmenu)

    # Menu bar - Settings:
    settingmenu = Menu(menubar, tearoff=0)

    # Submenu - Language:
    lang_submenu = Menu(settingmenu, tearoff=0)
    lang_submenu.add_command(label=lang[1]['English'], command=lang_english)
    lang_submenu.add_command(label=lang[1]['Spanish'], command=lang_spanish)
    lang_submenu.add_command(label=lang[1]['Italian'], command=lang_italian)
    settingmenu.add_cascade(label=lang[1]['Language'], menu=lang_submenu, underline=0)

    # Submenu - Backup:
    backup_submenu = Menu(settingmenu, tearoff=0)
    backup_submenu.add_command(label=lang[1]['Activate'], command=activate_database)
    backup_submenu.add_command(label=lang[1]['Deactivate'], command=deactivate_database)
    backup_submenu.add_separator()
    backup_submenu.add_command(label=lang[1]['Save Backup'], command=save_to_database)
    backup_submenu.add_command(label=lang[1]['Load Backup'], command=load_from_database)
    settingmenu.add_cascade(label=lang[1]['Backup'], menu=backup_submenu, underline=0)

    # Submenu - Security:
    security_submenu = Menu(settingmenu, tearoff=0)
    security_submenu.add_command(label=lang[1]['Activate'], command=activate_security)
    security_submenu.add_command(label=lang[1]['Deactivate'], command=deactivate_security)
    security_submenu.add_separator()
    security_submenu.add_command(label=lang[1]['Reset Password'], command=reset_password)
    settingmenu.add_cascade(label=lang[1]['Security'], menu=security_submenu, underline=0)

    menubar.add_cascade(label=lang[1]['Settings'], underline=0, menu=settingmenu)

    # Menu bar - Help:
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label=lang[1]['? Help'], command=create_help_window, accelerator='F1')
    helpmenu.add_command(label=lang[1]['About'], command=create_about_window)
    menubar.add_cascade(label=lang[1]['Help'], underline=0, menu=helpmenu)

    # Set leds:
    status_led()

    # Shortcuts:
    def shortcut_1(event):
        add_folder()  # Add
    filemenu.bind_all('<Control-a>', shortcut_1)

    def shortcut_2(event):
        delete_all()  # Clear All
    filemenu.bind_all('<Control-Alt-c>', shortcut_2)

    def shortcut_3(event):
        sys_exit(0)  # Exit
    filemenu.bind_all('<Control-q>', shortcut_3)

    def shortcut_4(event):
        un_hide()  # Show
    editmenu.bind_all('<Control-s>', shortcut_4)

    def shortcut_5(event):
        un_hide_all()  # Show All
    editmenu.bind_all('<Control-Alt-s>', shortcut_5)

    def shortcut_6(event):
        hide()  # Hide
    editmenu.bind_all('<Control-d>', shortcut_6)

    def shortcut_7(event):
        hide_all()  # Hide All
    editmenu.bind_all('<Control-Alt-d>', shortcut_7)

    def shortcut_8(event):
        create_help_window()  # ?Help
    helpmenu.bind_all('<F1>', shortcut_8)

    # Display menu bar:
    root.config(menu=menubar)

    # Window size and position:
    size_config(name=root, width=300, height=300)

    if login is True:
        login_w()

    elif login is False:
        # Show the main window:
        root.deiconify()

    # Window loop:
    root.mainloop()  # keep open the program interface

    # Exit program:
    sys_exit(0)


if __name__ == '__main__':
    """ Program start here """

    file_gen()  # create program data directories and files
    program_start()
