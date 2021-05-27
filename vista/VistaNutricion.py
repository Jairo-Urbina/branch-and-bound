import tkinter as tk
from tkinter import messagebox

from modelo.Nutricion import Nutricion
import vista.VenatanPrincipal as principal


class Ventana_Nutri:

    def __init__(self, ventana):
        '''
        Inicializa lso componentes de esta ventana
        :param ventana: Ventana a la que se añadirán los componententes
        '''
        # ---------------------------propidade de ventana --------------------------------------------------------------------
        ventana.title("Programación Dinámica")
        ventana.geometry('500x500')
        ventana.configure(background='light slate blue')
        titulo = tk.Label(ventana, text="Problema Nutrición", bg="light slate blue", fg="black")
        titulo.config(font=("Calibri Light", 16, "italic"))
        titulo.pack()
        # ------------------------------------------Variables--------------------------------------------------------------
        llenar = tk.StringVar()
        resultado0 = tk.StringVar()
        resultado = tk.StringVar()
        resultado2 = tk.StringVar()
        ar = []
        nutri = Nutricion()

        # ---------------------------------------------------LABEL MAYOR------------------------------------------------------
        label_ingreso = tk.Label(ventana,
                                 text="Ingrese el valor de calorías del plato, cada vez que oprima un botón " + '\n' + "se agrega un plato con esa cantidad de calorias",
                                 bg="light slate blue", fg="black")
        label_ingreso.config(font=("Calibri Light", 10, "italic"))
        label_ingreso.place(x=0, y=30, width=500, height=40)

        ingreso_ingreso1 = tk.Entry(ventana, textvariable=llenar)
        ingreso_ingreso1.place(x=10, y=80, width=400, height=25)

        label_resul = tk.Label(ventana, text="Lista de platos :", bg="light slate blue", fg="black")
        label_resul.place(x=25, y=200, width=220, height=20)
        label_resul.config(font=("Calibri Light", 12, "italic"))

        lista_menu = tk.Listbox(ventana)
        lista_menu.place(x=25, y=230, width=220, height=200)
        lista_menu.yview_scroll(0, tk.UNITS)

        label_ingreso2 = tk.Label(ventana,
                                  text="Ingrese el valor de calorías totales que puede consumir",
                                  bg="light slate blue", fg="black")
        label_ingreso2.place(x=0, y=120, width=500, height=20)
        label_ingreso2.config(font=("Calibri Light", 12, "italic"))

        resultadoTxt0 = tk.Entry(ventana, textvariable=resultado0)
        resultadoTxt0.place(x=10, y=150, width=360, height=25)

        label_resul2 = tk.Label(ventana, text="Lista de platos escogidos :", bg="light slate blue", fg="black")
        label_resul2.place(x=250, y=200, width=220, height=20)
        label_resul2.config(font=("Calibri Light", 12, "italic"))

        lista_respuesta = tk.Listbox(ventana)
        lista_respuesta.place(x=255, y=230, width=220, height=200)
        lista_respuesta.yview_scroll(0, tk.UNITS)

        # --------------------------METODOS--------------------------------------------------------------------------------
        def arreglo():
            '''
            Agrega un nuevo plato al menú
            :return:
            '''
            numero = (llenar.get())
            if int(numero) <= 0:
                messagebox.showinfo(message="No puedes ingresar valores negativos o cero", title="ERROR")
            elif not numero.isdigit():
                messagebox.showinfo(message="No ingresaste un valor numérico", title="ERROR")
                llenar.set("")
            else:
                numero = int(numero)
                ar.append(numero)
                resultado.set(ar)
                llenar.set("")
                x = "plato" + str(len(ar)) + " : " + str(numero) + " calorías"
                lista_menu.insert(tk.END, x)

        def limpiar():
            '''
            Vacía todos los campos
            '''
            del ar[:]
            resultado0.set("")
            resultado.set("")
            resultado2.set("")
            llenar.set("")
            lista_menu.delete(0, lista_menu.size())
            lista_respuesta.delete(0, lista_respuesta.size())

        def mostrar():
            '''
            Llena la lista de platos seleccioandos por el nutricionista
            '''
            lista_respuesta.delete(0, lista_respuesta.size())
            if not (resultado0.get().isdigit()):
                messagebox.showinfo(message="No ingresaste un valor válido", title="ERROR")
            elif lista_menu.size() == 0:
                messagebox.showinfo(message="El menú de platos está vacío", title="ERROR")
            elif int(resultado0.get()) <= 0:
                messagebox.showinfo(message="No puedes ingresar valores negativos o cero", title="ERROR")
            elif ar:
                arregloooo = nutri.resolver(ar, int(resultado0.get()))
                for i in range(len(arregloooo)):
                    lista_respuesta.insert(i, arregloooo[i])


        def devolver():
            '''
            Destruye los componenetes y pasa a la ventana principal
            '''
            titulo.destroy()
            label_ingreso.destroy()
            label_ingreso2.destroy()
            ingreso_ingreso1.destroy()
            label_resul.destroy()
            label_resul2.destroy()
            resultadoTxt0.destroy()
            lista_respuesta.destroy()
            lista_menu.destroy()
            botonAtras.destroy()
            botonLimpiar.destroy()
            botonMaximo.destroy()
            botonAgregar.destroy()
            aplicacion = principal.Principal(ventana)
            ventana.mainloop()

        # -----------------------------------------BOTONES----------------------------------------------------------------------------------

        botonAgregar = tk.Button(ventana, text="Agregar", fg='black', command=arreglo)
        botonAgregar.place(x=430, y=80)

        botonMaximo = tk.Button(ventana, text="Mostrar resultado ", fg='black', command=mostrar)
        botonMaximo.place(x=380, y=150)

        botonLimpiar = tk.Button(ventana, text="Limpiar Campos(Reset)", fg='black', command=limpiar)
        botonLimpiar.place(x=140, y=450)

        botonAtras = tk.Button(ventana, text="Atrás", fg='black', command=devolver)
        botonAtras.place(x=290, y=450)
