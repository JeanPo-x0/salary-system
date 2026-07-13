
from rich.console import Console

console = Console(highlight=False)

COLOR_TITULO = "#C9A15A"      # dorado champagne, para el título principal
COLOR_SUBTITULO ="#1DD6C0"    # cian/turquesa suave
COLOR_ERROR = "#F42B3C"    # rojo fuerte
COLOR_EXITO ="#EF88C9"            # Rosa polvo cálido
COLOR_DIA = "#B0A8B9"      # gris-lila suave, para el separador de cada día
COLOR_PREGUNTA ="#DF2B9A"         # mauve/rosa-morado
COLOR_RESUMEN = "#DC17BF"    # rosa-crema pastel, solo para "---- RESUMEN DE EL DIA ----"
COLOR_SEPARADOR = "#A8967E"    # beige-dorado apagado, para las líneas ====
COLOR_DESPEDIDA =  "#AA18BD"      # rosa final


# Variables

hora1 = 1800
hora2 = 1600
monto_indefinido = 0
multiplicacion_hora_extra = 1.5


#Funciones 

def horas_extra():
     
     while True:
         
         console.print("\nSe trabajaron horas extra?", style=COLOR_DIA)
         console.print("Ingrese si o no: ", style=COLOR_PREGUNTA, end="")
         respuesta = str(input()).lower().strip()

         if respuesta == "si":
             while True:
                 try:
                    console.print("Horas extra: ", style=COLOR_PREGUNTA, end="")
                    horas = int(input())
                    console.print("Minutos extra adicionales (0-59): ", style=COLOR_PREGUNTA, end="")
                    minutos = int(input())
                    if 0 <= horas <= 12 and 0 <= minutos <= 59:
                        total_extra = horas + (minutos / 60)
                        return total_extra
                    else:
                        console.print("\n¡¡Las horas extra deben estar entre 0 y 12, y los minutos entre 0 y 59!!", style=COLOR_ERROR)

                 except ValueError:
                     console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR)
         
         elif respuesta == "no":
             return 0
         
         else:
            console.print("\n¡¡Respuesta inválida, escriba 'si' o 'no'!!", style=COLOR_ERROR)
    


def horas_almuerzo():

    while True:
        console.print("\n¿El trabajador tomo la hora de almuezo?",style=COLOR_DIA)
        console.print("Ingrese si o no: ", style=COLOR_PREGUNTA, end="")
        respuesta = input().lower().strip()

        if respuesta == "si":
             while True:
                 try:
                    console.print("¿Cuantas horas de almuerzo tomo?: ", style=COLOR_PREGUNTA, end="")
                    hora_de_almuerzo = int(input())

                    if 0 <= hora_de_almuerzo <= 3:
                        return hora_de_almuerzo
                    else:
                        console.print("\n¡¡La hora de almuerzo debe estar en un rango de 0 y 3!!", style=COLOR_ERROR)

                 except ValueError:
                     console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR)
        
        elif respuesta == "no" or respuesta == "":        
            return 0
        
        else:
            console.print("\n¡¡Respuesta inválida, escriba 'si' o 'no'!!", style=COLOR_ERROR)


def trys():

    while True:
        try:
            console.print("Horas trabajadas: ", style=COLOR_PREGUNTA, end="")
            horas = int(input())
            console.print("Minutos adicionales (0-59): ", style=COLOR_PREGUNTA, end="")
            minutos = int(input())
            if 0 <= horas <= 24 and 0 <= minutos <= 59:
                total_horas = horas + (minutos / 60)
                return total_horas
            else:
                console.print("\n¡¡Las horas deben estar entre 0 y 24, y los minutos entre 0 y 59!!", style=COLOR_ERROR)

        except ValueError:
            console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR) 



def tarifas():

    global monto_indefinido

    while True:
        try:
            console.print("\nIngrese una opcion: ", style=COLOR_PREGUNTA, end="")
            opcion = int(input())

            if opcion == 1 or opcion == 2 or opcion == 3:

                if opcion == 3:

                    while True:
                        try:
                            console.print("\nIngrese el monto a pagar por hora: ", style=COLOR_PREGUNTA, end="")
                            monto = int(input())

                            if 500 <= monto <= 2200:
                                monto_indefinido = monto
                                return opcion
                            else: 
                                console.print("\n¡¡El precio a pagar tiene que estar en un rango de ₡500 a ₡2200!!", style=COLOR_ERROR)

                        except ValueError:
                            console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR)
                            continue

                return opcion 
            else:
                console.print("\n¡¡Opción inválida, ingrese 1, 2 o 3!!", style=COLOR_ERROR)

        except ValueError:
            console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR)




def formato_colones(numero):

    return f"₡{numero:,.0f}".replace(",", ".")


def formato_horas(horas_decimal):
    """Convierte horas decimales a formato horas:minutos para mostrar"""
    horas_enteras = int(horas_decimal)
    minutos = int((horas_decimal - horas_enteras) * 60 + 0.5) 
    return f"{horas_enteras}:{minutos:02d}h"


def pedir_continuar():

    while True:
        console.print("\n¿Quiere hacer otro calculo? ( Si/No ) ", style=COLOR_SUBTITULO, end="")
        respuesta = input().lower().strip()

        if respuesta == "si" or respuesta == "no":
            return  respuesta 
        else:
            console.print('\n¡¡Respuesta inválida, escriba "Si" para continuar o "No" para salir!!', style=COLOR_ERROR)


def opcion_de_semanas():

    while True:
        try:
            console.print("\nIngrese una opcion: ", style=COLOR_PREGUNTA, end="")
            opcion = int(input())

            if opcion == 1 or opcion == 2:
                return opcion

        except ValueError:
            console.print("\n¡¡Solo se permiten números, intente de nuevo!!", style=COLOR_ERROR)
        
        
        else:
            console.print("\n¡¡Opción inválida, ingrese 1 o 2!!", style=COLOR_ERROR)


# Inicio de el sistema 


console.print("\n======== eME.SISTEM ;) ========", style=COLOR_TITULO)
console.print("\n¿Cuantas semanas desea calcular?", style=COLOR_SUBTITULO)
console.print("\nOpcion 1: (Una semana)", style=COLOR_DIA)
console.print("Opcion 2: (Dos semanas)", style=COLOR_DIA)
opcionX = opcion_de_semanas()

if opcionX == 1:

        while True:
            hora_de_almuerzo = 0
            semana1_total = 0
            semana_fecha_actual = None
            registro = []
          

            console.print("\n===== SISTEMA DE SALARIOS =====", style=COLOR_TITULO)

            console.print("\nNombre de el trabajador: ", style=COLOR_PREGUNTA, end="")
            Nombre = input().title()
            console.print('Fecha "Ej: XX de Junio": ', style=COLOR_PREGUNTA, end="")
            fecha = input().title()

# Loop 

            for semana in range(1):
                
                if semana == 0:
                    console.print("\n===== Semana 1 =====", style=COLOR_TITULO)

                for dia in range(1):
                    console.print('\nIngrese el dia de la semana "Ej: Lunes": ', style=COLOR_PREGUNTA, end="")
                    Dia_semana = input().title()
                    console.print("¿Donde se realizo el trabajo?: ", style=COLOR_PREGUNTA, end="")
                    lugar_de_trabajo = input().title()
                    console.print("Descripcion de lo que realizo: ", style=COLOR_PREGUNTA, end="")
                    labor = input().title()
                    horas_trabajadas = trys()
                    extra = horas_extra()
                    hora_almuerzo = horas_almuerzo()

                    info = {"Semana": semana, "Dia": Dia_semana, "Ubicacion": lugar_de_trabajo, "Descripcion": labor, "Horas de trabajo": horas_trabajadas, "Extras": extra, "Almuerzo": hora_almuerzo }
                    registro.append(info)

# Opciones de horas
            console.print("\n===== ¿A cuanto se le va a pagar la hora? =====", style=COLOR_SUBTITULO)
            console.print("\n--- Escoja una opcion ---", style=COLOR_TITULO)
            console.print("\nOpcion 1: ₡1.800", style=COLOR_DIA)
            console.print("Opcion 2: ₡1.600", style=COLOR_DIA)
            console.print("Opcion 3: (Asignar un monto)", style=COLOR_DIA)
            opcion1 = tarifas()

            if opcion1 == 1:
                tarifa = hora1
    
            elif opcion1 == 2:
                tarifa = hora2

            elif opcion1 == 3:
                tarifa = monto_indefinido

# Calculo 

            for i in registro:
                
                if i["Semana"] != semana_fecha_actual:
                    semana_fecha_actual = i["Semana"]
                    console.print(f"\n########## RESULTADOS SEMANA {semana_fecha_actual + 1} ##########\n", style=COLOR_TITULO)

                if i["Extras"] == 0:
                    total_dia = (i["Horas de trabajo"] - i["Almuerzo"]) * tarifa 
                    almuerzo_texto = f'Almorzó {formato_horas(i["Almuerzo"])}' if i["Almuerzo"] > 0 else '"No" tomo la hora de almuerzo.'
                    console.print(f'---- RESUMEN DE EL DIA ----\n', style=COLOR_SUBTITULO)
                    console.print(f'FECHA: "{fecha}"\n', style=COLOR_DIA)
                    print(f'Dias: {i['Dia']}.\nTrabajo realizado en: {i['Ubicacion']}.\nDescripcion del trabajo: {i['Descripcion']}.\nHoras de trabajo: {formato_horas(i['Horas de trabajo'])}\n{almuerzo_texto}\n"No" se trabajaron horas extra!!\n')
                    console.print(f"El total del dia de {Nombre} es de {formato_colones(total_dia)}\n", style=COLOR_EXITO)
        
                elif i["Extras"] > 0:
                    total_dia = (i["Horas de trabajo"] - i["Almuerzo"]) * tarifa  + (i["Extras"] * tarifa  * multiplicacion_hora_extra)
                    almuerzo_texto = f'Almorzó {formato_horas(i["Almuerzo"])}' if i["Almuerzo"] > 0 else '"No" almorzó.'
                    console.print(f'---- RESUMEN DE EL DIA ----\n', style=COLOR_SUBTITULO)
                    console.print(f'FECHA: "{fecha}"\n', style=COLOR_DIA)
                    print(f"Dias: {i['Dia']}.\nLugar de trabajo: {i['Ubicacion']}.\nDescripcion del trabajo: {i['Descripcion']}.\nHoras de trabajo: {formato_horas(i['Horas de trabajo'])}\n{almuerzo_texto}\nTrabajo un total de {formato_horas(i['Extras'])} extras!!\n")
                    console.print(f"El total del dia de {Nombre} es de {formato_colones(total_dia)}\n", style=COLOR_EXITO)
        
                if i["Semana"] == 0:
                    semana1_total += total_dia

            semana_total = semana1_total

            console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
            console.print(f'       ----- RESULTADO FINAL (1 semana) -----\n', style=COLOR_TITULO)
            print(f"  El total de la Semana 1 de {Nombre} es de {formato_colones(semana1_total)}")
            console.print(f"       --- Total de la semana {formato_colones(semana_total)} ---", style=COLOR_EXITO)   
            console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
    
# ---- Preguntar si continuar o salir ----
            continuar = pedir_continuar()
            if continuar == "no":
                console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
                console.print("--- Gracias por usar el sistema ¡¡Hasta luego!! ;) ---", style=COLOR_DESPEDIDA)
                console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
                break


elif opcionX == 2:

    while True:
        hora_de_almuerzo = 0
        semana1_total = 0
        semana2_total = 0
        semana_fecha_actual = None
        registro = []
          

        console.print("\n===== SISTEMA DE SALARIOS =====", style=COLOR_TITULO)

        console.print("\nNombre de el trabajador: ", style=COLOR_PREGUNTA, end="")
        Nombre = input().title()
        console.print('Fecha "Ej: XX de Junio": ', style=COLOR_PREGUNTA, end="")
        fecha = input().title()

# Loop 

        for semana in range(2):

            if semana == 0:
                console.print("\n===== Semana 1 =====", style=COLOR_TITULO)

            elif semana > 0:
                console.print("\n===== Semana 2 =====", style=COLOR_TITULO)
                
            for dia in range(1):
                console.print('\nIngrese el dia de la semana "Ej: Lunes": ', style=COLOR_PREGUNTA, end="")
                Dia_semana = input().title()
                console.print("¿Donde se realizo el trabajo?: ", style=COLOR_PREGUNTA, end="")
                lugar_de_trabajo = input().title()
                console.print("Descripcion de lo que realizo: ", style=COLOR_PREGUNTA, end="")
                labor = input().title()
                horas_trabajadas = trys()
                extra = horas_extra()
                hora_almuerzo = horas_almuerzo()

                info = {"Semana": semana, "Dia": Dia_semana, "Ubicacion": lugar_de_trabajo, "Descripcion": labor, "Horas de trabajo": horas_trabajadas, "Extras": extra, "Almuerzo": hora_almuerzo }
                registro.append(info)

# Opciones de horas
        console.print("\n===== ¿A cuanto se le va a pagar la hora? =====", style=COLOR_SUBTITULO)
        console.print("\n--- Escoja una opcion ---", style=COLOR_TITULO)
        console.print("\nOpcion 1: ₡1.800", style=COLOR_DIA)
        console.print("Opcion 2: ₡1.600", style=COLOR_DIA)
        console.print("Opcion 3: (Asignar un monto)", style=COLOR_DIA)
        opcion1 = tarifas()

        if opcion1 == 1:
            tarifa = hora1
    
        elif opcion1 == 2:
            tarifa = hora2

        elif opcion1 == 3:
            tarifa = monto_indefinido

# Calculo 

        for i in registro:
            
            if i["Semana"] != semana_fecha_actual:
                semana_fecha_actual = i["Semana"]
                console.print(f"\n########## RESULTADOS SEMANA {semana_fecha_actual + 1} ##########\n", style=COLOR_TITULO)

            if i["Extras"] == 0:
                total_dia = (i["Horas de trabajo"] - i["Almuerzo"]) * tarifa 
                almuerzo_texto = f'Almorzó {formato_horas(i["Almuerzo"])}' if i["Almuerzo"] > 0 else '"No" tomo la hora de almuerzo.'
                console.print(f'---- RESUMEN DE EL DIA ----\n', style=COLOR_SUBTITULO)
                console.print(f'FECHA: "{fecha}"\n', style=COLOR_DIA)
                print(f'Dias: {i['Dia']}.\nTrabajo realizado en: {i['Ubicacion']}.\nDescripcion del trabajo: {i['Descripcion']}.\nHoras de trabajo:  {formato_horas(i['Horas de trabajo'])}\n{almuerzo_texto}\n"No" se trabajaron horas extra!!\n')
                console.print(f"El total del dia de {Nombre} es de {formato_colones(total_dia)}\n", style=COLOR_EXITO)
        
            elif i["Extras"] > 0:
                total_dia = (i["Horas de trabajo"] - i["Almuerzo"]) * tarifa  + (i["Extras"] * tarifa  * multiplicacion_hora_extra)
                almuerzo_texto = f'Almorzó {formato_horas(i["Almuerzo"])}' if i["Almuerzo"] > 0 else '"No" almorzó.'
                console.print(f'---- RESUMEN DE EL DIA ----\n', style=COLOR_SUBTITULO)
                console.print(f'FECHA: "{fecha}"\n', style=COLOR_DIA)
                print(f"Dias: {i['Dia']}.\nLugar de trabajo: {i['Ubicacion']}.\nDescripcion del trabajo: {i['Descripcion']}.\nHoras de trabajo:  {formato_horas(i['Horas de trabajo'])}\n{almuerzo_texto}\nTrabajo un total de {formato_horas(i['Extras'])} extras!!\n")
                console.print(f"El total del dia de {Nombre} es de {formato_colones(total_dia)}\n", style=COLOR_EXITO)
        
            if i["Semana"] == 0:
                semana1_total += total_dia
            elif i["Semana"] == 1:
                semana2_total += total_dia

        semanas_totales = semana1_total + semana2_total

        console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
        console.print(f'       ----- RESULTADO FINAL (QUINCENA) -----\n', style=COLOR_TITULO)
        print(f"  El total de la Semana 1 de {Nombre} es de {formato_colones(semana1_total)}")
        print(f"  El total de la Semana 2 de {Nombre} es de {formato_colones(semana2_total)}")
        console.print(f"       --- Total de la quincena {formato_colones(semanas_totales)} ---", style=COLOR_EXITO)   
        console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
    
# ---- Preguntar si continuar o salir ----
        continuar = pedir_continuar()
        if continuar == "no":
            console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
            console.print("--- Gracias por usar el sistema ¡¡Hasta luego!! ;) ---", style=COLOR_DESPEDIDA)
            console.print("\n=======================================================\n", style=COLOR_SEPARADOR)
            break