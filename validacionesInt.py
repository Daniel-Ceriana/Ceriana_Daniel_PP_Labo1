
def verificar_int_rango(num:int,desde:int,hasta:int)->bool:
    '''
    verifica que el numero este dentro del rango
    parametros: num:int -> numero a verificar
                desde:int, hasta:int -> rango
    retorno: bool -> esta dentro del rango o no
    '''
    retorno = False
    if(num >= desde and num <= hasta):
        retorno = True

    return retorno

def pedir_int(texto:str = "ingrese un numero entero: ")->int:
    '''
    Pide numero entero al usuario, no termina hasta que sea correcto
    parametros: texto:str, el texto que va a ver el usuario cuando se le pide el numero
    retorno: int => devuelve el input casteado a int cuando es correcto
    '''
    while True:
        numero = input(texto)
        if numero.isdigit():
            return int(numero)

#pedir numero entre rango
def  pedir_int_rango(desde:int,hasta:int, texto = "ingrese un numero entero: ")->int:
    '''
        Pide por input un numero, lo acepta cuando esta dentro del rango
        parametros: desde y hasta para determinar rango. texto a mostrar al pedir el input
        devuelve el numero(int) solo cuando esta dentro del rango
    '''
    while True:
        numero = pedir_int(texto)
        if verificar_int_rango(numero,desde,hasta):
            return numero
        else:
            print("-----Verifique las condiciones y vuelva a intentarlo-----")
# print(pedir_int_rango(0,10))
            

        
        


##funcion como parametro
def pedir_int_condicion(func, texto:str)->int:
    '''
    pide un int y verifica que cumpla una condicion
    parametros: func:function(:int)->bool: =>funcion que reciba un int
                                             como parametro y que devuelva
                                            bool, habiendo verificado
                                            una condicion
                texto:str => texto a mostrar al pedir input
    return ->int devuelve el numero una vez cumpla con la condicion
    '''
    while True:
        num = pedir_int(texto)
        if(func(num)):
            print("ES VALIDO")
            return num
        else:
            print("NO ES VALIDO")

def es_par_int(num:int)->bool:
    '''
    verifica que el int sea par
    parametros: num:int entero a verificar
    return: bool, es o no es par
    '''
    if(num % 2 == 0):
        return True
    else:
        return False

# pedir_int_condicion(es_par_int,"Ingrese un numero que sea par: ")