from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QTableWidget, QTableWidgetItem, QLabel)


class DibujarTabla(QWidget):
    '''
    Clase encargada de dibujar tablas
    '''
    filas = 0
    columnas = 0
    tablachida = None

    def __init__(self, matriz, maximo):
        '''
        Inicializa la clase con la matriz a dibujar y un número dado por parámetro que decidirá como se dibujará
        :param matriz: Matriz a dibujar
        :param maximo: Numero entero que decidirá forma de pintar
        '''
        super().__init__()
        self.initUI(matriz, maximo)

    def initUI(self, matriz, maximo):
        '''
        Dibuja la matriz
        :param matriz: La matriz a dibujar
        :param maximo: número que decidirá cómo se pinta
        '''

        # Le damos valores al número de filas y columnas y ocultamos las cabezaras
        self.filas = len(matriz)
        self.columnas = len(matriz[0])
        self.tablachida = QTableWidget(self.filas, self.columnas, self)
        self.tablachida.horizontalHeader().hide()
        self.tablachida.verticalHeader().hide()
        self.tablachida.resizeColumnsToContents()

        # llenamos la matriz, si maximo es -1, la llenamos con continental, sino la llenamos con pasos de liebre
        for i in range(self.filas):
            for j in range(self.columnas):
                if maximo == -1:
                    self.setWindowTitle('Continental tablero final')
                    nuevo = QTableWidgetItem(str(matriz[i][j]))
                    if matriz[i][j] == "1":
                        nuevo.setBackground(Qt.red)
                    elif matriz[i][j] == "0":
                        nuevo.setBackground(Qt.yellow)
                    else:
                        nuevo.setBackground(Qt.black)
                    self.tablachida.setItem(i, j, nuevo)
                else:
                    if matriz[i][j] is None or matriz[i][j] == 0:
                        nuevo = QTableWidgetItem("")
                        self.tablachida.setItem(i, j, nuevo)
                    else:
                        self.setWindowTitle('Recorrido del conejo')
                        nuevo = QTableWidgetItem(str(matriz[i][j]))
                        if matriz[i][j] == 1:
                            nuevo.setBackground(Qt.red)
                        elif matriz[i][j] == maximo-1:
                            nuevo.setBackground(Qt.blue)
                        self.tablachida.setItem(i, j, nuevo)


        # Quitamos los scrolls y ponemos visible la matriz
        self.tablachida.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablachida.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablachida.setMaximumSize(self.getQTableWidgetSize())
        self.tablachida.setMinimumSize(self.getQTableWidgetSize())
        self.show()

    def getQTableWidgetSize(self):
        '''
        Metodo para obtener el tamaño del componenete de tablas
        :return: el tamaño de la tabla
        '''
        w = self.tablachida.verticalHeader().width() - 4  # +4 seems to be needed
        for i in range(self.tablachida.columnCount()):
            w += self.tablachida.columnWidth(i) - 4  # seems to include gridline (on my machine)
        h = self.tablachida.horizontalHeader().height() - 4
        for i in range(self.tablachida.rowCount()):
            h += self.tablachida.rowHeight(i) - 5
        return QtCore.QSize(w, h)
