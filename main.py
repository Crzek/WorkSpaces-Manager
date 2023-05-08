from app import App

import subprocess
import os

ACTIVE_APP_FILE = "data/active_apps.txt"
WORK_SPACES = []


def writesAppToTxt(app_list):
    listaAPP = list()
    with open(ACTIVE_APP_FILE, 'w') as archivo:
        for app in app_list:
            if len(app) > 3:
                app_separate = app.split()
                app_separate = cleanList(app_separate)
                if ((app_separate != None) and (len(app_separate) > 3)):
                    name_app = app_separate[0]
                    id_app = app_separate[1]
                    description_app = desplit(app_separate[2:])
                    app = App(name_app, id_app, description_app)
                    listaAPP.append(app)
                    archivo.write(f"{name_app}.exe {id_app}\n")
    return listaAPP


def desplit(array):
    text = ""
    for word in array:
        if word == array[0]:
            text = word
        text = f"{text} {word}"
    return text


def openAPPbyName():
    # abrir las aplicaciones listadas en el archivo
    with open(ACTIVE_APP_FILE, 'r') as archivo:
        for linea in archivo:
            linea = cleanList(linea.split())
            if (linea != None):

                # aplicacion = linea.strip()  # eliminar caracteres en blanco al inicio y final
                # ejecutar la aplicación con el comando start
                os.system(f"start {linea[0]}")


def readTXT():
    listApp = list()
    with open(ACTIVE_APP_FILE, "r") as archivo:
        for lineas in archivo:
            if (cleanList(lineas) != None):
                pass


def procesosInWindows():
    result = subprocess.run(['powershell.exe', '-Command',
                            'Get-Process | Where-Object {$_.MainWindowTitle} | Where-Object {$_.Responding -eq $true} | Select-Object Name,id,MainWindowTitle'], capture_output=True)
    try:
        output = result.stdout.decode("utf-8")
    except:
        output = result.stdout.decode("latin-1") 

    app_list = output.split("\n")

    return app_list


def cleanList(appList):
    if ("Name" in appList) or ("Id" in appList):
        return None
    elif (("-" in appList[0])):
        return None
    return appList


def opcion():
    print("1. Leer Achivos en ejecucion")
    print("2. Abrir Archivos en Ejecucion")

    opcion = int(input("Introduce 1-2:"))
    if opcion == 1:
        return opcion
    elif opcion == 2:
        return opcion
    else:
        return False


def printWSlist():
    for ws in WORK_SPACES:
        ws.printWSpace()


# MAIN
proocesWindows = procesosInWindows()

select_opcion = False
counter = 0
while (not select_opcion) and (counter < 3):
    user_opcion = opcion()
    if (user_opcion == 1):
        appList = writesAppToTxt(proocesWindows)
        WORK_SPACES.append(appList)
        select_opcion = True
    elif (user_opcion == 2):
        printWSlist()
        openAPPbyName()
        select_opcion = True
    counter += 1
