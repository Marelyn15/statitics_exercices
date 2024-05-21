import statistics as st
import math

grupo_control = [3.4,2.5,4.8,2.8,3.3,5.6,4.4,4.0,5.2,2.9,3.7,3.0,3.6,2.8,4.8]
group = [7, 3, -4, 14, 2, 5, 22, -7, 9, 5]
group2 = [-6, 5, 9, 4, 4, 12, 37, 5, 3, 3]

def estadisticas(grupo):
    #----------Funciones estadisticas ---------------------------
    media = round(st.mean(grupo),2)
    mediana = round(st.median(grupo),2)
    tamanio = len(grupo)

    #--------------Funciones hechas ----------------------------------
    def media_acotada_dos_lados(lista, porcentaje):
        lista = sorted(lista)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        i = 0
        while i < numeros_quitar:
            del lista[0]
            del lista[-1]
            i = i + 1
        return(lista)
    
    def media_acotada(lista, porcentaje):
        lista = sorted(lista)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        i = 0
        while i < numeros_quitar:
            del lista[0]
            i = i + 1
        return(lista)
    
    def varianza(lista):
        largo = tamanio - 1
        all_values = []
        for i in lista:
            element = (i - media) ** 2
            all_values.append(element)
        all_values = sum(all_values)
        resultado = 1 / largo * (all_values)
        return resultado
    
    def estandar(lista):
        largo = tamanio - 1
        all_values = []
        for i in lista:
            element = (i - media) ** 2
            all_values.append(element)
        all_values = sum(all_values)
        resultado = 1 / largo * (all_values)
        return round(math.sqrt(resultado),2)



    #-----------------------resultados-----------------------------------------------------------------
    calculo_varianza = round(varianza(grupo),2)
    desviancion_estandar = estandar(grupo)
    media_ya_acotada_dos_lados = round(st.mean(media_acotada_dos_lados(grupo, 10)),2)
    media_ya_acotada = round(st.mean(media_acotada(grupo, 10)),2)


    #---------------------resultado final--------------------------------------------------------------
    print(f"Estos son los resultados del {grupo}: el tamaño es: {tamanio} la media es: {media}, la mediana es: {mediana}, la media acortada es a dos lados:  {media_ya_acotada_dos_lados}, la media acortada es: {media_ya_acotada}, la varianza es {calculo_varianza}, y la desviación estándar es {desviancion_estandar}")
    
#estadisticas(grupo_control)
estadisticas(group)
estadisticas(group2)
#estadisticas(grupo_tratamiento)