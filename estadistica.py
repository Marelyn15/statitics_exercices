import statistics as st

grupo_control = [7,3,-4,14,2,5,22,-7,9,5]

grupo_tratamiento = [-6,5,9,4,4,12,37,5,3,3]

def estadisticas(grupo):
    media = st.mean(grupo)
    mediana = st.median(grupo)

    def media_recortada(lista, porcentaje):
        lista = sorted(lista)
        print(lista, porcentaje)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        print(numeros_quitar)
        i = 0
        while i < numeros_quitar:
            del lista[0]
            print(lista)
            del lista[-1]
            print(lista)
            i = i + 1
            print(i)
        return(lista)
    
    def media_acotada(lista, porcentaje):
        lista = sorted(lista)
        print(lista, porcentaje)
        porcentaje = porcentaje / 100
        digitos_en_lista = len(lista)
        numeros_quitar = digitos_en_lista * porcentaje
        print(numeros_quitar)
        i = 0
        while i < numeros_quitar:
            del lista[0]
            print(lista)
            i = i + 1
            print(i)
        return(lista)
    
    media_ya_recortada = st.mean(media_acotada(grupo, 10))
    media_ya_acotada = st.mean(media_recortada(grupo, 10))
    print(f"Estos son los resultados del {grupo}: la media es: {media}, la mediana es: {mediana}, la media recortada es:  {media_ya_recortada}, y la media recortada es:  {media_ya_acotada}")

estadisticas(grupo_control)
estadisticas(grupo_tratamiento)