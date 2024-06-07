from funciones_generales import *
from funciones_archivos import *

datos_importados = False
datos = []
datos_ordenados = False
while True:
    separar_terminal()
    opcion = mostrar_menu(1,7)
    if opcion > 1 and opcion < 7 and datos_importados == False:
        print("---- Importe el archivo antes de continuar ----")
    else:
        match opcion:
            case 1:
                keys = ["id_servicio","descripcion","tipo",
                        "precioUnitario",
                        "cantidad",
                        "totalServicio"]
                datos = leer_json_lista("data.json")
                if datos:
                    print("Datos importados de forma exitosa")
                    datos_importados = True
            case 2:
                keys = ["id_servicio","descripcion","tipo",
                        "precioUnitario",
                        "cantidad",
                        "totalServicio"]
                mostrar_todos_los_datos(datos,keys)
            case 3:
                keys = ["id_servicio","descripcion","tipo",
                        "precioUnitario",
                        "cantidad",
                        "totalServicio"]
                for item in datos:
                    item["totalServicio"] = (lambda cant,precio: cant *
                                             precio)(float(item["cantidad"]),
                                                     float(item["precioUnitario"]))
            case 4:
                opcion_submenu = mostrar_submenu(1,4)
                if(opcion_submenu < 4):
                    lista_filtrada = filtrar(datos,"tipo",str(opcion_submenu))
                    guardar_json_lista(f"datos_filtrados_por_tipo_{opcion_submenu}.json",lista_filtrada)
            case 5:
                keys = ["id_servicio","descripcion","tipo",
                        "precioUnitario",
                        "cantidad",
                        "totalServicio"]
                datos.sort(key=lambda item: item["descripcion"],reverse=False)
                datos_ordenados = True
                mostrar_todos_los_datos(datos,keys)
            case 6:
                if(datos_ordenados):
                    guardar_json_lista("datos_ordenados.json",datos)
                else:
                    print("Ordene los datos antes de guardar")
            case 7:
                print("Saliendo del programa")
                break
