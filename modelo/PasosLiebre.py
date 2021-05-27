class PasosLiebre:
    '''
    clase que representa los pasos a dar por la liebre para llegar al destino
    '''
    tablero = []
    movimientos = 0

    def __init__(self, f, c):
        '''
        Inicializa los pasos de la liebre con los datos por parámetro
        :param f: filas del tablero
        :param c: columnas del tablero
        '''
        self.movimientos = -1

        # Llenar la matriz con ceros con medidas (f+1)x(c+1)
        for i in range(f+1):
            self.tablero.append([])
            for j in range(c+1):
                self.tablero[i].append(0)



    def movimietos_posibles(self, f, c):
        '''
        Calcula el máximo de movimientos posibles dentro de la matriz dada
        :param f: filas de la matriz a calcular
        :param c: columas de la matriz a calcular
        '''
        for i in range(1, f):
            for j in range(1, c):
                if self.tablero[i][j] != 0:
                    self.movimientos += 1
