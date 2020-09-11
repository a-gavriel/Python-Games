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

temblores = {}
annos = {}


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
        archivo = input('Ingrese el nombre del archivo: ') #abrir en ventana nueva
        datos = open(archivo, 'r', encoding = 'iso-8859-1')
        for line in datos:
            line = line.replace('\n', '')
            info = line.split(';')
            anno = info[0]
            mes = info[1]
            magnitud = info[2]
            temblores[info[0]] = [anno, mes, magnitud]
            #                      0    1       2
            datos[anno] = 0
            datos[anno + mes] = 0
            datos[anno + mes + magnitud] = 0

            if anno not in datos:
                datos[anno] = 0
                datos[anno + mes] = 0
                datos[anno + mes + magnitud] = 0
            else:
                if anno + mes not in datos:
                    datos[anno + mes] = 0
                    datos[anno + mes + magnitud] = 0
                elif anno + mes + magnitud not in datos:
                    datos[anno + mes + magnitud] = 0

                if anno == '2008':
                    datos[anno][0] += 1
                    datos[anno + mes][0] +=1
                    datos[anno + mes + magnitud][0] += 1
                elif anno == '2009':
                    datos[anno][1] += 1
                    datos[anno + mes][1] +=1
                    datos[anno + mes + magnitud][1] += 1
                elif anno == '2010':
                    datos[anno][2] += 1
                    datos[anno + mes][2] +=1
                    datos[anno + mes + magnitud][2] += 1
                elif anno == '2011':
                    datos[anno][3] += 1
                    datos[anno + mes][3] += 1
                    datos[anno + mes + magnitud][3] += 1
                elif anno == '2012':
                    datos[anno][4] += 1
                    datos[anno + mes][4] +=1
                    datos[anno + mes + magnitud][4] += 1

                for k,v in annos.items():
                    print('Para el año {} se registró una cantidad de {} temblores en {} meses con una magnitud promedio de {}'.format(k, v[0],v[1],v[2]))
                    for k2,v2 in v[1].items():
                        print('     Para el mes {} se registraron {} temblores con una magnitud promedio de {}'.format(k2, v2[0],v2[1]))



    if opcion == '2':
        None

    if opcion == '3':
        None

