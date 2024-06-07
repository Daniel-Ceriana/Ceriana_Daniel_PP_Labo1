import json

def leer_json(nombre_archivo:str,primer_item:str)->list:
    try:

        with open(nombre_archivo,"r") as archivo:
            item = json.load(archivo)
        return item[primer_item]
    except FileNotFoundError:
        print("El archivo no existe")
        return False
    except KeyError:
        print("El archivo no contiene la key solicitada")

# lista = leer_json("data_stark.json","heroes")



def guardar_archivo(nombre_archivo:str,datos:str):
    '''
    genera archivo csv segun los datos pasados
    Parametros: nombre_archivo:str
                primer_linea:str
                lista:list => lista con cada diccionario como linea
    Retorno: True => todo funciono
            False=> error
    '''
    if len(datos)>0 and len(nombre_archivo)>0:
        try:
            with open(nombre_archivo,"w+") as archivo:
                archivo.write(datos)
                print("Se creó el archivo:",nombre_archivo)
                return True
        except:
            print("Error al crear el archivo:",nombre_archivo)
            return False    
    else:
        print("Error al crear el archivo, revise nombre y datos")
        return False    
    
        
def generar_csv(nombre_archivo:str,lista:list)->str:
    '''
    genera str con formato csv
    Parametros: nombre_archivo:str
                lista:list => lista con cada diccionario como linea
    Retorno:str=> str con formato csv
    '''
    if len(lista)>0:
        try:
            retorno = ""
            flag_cabecera = True
            for item in lista:
                linea = ""
                cabecera = ""
                for key in item.keys():
                    #separo los datos por guiones
                    linea += str(item[key])+","
                    cabecera += str(key)+","
                #limpio el ultimo guion
                linea = linea[:-1]
                cabecera = cabecera[:-1]
                if flag_cabecera:
                    retorno += cabecera + '\n'
                    flag_cabecera = False
                retorno += linea + "\n"
            print(guardar_archivo(nombre_archivo,retorno))
            return retorno
        except:
            print("Error al generar csv")

# print(generar_csv("ASD.csv",lista))
