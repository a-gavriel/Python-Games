'''
La Red Sismológica Nacional, dentro de su proyecto de investigación en el estudio de temblores de
Costa Rica, ha generado un archivo plano de los temblores registrados desde el 2008 al 2020, con el
siguiente detalle de la información
    1. Año del temblor registrado.
    2. Mes del temblor registrado.
    3. Grado del temblor registrado.
Usted ha sido contratado para hacer un programa que tome este archivo y realice las siguientes
acciones:
    1. Cargar archivo: debe solicitar el nombre del archivo para que sea cargado en la aplicación.
    2. Estadísticas por mes: se debe de generar un archivo .txt el cual debe contener el año, mes,
        cantidad de temblores del correspondiente mes y el promedio de los temblores que se
        registraron en ese mes.
    3. Estadísticas por año: se debe de generar un archivo .txt el cual debe contener el año, cantidad de
        temblores registrados en ese año y el promedio de los temblores registrados en ese año.
'''

# Irene Castro Lobo

registros = []


def cargar_archivo(archivo_nombre):
    archivo = open(archivo_nombre, 'r', encoding='iso-8859-1')
    for line in archivo:
        line = line.replace('\n', '')
        info = line.split(';')
        anno = info[0]
        mes = info[1]
        magnitud = float(info[2].replace(",","."))
        temblor = (anno, mes, magnitud)
        registros.append(temblor) #

    archivo.close()


def estadisticas(modo):    
    if modo == 1: # estad1sticas por mes
        anno_x_mes = []
        sumamag_tot = []
        # primero se generan dos listas, una contiene el (año,mes) y la otra en la misma posición [cantidad total de temblores, suma total de magnitudes]
        for (anno, mes, magnitud) in registros:        
            if (anno,mes) in anno_x_mes:
                i = anno_x_mes.index( (anno,mes) )
                sumamag_tot[i][0] += 1
                sumamag_tot[i][1] += magnitud
            else:
                anno_x_mes.append( (anno,mes) )
                sumamag_tot.append([1,magnitud])   

        total_regs = len(anno_x_mes)
        for i in range(total_regs):
            (anno,mes) = anno_x_mes[i]
            tot_mags = sumamag_tot[i][0]           
            suma_mags =  sumamag_tot[i][1] 
            promedio = suma_mags / tot_mags
            print(f"año {anno} mes {mes}, promedio {promedio}")


    else: #estadisticas por año
        annos = []
        sumamag_tot = []
        # primero se generan dos listas, una contiene el año y la otra en la misma posición [cantidad total de temblores, suma total de magnitudes]
        for (anno, mes, magnitud) in registros:        
            if anno in annos:
                i = annos.index( anno )
                sumamag_tot[i][0] += 1
                sumamag_tot[i][1] += magnitud
            else:
                annos.append( anno )
                sumamag_tot.append([1,magnitud])

        total_regs = len(annos)
        for i in range(total_regs):            
            tot_mags = sumamag_tot[i][0]           
            suma_mags =  sumamag_tot[i][1] 
            promedio = suma_mags / tot_mags
            print(f"año {annos[i]}, promedio {promedio}")


seguir = True
while seguir:
    print('Bienvenido a La Red Sismológica Nacional')
    print('Menú principal')

    print('1. Cargar archivo')
    print('2. Estadísticas por mes')
    print('3. Estadísticas por año')
    print('4. Salir')

    opcion = input('Por favor seleccione una de las opciones anteriores: ')
    print('---------------------------------------------------------------')

    if opcion == '4':
        seguir = False

    if opcion == '1':
        archivo_nombre = input('Ingrese el nombre del archivo: ')  # abrir en ventana nueva
        cargar_archivo(archivo_nombre)
        

        i = 0
        cantidad = 0
        largo = len(registros)
        while i < largo:
            if registros[i][0] == '2008':
                cantidad += 1
            elif registros[i][0] == '2009':
                cantidad += 1

            i += 1
