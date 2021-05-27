import vista.VenatanPrincipal as ventanaPrincipal
import tkinter as tk
class Principal():
  '''
  Clase que inicia la aplicación
  '''
  def __init__(self):
    pass
  def main(self):
    '''
    Inicializa la vista y la deja corriendo
    :return:
    '''
    root = tk.Tk()
    aplicacion = ventanaPrincipal.Principal(root)
    root.mainloop()


if __name__ == '__main__':
  '''
  Inicia la aplicación
  '''
  controlador = Principal()
  controlador.main()