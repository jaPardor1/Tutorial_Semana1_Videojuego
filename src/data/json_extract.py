
import json

def extraer_datos_json(directorio:str):
    
    #f = open('assets/cfg/window.json',"r")
    f = open(directorio,"r")
    data=json.loads(f.read())
    return data