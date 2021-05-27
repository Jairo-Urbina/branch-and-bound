import sys
import subprocess
from PyQt5.QtWidgets import QApplication
from modelo.Continental import Juego
import vista.VenatanPrincipal as principal
import tkinter as tk
from util.dibujarTabla import DibujarTabla


class Ventana_C:
    '''
    Ventana del juego continental de la aplicación
    '''

    def __init__(self, ventana):
        '''
        Inicializa los componentes de esta ventana
        :param ventana: Ventana a la que se añadirán los componententes
        '''
        # ===================================PROPIEDADES DE LA VENTANA====================================
        ventana.title("Backtracking")
        ventana.geometry('380x300')
        ventana.configure(background='light slate blue')

        titulo = tk.Label(ventana, text="EL CONTINENTAL", bg="light slate blue", fg="black")
        titulo.config(font=("Calibri Light", 16, "italic"))
        titulo.place(x=0, y=7, width=380, height=30)

        a = tk.Label(ventana, text="Al darle al botón se creará un archivo con el historial de movimientos \ny se mostrará la posición final del tablero", bg="light slate blue", fg="black")
        a.config(font=("Calibri Light", 10, "italic"))
        a.place(x=0, y=40, width=380, height=30)

        b = tk.Label(ventana, text="Nota: el proceso podría tardar algunos segundos", bg="light slate blue", fg="black")
        b.place(x=0, y=250, width=380, height=30)

        fr = tk.Frame(ventana)
        fr.place(x=80, y=70)

        tableroFinal = tk.StringVar()



        # =================================================VARIABLES=======================================
        tablero = [[' ', ' ', '1', '1', '1', ' ', ' '],
                   [' ', ' ', '1', '1', '1', ' ', ' '],
                   ['1', '1', '1', '1', '1', '1', '1'],
                   ['1', '1', '1', '0', '1', '1', '1'],
                   ['1', '1', '1', '1', '1', '1', '1'],
                   [' ', ' ', '1', '1', '1', ' ', ' '],
                   [' ', ' ', '1', '1', '1', ' ', ' ']]

    # ============================================ LABEL Y TEXTO ====================================================

        for i, block_row in enumerate(tablero):
            for j, block in enumerate(block_row):
                text = tk.Label(fr, text=block)
                text.grid(row=i, column=j)
                text.config(width=4)

    # ====================================MÉTODOS AUXILIARES IMPLEMENTADOS EN LOS BOTONES========================

        def ejecutar():
            '''
            Ejecuta el juego continental y pinta la versión final del tablero y el historial en un block de notas
            '''

            modelo = Juego()
            tablero = modelo.tablero
            subprocess.Popen(["notepad", "historial_continental.txt"])
            try:
                app = QApplication(sys.argv)
                ex = DibujarTabla(tablero, -1)
                sys.exit(app.exec_())
            except:
                print("cerrando table...")

        def devolver():
            '''
            Destruye los componenetes y pasa a la ventana principal
            '''

            titulo.destroy()
            text.destroy()
            fr.destroy()
            btnAtras.destroy()
            btnEjecutar.destroy()

            aplicacion = principal.Principal(ventana)
            ventana.mainloop()

    #=================================================== BOTONES ===============================================

        btnEjecutar = tk.Button(ventana, text="Ejecutar", fg='black', command= ejecutar)
        btnEjecutar.place(x=80, y=230)

        btnAtras = tk.Button(ventana, text="Atrás", fg='black', command=devolver)
        btnAtras.place(x=280, y=230)



