from validacionesInt import *
from functools import reduce

def mostrar_menu(num1:int=0,num2:int=5):
    print("""    1) Cargar archivo.
    2) Imprimir lista de servicios.
    3) Asignar totales.
    4) Filtrar por tipo.
    5) Mostrar servicios ordenados por descripción de manera ascendente.
    6) Guardar servicios.
    7) Salir."""
        )
    opcion = pedir_int_rango(num1,num2)
    return opcion

def mostrar_submenu(num1:int=0,num2:int=4):
    print("""    1) Tipo 1.
    2) Tipo 2.
    3) Tipo 3.
    4) Salir."""
        )
    opcion = pedir_int_rango(num1,num2)
    return opcion


def mostrar_todos_los_datos_indices(indices:list,listas:list,lista_columnas=[""]):
    '''
    Muestra en la terminal todos los datos de los indices indicados
    Parametros: indices:list => indices a buscar
    Retorno: No
    '''
    separar_por_datos(lista_columnas)
    aux = ""
    for i in indices:
        for lista in listas:
            aux += f"{str(lista[i]):22}"        
        print(aux)
        aux = ""
        
def mostrar_un_dato(item:dict,lista_keys:list):
    '''
    Muestra en consola un item segun las keys indicadas
    Parametros: item:dict => diccionario con la informacion a mostrar (debe 
                                    tener las keys indicadas en lista_keys)
                lista_keys:list => lista con las keys a mostrar
    '''
    aux = ""
    for key in lista_keys: 
        try:
            if type(item[key])==str and item[key].replace(".", "").isdigit():
                
                aux_item = round(float(item[key]),2)
                aux += f"{str(aux_item):19}"
            else:
                aux += f"{str(item[key])[0:17]:19}"                  
        except(KeyError):
            aux += f"{"":19}"  
    print(aux,"\n")
    aux = ""
    
    
    
def mostrar_todos_los_datos(lista:list,lista_keys:list):
    '''
    Muestra en la terminal todos los datos de los indices indicados
    Parametros: indices:list => indices a buscar
    Retorno: No
    '''
    if len(lista) > 0 and len(lista_keys) > 0: 
        separar_por_datos(lista_keys)
    
        for item in lista:
            mostrar_un_dato(item,lista_keys)
    else:
        print("No se puede leer una lista vacia")

    
def separar_terminal(separador:str="---------------"):
    '''
    Separa la terminal con algun simbolo pasado por parametros
    Parametros: Separador:str => simbolo que indique la separacion,
                                Por defecto: "---------------"
    Retorno: no
    '''
    print(separador)
    
def separar_por_datos(columnas:list):
    '''
    Muestra en forma de columnas, las listas
    '''
    aux = ""
    for i in range(len(columnas)):
        aux += f"{str(columnas[i].capitalize()):19}"        
    print(aux)
    

def append_a_lista_int(lista_principal:list,lista_append:list,key:str):
    '''
    hace appends de los valores de los items[key], los transforma en int
    Parametros: lista_principal:list => lista con todos los items
                lista_append:list => lista a modificar 
                key:str => key a buscar para el append
    Retorno: no
    '''
    for item in lista_principal:
        lista_append.append(int(item[key]))
        
def append_a_lista(lista_principal:list,lista_append:list,key:str):
    '''
    hace appends de los valores de los items[key], sin importar el tipo
    Parametros: lista_principal:list => lista con todos los items
                lista_append:list => lista a modificar 
                key:str => key a buscar para el append
    Retorno: no
    '''
    for item in lista_principal:
        lista_append.append(item[key]) 
                
def append_a_lista_condicion(lista_principal:list,lista_append:list,key:str,condicion,valor_condicion):
    '''
    hace appends a una lista segun la condicion pasada por parametros
    Parametros: lista_principal:list => lista con todos los items
                lista_append:list => lista a modificar 
                key:str => keys a comparar (con la condicion)
                condicion => funcion que reciba dos parametros (item[keys] y parametro valor_condicion)
                valor_condicion => valor a comparar con la key de cada item
    retorno: no
    '''
    for item in lista_principal:
        if condicion(item[key],valor_condicion):
            lista_append.append(item) 



def mostrar_por_grupo(dic:dict):
    '''
    muestra en consola los items de un diccionario divididos en grupo
    Parametros: dic:dict => diccionario a recorrer
    Retorno: no
    '''
    for key in dic:
        print("\n")
        print(key,":\n")
        for item in dic[key]:
            print("    ",item["nombre"])
            
def agrupar(lista:list,key:str)->dict:
    '''
    agrupa items en un diccionario segun la key
    Parametros:  lista:list => lista de items
                key:str => key a comparar
    retorno: diccionario con los items separados por la key
    '''
    aux = {}
    for item in lista:
            if item[key].capitalize() in aux:
                aux[item[key].capitalize()].append(item)
            else:
                aux[item[key].capitalize()] = [item]
    return aux
                
def filtrar(lista:list,key:str,condicion:str):
    '''
    crea una sublista segun una key y condicion
    Parametros: lista:list => lista a filtrar
                key:str => key a buscar
                condicion:str => condicion a comparar
    '''
    sublista = []
    if len(lista) > 0 and len(key) > 0 and len(condicion) > 0:
        for item in lista:
            if item[key] == condicion:
                sublista.append(item)
    return sublista