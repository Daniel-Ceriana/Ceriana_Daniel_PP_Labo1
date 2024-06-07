from validacionesInt import *
from functools import reduce

def mostrar_menu(num1:int=0,num2:int=5):
    print("""    1. Listar ordenado por Nombre.
    2. Listar Masculinos débiles.
    3. Cantidad por color de ojos.
    4. Listar por color de Pelo.
    5. Listar inteligencia.
    6. Listar Promedio.
    7. Asignar IMC.
    8-Salir"""
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
    
    separar_por_datos(lista_keys)
  
    for item in lista:
        mostrar_un_dato(item,lista_keys)

    
def separar_terminal(separador:str="---------------"):
    '''
    Separa la terminal con algun simbolo pasado por parametros
    Parametros: Separador:str => simbolo que indique la separacion,
                                Por defecto: "---------------"
    Retorno: no
    '''
    print(separador)
    
def promediar(lista:list)->float:
    '''
    Parametros: lista:list => datos a promediar
    retorno: float => resultado del promedio
    '''
   
    acumulador = reduce(lambda a,b: float(a)+float(b),lista) 
        #validar que no se divida por 0
    return round(acumulador / len(lista),2)


def separar_por_datos(columnas:list):
    '''
    Muestra en forma de columnas, las listas
    '''
    aux = ""
    for i in range(len(columnas)):
        aux += f"{str(columnas[i].capitalize()):19}"        
    print(aux)
    
def buscar_extremo(lista:list,mayor:int=1)->float:
    '''
    Parametros:
            mayor:int=1 => si es 1, busca al numero mayor de la lista, sino
                            al menor 
    '''
    num = lista[0]
    for i in range(len(lista)):
        if mayor == 1:
            if num < lista[i]:
                num = lista[i]
        else:
            if num > lista[i]:
                num = lista[i]
    return num

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


def buscar_debiles(lista:list)->list:
    '''
    busca a los items de menor fuerza
    Parametros: lista:list => lista de items
    retorno: lista con los items que cumplan la condicion
    '''
    lista_fuerza = []
    lista_retorno = []
    
    #busca los valores "fuerza" y los agrega a la lista
    append_a_lista_int(lista,lista_fuerza,"fuerza")        
    
    #busca el menor valor "fuerza"
    menor_fuerza = buscar_extremo(lista_fuerza,0)
    
    #lambda para verificar igualdad
    condicion = lambda valor1,valor2: valor1 == valor2
    
    #agrega a la lista retorno, los items que contengan a la menor fuerza
    append_a_lista_condicion(lista,lista_retorno,"fuerza",condicion,str(menor_fuerza))
    return lista_retorno



#generalizar, en vez de genero usar key, y el otro str se puede elegir despues
def buscar_genero(lista:list,genero:str="m")->list:
    '''
    busca en una lista de items por genero
    Parametros: lista:list => lista de items
                genero:str="m" => genero a buscar, por defecto "m"
    '''
    lista_genero = []
    condicion = lambda valor1,valor2: valor1.lower() == valor2
    append_a_lista_condicion(lista,lista_genero,"genero",condicion,genero)
    return lista_genero


def contar_cantidad_repetidos(lista:list,key:str):
    '''
    Cuenta cuantas veces se repite el valor de la key en la lista
    Parametros: lista:list => lista a recorrer
                key:str => key a buscar, su valor tiene que ser str dentro del item
    '''
    aux = {}
    for item in lista:
        if item[key].capitalize() in aux:
            aux[item[key].capitalize()] += 1
        else:
            aux[item[key].capitalize()] = 1
    return aux


def buscar_por_pelo(lista:list,key:str):
    '''
    agrupa items en un diccionario segun la key, aunque contenga dos valores
            separados por un "/"
    Parametros:  lista:list => lista de items
                key:str => key a comparar
    retorno: diccionario con los items separados por la key
    '''
    aux = {}
    for item in lista:
        if not "/" in item[key]:
            if item[key].capitalize() in aux:
                aux[item[key].capitalize()].append(item)
            else:
                aux[item[key].capitalize()]=[item]
        else:
            #clasifica a los que tienen varios colores en ambas categorias
            #ej: white/brown pasa a white y a brown
            #       y no crea una categoria "white/brown"
            colores_aux = item[key].split("/")
            for color in colores_aux:
                color_normalizado = color.capitalize().strip()
                if color_normalizado in aux:
                    aux[color_normalizado].append(item)
                else:
                    aux[color_normalizado]=[item]
    return aux

# def agrupar_para_mostrar(dic:dict):
#     aux_datos=[]
#     for key in dic:
#         aux_datos.append(dic[key])
#     append_a_lista(dic)

# def mostrar_por_color_pelo(dic:dict):
#     keys = []
#     items = []
#     for key in dic:
#         keys.append(key)
#         for item in dic[key]:
#             items.append({"nombre":item["nombre"],key:key})
#     # print("Color de pelo:")
    
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

def buscar_mayor_o_menor_a(lista:list,num:float,mayor:bool = True)->list:
    '''
    busca en una lista a los numeros mayores o menores al indicado
    Parametros: lista:list => lista a recorrer
                num:float => numero de referencia
                mayor:bool = True => True = Busca mayor
                                     False = Busca menor
    Retorno: ->list 
    '''
    lista_retorno = []
    for numero in lista:    
        if mayor:
            if numero > num:
                lista_retorno.append(num)
        else:
            if numero < num:
                lista_retorno.append(num)
                
def buscar_items_mayor_menor_a(lista:list,key:str,num,mayor:bool=True)->list:
    '''
    Busca los items de una lista que sean mayor o menor de un numero
    Parametros: lista:list => lista a recorrer
                key:str => key a comparar
                num:float => numero de referencia
                mayor:bool = True => True = Busca mayor
                                     False = Busca menor
    retorno: ->list => lista con los items que cumplen con la condicion
    '''
    lista_aux = []
    for item in lista:
        if mayor:
            if float(item[key]) > num:
                lista_aux.append(item) 
        else:
            if float(item[key]) < num:
                lista_aux.append(item)
    return lista_aux


def asignar_imc(lista:list):
    '''
    calcula y asigna el imc de todos los items de una lista
    Parametros: lista:list => lista con los items
    retorno:no
    '''
    for item in lista:
        peso_item = float(item["peso"])
        #paso la altura a Metros
        altura_item = float(item["altura"])/100
        # item["imc"] = round((lambda peso,altura: peso/(altura**2))
        #                     (peso_item,altura_item),2) 
        