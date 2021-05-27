class Juego:
    '''
    Clase que representa el juego continental
    '''

    ruta = "historial_continental.txt"
    archivo = open(ruta, 'w')


    tablero= [[' ', ' ', '1', '1', '1', ' ', ' '],
             [' ', ' ', '1', '1', '1', ' ', ' '],
             ['1', '1', '1', '1', '1', '1', '1'],
             ['1', '1', '1', '0', '1', '1', '1'],
             ['1', '1', '1', '1', '1', '1', '1'],
             [' ', ' ', '1', '1', '1', ' ', ' '],
             [' ', ' ', '1', '1', '1', ' ', ' ']]

    alto = len(tablero)
    largo = len(tablero[alto - 1])
    fichas = 32
    DIRECCIONES = ["ARRIBA", "DERECHA", "ABAJO", "IZQUIERDA"]

    def __init__(self):
        '''
        Inicializa el juego
        '''
        self.ejecutar()

    def ejecutar(self):
        '''
        Imprime el tablero y trata de encontrar la solución, si no puede imprime un mensaje de proceso fallido
        '''
        self.imprimirTablero()
        self.archivo.write("Resolviendo..."+'\n')

        # print("Resolviendo..."+'\n')

        if not self.encontrarSolucion():
            self.archivo.write("Solución NO encontrada!")
            #print("Solución NO encontrada!")


    def imprimirTablero(self):
        '''
        Imprime el tablero en un txt
        '''
        self.archivo.write("----------------------------------------------------------------" + '\n')
        for i in range(self.alto):
            self.archivo.write('.'.join(self.tablero[i])+'\n')

        # Aquí lo imprime por consola
        #print("----------------------------------------------------------------" + '\n')
        #for i in range(self.alto):
            #print('.'.join(self.tablero[i]) + '\n')

    def encontrarSolucion(self):
        if (self.fichas == 1 and self.tablero[3][3] == '1'):
            self.archivo.write("Solución Encontrada!!"+'\n')
            # print("Solución Encontrada!!"+'\n')
            self.imprimirTablero()
            return True
        else:
            '''
            Se recorre el tablero junto a sus posibles direcciones
            '''
            for i in range(self.largo):
                for j in range(self.alto):
                    for k in range(len(self.DIRECCIONES)):
                        movimiento = self.calcularMovimientos(j, i, self.DIRECCIONES[k]) #1. se verifican todos los posibles movimientos
                        if self.validarMovimiento(movimiento):  #2. se verifica si el movimiento es válido
                            self.realizarMovimiento(movimiento) #3. se realiza el movimiento.
                            self.imprimirTablero()  #4. Si se ha encontrado la solución, la ejecución para, de lo contrario sigue iterando

                            if self.encontrarSolucion():
                                return True
                            self.deshacer(movimiento) # 5. Si el movimiento es inválido, los deshace
            return False

    '''Método que evalua todos los posibles movimientos'''

    def calcularMovimientos(self, fila, columna, direccion):
        '''
        Crea y llena una matriz de 3x2 que contiene los indices de movimiento de la ficha
        :param fila: filas
        :param columna: columnas
        :param direccion: dirección que se va a revisar
        :return: la matriz de movimiento
        '''
        move = []
        for i in range(3):
            move.append([])
            for j in range(2):
                move[i].append(None)


        '''La posición 0,0 tendrá la fila de incio'''
        move[0][0] = fila

        '''La posición 0,1 tendrá la columna de inicio'''
        move[0][1] = columna

        if direccion == "ARRIBA":
            move[1][0] = fila - 1
            move[1][1] = columna
            move[2][0] = fila - 2
            move[2][1] = columna

        elif direccion == "IZQUIERDA":
            move[1][0] = fila
            move[1][1] = columna - 1
            move[2][0] = fila
            move[2][1] = columna - 2

        elif direccion == "DERECHA":
            move[1][0] = fila
            move[1][1] = columna + 1
            move[2][0] = fila
            move[2][1] = columna + 2

        elif direccion == "ABAJO":
            move[1][0] = fila + 1
            move[1][1] = columna
            move[2][0] = fila + 2
            move[2][1] = columna
        return move

    def validarMovimiento(self, movimiento):
        '''
        Verifica que un movimiento sea válido
        '''

        '''Verificamos si la casilla destino se encuentra dentro del tablero, es decir es menor o igual a 7, o mayor a 0'''
        if movimiento[2][0] >= 7 or movimiento[2][1] >= 7 or movimiento[2][0] < 0 or movimiento[2][1] < 0:
            return False

        else:

            '''En caso de ser un movimiento válido, simplemente le indicamos los valores de las casillas de nuestro tablero inicial'''
            return self.tablero[movimiento[0][0]][movimiento[0][1]] == '1' and self.tablero[movimiento[1][0]][movimiento[1][1]] == '1' and \
               self.tablero[movimiento[2][0]][movimiento[2][1]] == '0'

    def realizarMovimiento(self, movimiento):

        '''Una vez validado los movimientos, se procede a realizarlo.
        Para esto se establece la casilla de inicio con un valor de 0, lo que indica vacía
        Se establece la casilla sobre la cual saltamos con un valor de 0, lo que indica vacía
        Se establece la casilla final con un valor de 1, lo que indica que esta llena.
        Finalmente disminuimos el número de fichas en 1.'''

        self.tablero[movimiento[0][0]][movimiento[0][1]] = '0'
        self.tablero[movimiento[1][0]][movimiento[1][1]] = '0'
        self.tablero[movimiento[2][0]][movimiento[2][1]] = '1'

        self.fichas = self.fichas - 1

    def deshacer(self, movimiento):

        '''En caso de que el movimmiento no sea válido, se deshace.'''

        self.archivo.write("Deshacer"+'\n')
        #print("Deshacer"+'\n')

        self.tablero[movimiento[0][0]][movimiento[0][1]] = '1'
        self.tablero[movimiento[1][0]][movimiento[1][1]] = '1'
        self.tablero[movimiento[2][0]][movimiento[2][1]] = '0'

        self.fichas = self.fichas + 1