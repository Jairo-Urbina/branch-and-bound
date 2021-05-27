import sys
import tkinter as tk
from tkinter import messagebox

from PyQt5.QtWidgets import QApplication

import vista.VenatanPrincipal as principal
from modelo.Liebre import Liebre
from util.dibujarTabla import DibujarTabla


class Ventana_L:
    def __init__(self, ventana):
        '''
        Inicializa lso componentes de esta ventana
        :param ventana: Ventana a la que se añadirán los componententes
        '''

        # ===================================PROPIEDADES DE LA VENTANA====================================
        ventana.title("Rama y poda")
        ventana.geometry('380x300')
        ventana.configure(background='light slate blue')

        titulo = tk.Label(ventana, text="EL SALTO DE LA LIEBRE", bg="light slate blue", fg="black")
        titulo.config(font=("Calibri Light", 16, "italic"))
        titulo.place(x=100, y=15)
        # =================================================VARIABLES=======================================

        fila = tk.StringVar()
        colum = tk.StringVar()
        p = tk.StringVar()
        q = tk.StringVar()
        xInicio = tk.StringVar()
        xFinal = tk.StringVar()
        yInicio = tk.StringVar()
        yFinal = tk.StringVar()

        tablero = tk.StringVar()
        movimientos = tk.StringVar()

        # ========================================LABEL Y ENTRADAS DE TEXTO ==================================================
        label_fila = tk.Label(ventana, text="Filas", bg="light slate blue", fg="black")
        label_fila.place(x=90, y=70)
        label_fila.config(font=("Calibri Light", 11, "italic"))

        txt_Fila = tk.Entry(ventana, textvariable=fila)
        txt_Fila.place(x=160, y=70)
        txt_Fila.config(width=6)

        label_colum = tk.Label(ventana, text="Columnas", bg="light slate blue", fg="black")
        label_colum.place(x=90, y=100)
        label_colum.config(font=("Calibri Light", 11, "italic"))
        txt_colum = tk.Entry(ventana, textvariable=colum)
        txt_colum.place(x=160, y=100)
        txt_colum.config(width=6)

        label_p = tk.Label(ventana, text="P", bg="light slate blue", fg="black")
        label_p.place(x=235, y=70)
        label_p.config(font=("Calibri Light", 11, "italic"))
        txt_p = tk.Entry(ventana, textvariable=p)
        txt_p.place(x=265, y=70)
        txt_p.config(width=6)

        label_q = tk.Label(ventana, text="Q", bg="light slate blue", fg="black")
        label_q.place(x=235, y=100)
        label_q.config(font=("Calibri Light", 11, "italic"))
        txt_q = tk.Entry(ventana, textvariable=q)
        txt_q.place(x=265, y=100)
        txt_q.config(width=6)

        label_Xinicio = tk.Label(ventana, text="X Inicio", bg="light slate blue", fg="black")
        label_Xinicio.place(x=90, y=130)
        label_Xinicio.config(font=("Calibri Light", 11, "italic"))
        txt_xInicio = tk.Entry(ventana, textvariable=xInicio)
        txt_xInicio.place(x=160, y=130)
        txt_xInicio.config(width=6)

        label_XFinal = tk.Label(ventana, text="X Final", bg="light slate blue", fg="black")
        label_XFinal.place(x=220, y=130)
        label_XFinal.config(font=("Calibri Light", 11, "italic"))
        txt_XFinal = tk.Entry(ventana, textvariable=xFinal)
        txt_XFinal.place(x=265, y=130)
        txt_XFinal.config(width=6)

        label_Yinicio = tk.Label(ventana, text="Y Inicio", bg="light slate blue", fg="black")
        label_Yinicio.place(x=90, y=160)
        label_Yinicio.config(font=("Calibri Light", 11, "italic"))
        txt_YInicio = tk.Entry(ventana, textvariable=yInicio)
        txt_YInicio.place(x=160, y=160)
        txt_YInicio.config(width=6)

        label_YFinal = tk.Label(ventana, text="Y Final", bg="light slate blue", fg="black")
        label_YFinal.place(x=220, y=160)
        label_YFinal.config(font=("Calibri Light", 11, "italic"))
        txt_YFinal = tk.Entry(ventana, textvariable=yFinal)
        txt_YFinal.place(x=265, y=160)
        txt_YFinal.config(width=6)

        # ====================================MÉTODOS AUXILIARES IMPLEMENTADOS EN LOS BOTONES==================================

        def limpiar():
            '''
            Vacía todos los campos
            '''
            fila.set("")
            colum.set("")
            p.set("")
            q.set("")
            xInicio.set("")
            yInicio.set("")
            xFinal.set("")
            yFinal.set("")
            tablero.set("")
            movimientos.set("")

        def validar():
            '''
            Valida la información de los campos
            '''

            ItemFila = (fila.get())
            ItemColum = (colum.get())
            Itemp = (p.get())
            Itemq = (q.get())
            ItemXinicio = (xInicio.get())
            ItemYinicio = (yInicio.get())
            ItemXfinal = (xFinal.get())
            ItemYfinal = (yFinal.get())

            if not (ItemFila.isdigit() and ItemColum.isdigit() and Itemp.isdigit() and
                    Itemq.isdigit() and ItemXinicio.isdigit() and ItemYinicio.isdigit()
                    and ItemXfinal.isdigit() and ItemYfinal.isdigit()):
                messagebox.showwarning("¡¡ERROR!!", "Datos inválidos, ingrese únicamente números enteros")
            elif ItemXinicio > ItemFila or ItemYinicio >  ItemColum:
                messagebox.showwarning("¡¡ERROR!!", "El punto de inicio está fuera de rango")
            elif ItemXfinal > ItemFila or ItemYfinal >  ItemColum:
                messagebox.showwarning("¡¡ERROR!!", "El punto de llegada está fuera de rango")
            elif ItemXinicio == ItemXfinal and ItemYinicio == ItemYfinal:
                    messagebox.showwarning("¡¡ERROR!!", "El punto de llegada no puede ser igual al de partida")
            else:
                board = None
                liebre = None
                try:
                    liebre = Liebre(int(ItemFila), int(ItemColum), int(Itemp), int(Itemq), int(ItemXinicio),
                                    int(ItemYinicio), int(ItemXfinal), int(ItemYfinal))
                    board = liebre.rama_poda()
                    tablero.set(board.tablero)
                    messagebox.showinfo("Movimientos", "Hubo "+str(liebre.movimientosPosibles / 2)+" movimientos")
                except:
                    messagebox.showwarning("Sin solución", "No hay solución :/")
                try:
                    app = QApplication(sys.argv)
                    ex = DibujarTabla(board.tablero, liebre.movimientosPosibles)
                    sys.exit(app.exec_())
                except:
                    pass
        def cambio():
            '''
            Destruye los componenetes y pasa a la ventana principal
            '''
            titulo.destroy()
            label_fila.destroy()
            label_colum.destroy()
            txt_Fila.destroy()
            txt_colum.destroy()
            label_p.destroy()
            label_q.destroy()
            txt_p.destroy()
            txt_q.destroy()
            txt_xInicio.destroy()
            txt_XFinal.destroy()
            txt_YInicio.destroy()
            txt_YFinal.destroy()
            label_Xinicio.destroy()
            label_XFinal.destroy()
            label_Yinicio.destroy()
            label_YFinal.destroy()
            botonAceptar.destroy()
            botonAtras.destroy()
            botonLimpiar.destroy()

            aplicacion = principal.Principal(ventana)
            ventana.mainloop()

        # ======================================BOTONES================================================================

        botonAceptar = tk.Button(ventana, text="Aceptar", fg='black', command=validar)
        botonAceptar.place(x=145, y=200)

        botonLimpiar = tk.Button(ventana, text="Limpiar", fg='black', command=limpiar)
        botonLimpiar.place(x=210, y=200)

        botonAtras = tk.Button(ventana, text="Atrás", fg='black', command=cambio)
        botonAtras.place(x=10, y=240)
