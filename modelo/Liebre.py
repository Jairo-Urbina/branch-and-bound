from modelo.PasosLiebre import *


class Liebre:
    '''
    Clase que representa una liebre en un tablero
    '''
    filas = 0
    columnas = 0
    p = 0
    q = 0
    saltos = []

    xInicio = 0
    yInicio = 0

    xFinal = 0
    yFinal = 0

    soluciones = []
    solucion = None
    movimientosPosibles = 0

    def __init__(self, f, c, p, q, xi, yi, xf, yf):
        '''
        Inicializa al conejo y el tablero con los datos por parámetro
        :param f: número de filas del tablero
        :param c: número de columnas del tablero
        :param p: número de pasos que se puede dar horizontalmente
        :param q: número de pasos que se puede dar verticalmente
        :param xi: posición inicial de x
        :param yi: posición incial de y
        :param xf: posición final de x
        :param yf: posición final de y
        '''
        self.filas = f
        self.columnas = c

        self.p = p
        self.q = q

        self.xInicio = xi
        self.yInicio = yi

        self.xFinal = xf
        self.yFinal = yf

        self.saltos_inicio()

    def inicializar(self):
        '''
        LLena el tablero inicial con ceros y los bordes con None
        '''
        tablero_inicial = []
        # LLENAMOS LA MATRIZ INICIAL CON NONE
        for i in range(self.filas):
            tablero_inicial.append([])
            for j in range(self.columnas):
                tablero_inicial[i].append(None)

        for i in range(1, self.filas):
            for j in range(1, self.columnas):
                tablero_inicial[i][j] = 0
        return tablero_inicial

    def saltos_inicio(self):
        '''
        Se inicializa la matriz de saltos
        :return:
        '''
        if self.p != self.q:

            # LLENAMOS LA MATRIZ DE SALTOS CON NONE DE 8X2
            for i in range(8):
                self.saltos.append([])
                for j in range(2):
                    self.saltos[i].append(None)

            self.saltos[0][0] = self.p
            self.saltos[0][1] = self.q

            self.saltos[1][0] = self.q
            self.saltos[1][1] = self.p

            self.saltos[2][0] = -self.q
            self.saltos[2][1] = self.p

            self.saltos[3][0] = -self.p
            self.saltos[3][1] = self.q

            self.saltos[4][0] = -self.p
            self.saltos[4][1] = -self.q

            self.saltos[5][0] = -self.q
            self.saltos[5][1] = -self.p

            self.saltos[6][0] = self.q
            self.saltos[6][1] = -self.p

            self.saltos[7][0] = self.p
            self.saltos[7][1] = -self.q
            self.movimientosPosibles = 8
        else:
            # LLENAMOS LA MATRIZ DE SALTOS CON NONE DE 4X2
            for i in range(4):
                self.saltos.append([])
                for j in range(2):
                    self.saltos[i].append(None)

            self.saltos[0][0] = self.p
            self.saltos[0][1] = self.q

            self.saltos[1][0] = -self.q
            self.saltos[1][1] = self.p

            self.saltos[2][0] = -self.p
            self.saltos[2][1] = -self.q

            self.saltos[3][0] = self.p
            self.saltos[3][1] = -self.q
            self.movimientosPosibles = 4

    def saltar(self, xInicio, yInicio, valor, tablero):
        '''
        Se crea un salto en el tablero con los datos dados por parámetro
        :param xInicio: posición incial del salto en x
        :param yInicio: posición incial del salto en y
        :param valor: valor del salto
        :param tablero: tablero sobre el que se va a saltar
        '''
        movX = 0
        movY = 0
        movimientos = 0

        while (movimientos < self.movimientosPosibles):
            movimientos += 1

            movX = xInicio + self.saltos[movimientos - 1][0]
            movY = yInicio + self.saltos[movimientos - 1][1]

            if (movX == self.xFinal and movY == self.yFinal):
                tablero[movX][movY] = valor
                self.solucion = PasosLiebre(self.filas, self.columnas)

                self.solucion.tablero = self.copiarMatriz(tablero)
                self.solucion.movimietos_posibles(self.filas, self.columnas)
                self.soluciones.append(self.solucion)

                tablero[movX][movY] = 0
                break
            if (movX >= 1) and (movX <= self.filas) and (movY >= 1) and (movY <= self.columnas) and (
                    tablero[movX][movY] == 0):
                tablero[movX][movY] = valor
                self.saltar(movX, movY, valor + 1, tablero)
                tablero[movX][movY] = 0

    def rama_poda(self):
        '''
        Genera la matriz resultante mediante el mecanismo rama y poda
        :return: Matriz de saltos resultante
        '''
        tablero = self.inicializar()
        tablero[self.xInicio][self.yInicio] = 1
        self.saltar(self.xInicio, self.yInicio, 2, tablero)

        menorMov = float("inf")
        mejor = None

        while (len(self.soluciones) != 0):
            act = self.soluciones[0]
            if act.movimientos <= menorMov:
                menorMov = act.movimientos
                mejor = act
            self.soluciones.pop(0)
        return mejor

    def copiarMatriz(self, tablero):
        '''
        Copia una matriz dada por parámetro y retorna la copia
        :param tablero: matriz a copiar
        :return: Matriz nueva copiada
        '''
        # CREAMOS Y LLEAMOS UNA MATRIZ ABC CON NULL
        abc = []
        for i in range(self.filas + 1):
            abc.append([])
            for j in range(self.columnas + 1):
                abc[i].append(None)

        for i in range(self.columnas):
            for j in range(self.filas):
                abc[j][i] = tablero[j][i]
        return abc

