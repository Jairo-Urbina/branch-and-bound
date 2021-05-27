# coding=utf-8
class Nutricion:
    '''
    Clase que representa el problema del nutrionista
    '''

    I = float("inf")  # Representación de número infinito

    def _init_(self):
        pass

    def calcular(self, lista, n, c):
        '''
        Calcula las
        :param lista: La lista de platos disponibles
        :param n: cantidad de platos
        :param c: calorías máximas
        :return: Tabla de valores entre 0, infinito y valores enteros
        '''
        max_elemento = n+1
        max_cantidad = c+1

        tabla = []
        # CREAMOS UNA MATRIZ DE TAMAÑO (max_elemento)x(max_cantidad) y la llenamos de None
        for i in range(max_elemento):
            tabla.append([])
            for j in range(max_cantidad):
                tabla[i].append(None)
        # Llena la primera columna de la matriz con 0's
        for i in range(max_elemento):
            tabla[i][0] = 0
        # Llena la primera fila de la matriz con infinito(Excepto la primera casilla que ya está llena con un 0
        for i in range(1, max_cantidad):
            tabla[0][i] = self.I
        # La matriz quedaría de esta forma
        # [0, inf, inf, inf....etc]
        # [0, None, None, .....etc]
        # [0, None, None, .....etc]
        # ..etc
        a=0
        b=0
        # Estos 2 for se encargan de ir llenando lo faltante de la matriz, puede quedar con infinito, 0, o un entero
        for i in range(1, max_elemento):
            for j in range(1, max_cantidad):
                a = tabla[i-1][j]
                if(lista[i-1] <= j):
                    b = tabla[i-1][j-lista[i-1]]
                    if(b < self.I):
                        b += lista[i-1]
                else:
                    b = lista[i-1]

                if(b >= j):
                    tabla[i][j] = min(a, b)
                else:
                    tabla[i][j] = self.I

        return tabla


    def resultado(self, t, l, n, c):
        '''

        :param t: tabla de valores
        :param l: lista de platos
        :param n: cantidad de platos
        :param c: caloráis máximas
        :return: lista de platos seleccionados
        '''
        r = []
        i = n
        j = c

        while(i > 0 and j > 0):
            if(t[i][j] == t[i-1][j]):
                i -= 1
            else:
                r.append(i-1)
                j -= l[i - 1]
                i -= 1
        return r


    def resolver(self, lista, c):
        '''
       Escoge las mejores conbinaciones de platos para obtener las calorias necesarias
       :param lista: La lista de platos con sus calorías
       :param c: El máximo de calorías
       :return: Los platos escogidos con sus calorías respectivas y las calorías totales
       '''
        tabla = self.calcular(lista, len(lista), c)

        r = self.resultado(tabla, lista, len(lista), c)

        suma = 0
        rta= []
        for i in r:
            valor = i
            suma += lista[valor]
            x = 'plato' + str(valor+1) + ' = ' + str(lista[valor]) + ' calorias'
            rta.append(x)
        x = 'Total consumido: ' + str(suma) + ' calorias'
        rta.append(x)
        return rta



