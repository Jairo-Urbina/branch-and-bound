import tkinter as tk
import vista.ventanaContinental as ventanaC
import vista.VentanaLiebre as ventanaL
import vista.VistaNutricion as ventanaN

class Principal():
    '''
    Ventana principal de la aplicación
    '''
    def __init__(self, ventana):
        '''
        Inicializa lso componentes de esta ventana
        :param ventana: Ventana a la que se añadirán los componententes
        '''
    #---------------------------
        ventana.title("Proyecto Final")
        ventana.geometry('400x400')
        ventana.configure(background='light slate blue')
        titulo = tk.Label(ventana, text="¡¡BIENVENIDO!!", bg="light slate blue", fg="black")
        titulo.config(font=("Calibri Light", 16 , "italic"))
        titulo.place(x=130, y=15)

        u = tk.Label(ventana, text="UNIVERSIDAD EL BOSQUE", bg="light slate blue", fg="black")
        u.config(font=("Calibri Light", 9, "italic"))
        u.place(x=10, y=290)

        f = tk.Label(ventana, text="FACULTAD DE INGENIERÍA", bg="light slate blue", fg="black")
        f.config(font=("Calibri Light", 9, "italic"))
        f.place(x=10, y=310)

        pr = tk.Label(ventana, text="INGENIERÍA DE SISTEMAS", bg="light slate blue", fg="black")
        pr.config(font=("Calibri Light", 9, "italic"))
        pr.place(x=10, y=330)

        com = tk.Label(ventana, text="COMPLEJIDAD ALGORÍTMICA", bg="light slate blue", fg="black")
        com.config(font=("Calibri Light", 9, "italic"))
        com.place(x=10, y=350)

        j = tk.Label(ventana, text="Jairo Andrés Urbina Pineda", bg="light slate blue", fg="black")
        j.config(font=("Calibri Light", 10, "italic"))
        j.place(x=230, y=310)

        d = tk.Label(ventana, text="Daniela Sofía López González", bg="light slate blue", fg="black")
        d.config(font=("Calibri Light", 10, "italic"))
        d.place(x=230, y=330)

        p = tk.Label(ventana, text="Paula Ximena Deaza Gómez", bg="light slate blue", fg="black")
        p.config(font=("Calibri Light", 10, "italic"))
        p.place(x=230, y=350)


    #----------------------------------------MÉTODOS-------------------------------------------
        def cambio1():
            '''
            Destruye los componenetes y pasa a la ventana 1
            '''
            titulo.destroy()
            u.destroy()
            j.destroy()
            d.destroy()
            p.destroy()
            f.destroy()
            pr.destroy()
            com.destroy()

            botonUno.destroy()
            botonDos.destroy()
            botonTres.destroy()
            aplicacion = ventanaN.Ventana_Nutri(ventana)

            ventana.mainloop()

        def cambio2():
            '''
            Destruye los componenetes y pasa a la ventana 2
            '''
            titulo.destroy()
            u.destroy()
            j.destroy()
            d.destroy()
            p.destroy()
            f.destroy()
            pr.destroy()
            com.destroy()

            botonUno.destroy()
            botonDos.destroy()
            botonTres.destroy()

            aplicacion = ventanaC.Ventana_C(ventana)
            ventana.mainloop()

        def cambio3():
            '''
            Destruye los componenetes y pasa a la ventana 3
            '''
            titulo.destroy()
            u.destroy()
            j.destroy()
            d.destroy()
            p.destroy()
            u.destroy()
            f.destroy()
            pr.destroy()
            com.destroy()
            botonUno.destroy()
            botonDos.destroy()
            botonTres.destroy()
            aplicacion = ventanaL.Ventana_L(ventana)
            ventana.mainloop()


    #-----------------------------------------------BOTONES---------------------------------------
        botonUno = tk.Button(ventana, text="PROGRAMACIÓN DINÁMICA", width=23, fg='black', command =cambio1)
        botonUno.place(x=110, y=80)
        botonUno.config(font=("Calibri Light", 11, "italic"))

        botonDos = tk.Button(ventana, text="BACKTRACKING", width=23, fg='black',command = cambio2)
        botonDos.place(x=110 , y= 130)
        botonDos.config(font=("Calibri Light", 11, "italic"))

        botonTres = tk.Button(ventana, text="RAMA Y PODA", width=23, fg='black', command=cambio3)
        botonTres.place(x=110, y=180)
        botonTres.config(font=("Calibri Light", 11, "italic"))
