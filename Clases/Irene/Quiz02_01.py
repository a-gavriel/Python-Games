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

temblores = []
#       8,9,10,11,12,13,14,15,16,17,18,19,20
annos = [0,0,0,0,0,0,0,0,0,0,0,0,0]
#       1,2,3,4,5,6,7,8,9,10,11,12
meses = [0,0,0,0,0,0,0,0,0,0,0,0,]
registro = []

# otra forma anno = [mes, cantidad, promedio de magnitud]

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
        archivo = input('Ingrese el nombre del archivo: ')
        datos = open(archivo, 'r', encoding = 'iso-8859-1')
        for line in datos:
            line = line.replace('\n', '')
            info = line.split(';')
            anno = info[0]
            mes = info[1]
            magnitud = info[2]
            temblores = [anno, mes, magnitud]
            registro.append(temblores)

            if anno == '2008':
                annos[0] += 1
            elif anno == '2009':
                annos[1] += 1
            elif anno == '2010':
                annos[2] += 1
            elif anno == '2011':
                annos[3] += 1
            elif anno == '2012':
                annos[4] += 1
            elif anno == '2013':
                annos[5] += 1
            elif anno == '2014':
                annos[6] += 1
            elif anno == '2015':
                annos[7] += 1
            elif anno == '2016':
                annos[8] += 1
            elif anno == '2017':
                annos[9] += 1
            elif anno == '2018':
                annos[10] += 1
            elif anno == '2019':
                annos[11] += 1
            elif anno == '2020':
                annos[12] += 1

            if mes == '1':
                meses[0] += 1
            elif mes == '2':
                meses[1] += 1
            elif mes == '3':
                meses[2] += 1
            elif mes == '4':
                meses[3] += 1
            elif mes == '5':
                meses[4] += 1
            elif mes == '6':
                meses[5] += 1
            elif mes == '7':
                meses[6] += 1
            elif mes == '8':
                meses[7] += 1
            elif mes == '9':
                meses[8] += 1
            elif mes == '10':
                meses[9] += 1
            elif mes == '11':
                meses[10] += 1
            elif mes == '12':
                meses[11] += 1

        i = 0
        j = 0
        while i < 13:
            while j < 12:
                print('Año {}, mes {}, temblores {}'.format(annos[i],meses[j],))
                j += 1
            j = 0
            i += 1

def cantidad_mes(lista,anno,mes):
    resultado = 0
    i = 0
    j = 0
    while i < len(lista):
        if lista[i][0] == anno and lista[i][1] == mes:
            resultado += 1




if opcion == '2':
        None

    if opcion == '3':
        None

