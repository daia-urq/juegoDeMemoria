from tkinter import *
import random
from PIL import Image, ImageTk

ROJO = "#D90707"
CELESTE = "#668CD9"
NARANJA = "#F2600C"
AMARILLO = "#F2B035"
VIOLETA = "#7229D9"

class JuegoMemoria:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Juego de Memoria")
        self.raiz.resizable(0, 0)
        self.raiz.geometry("500x500")
        self.raiz.config(bg=CELESTE)
        self.componentes()

    def componentes(self):       
        self.imagenFondo = Image.open("fondo-01-01.png")
        self.imagenFondo = self.imagenFondo.resize((500, 500))
        self.imagenFondo = ImageTk.PhotoImage(self.imagenFondo)

        self.canvas = Canvas(self.raiz, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.imagenFondo)

        self.tituloJuego = Label(self.raiz, text="¡Juego de Memoria!", font=("Arial", 24), fg=AMARILLO)
        self.tituloJuego.place(x=105, y=70)

        self.opcionLetraNumero = IntVar(value=2)
        Radiobutton(self.raiz, text="LETRAS", variable=self.opcionLetraNumero, value=1, bg=ROJO, fg="#ffffff",
                    selectcolor=CELESTE, width=10, relief="ridge").place(x=150, y=190)
        Radiobutton(self.raiz, text="NUMEROS", variable=self.opcionLetraNumero, value=2, bg=CELESTE, fg="#ffffff",
                    selectcolor=CELESTE, width=10, relief="ridge").place(x=270, y=190)

        self.dificultadOpcion = IntVar(value=8)
        Radiobutton(self.raiz, text="FACIL", variable=self.dificultadOpcion, bg=NARANJA, fg="#ffffff",
                    selectcolor=CELESTE, width=10, relief="ridge", value=8).place(x=90, y=250)
        Radiobutton(self.raiz, text="MEDIO", variable=self.dificultadOpcion, bg=AMARILLO, fg="#ffffff",
                    selectcolor=CELESTE, width=10, relief="ridge", value=12).place(x=210, y=250)
        Radiobutton(self.raiz, text="DIFICIL", variable=self.dificultadOpcion, bg=VIOLETA, fg="#ffffff",
                    selectcolor=CELESTE, width=10, relief="ridge", value=16).place(x=330, y=250)

        self.botonJugar = Button(self.raiz, text="Jugar", activeforeground="red", width=10, height=2, cursor="hand2",
                                 bg=CELESTE, fg="#ffffff", font=("Arial", 16), relief="ridge", bd=5,
                                 command=self.comenzarJuego)
        self.botonJugar.place(x=190, y=310)

        self.buttonSalir = Button(self.raiz, text="Salir", activeforeground="red", width=6, height=1, cursor="hand2",
                                  bg=AMARILLO, fg="#ffffff", font=("Arial", 10), relief="ridge", bd=5,
                                  command=self.cerrarJuego)
        self.buttonSalir.place(x=225, y=400)

    def comenzarJuego(self):
        tipo = self.opcionLetraNumero.get()
        dificultad = self.dificultadOpcion.get()
        self.ventanaLetras(tipo, dificultad)

    def mostarValorBotones(self, valor, boton):
        boton.config(text=str(valor))

    def generarBotones(self, ventana, elementos):
        random.shuffle(elementos)
        elementos_repetidos = elementos * 2
        random.shuffle(elementos_repetidos)
        colores = [ROJO, CELESTE, NARANJA, AMARILLO, VIOLETA]

        longitud_array = len(elementos)

        if longitud_array == 8:
            filas = 4
            columnas = 4
        elif longitud_array == 12:
            filas = 4
            columnas = 6
        else:
            filas = 4
            columnas = 8

        for i in range(filas):
            for j in range(columnas):
                color = colores[(i * 4 + j) % len(colores)]
                elemento = elementos_repetidos.pop()
                texto = ""
                boton = Button(ventana, text=texto, bg=color, width=12, height=5, font=("helvetica", 12), fg="white")
                boton.grid(row=i, column=j)
                boton.config(command=lambda valor=elemento, boton=boton: self.mostarValorBotones(valor, boton))

    def ventanaLetras(self, tipo, dificultad):
        if tipo == 1:
            elemento = [chr(ord('A') + i) for i in range(dificultad)]
        if tipo == 2:
            elemento = list(range(1, dificultad + 1))

        ventanaLetras = Toplevel(self.raiz)
        ventanaLetras.resizable(0, 0)
        ventanaLetras.config(bg="yellow")
        ventanaLetras.config(width="600", height="600")
        ventanaLetras.config(bd=5)
        ventanaLetras.config(relief="ridge")
        ventanaLetras.config(cursor="hand2")
        ventana2 = Frame(ventanaLetras)
        ventana2.pack(anchor="w")
        self.generarBotones(ventana2, elemento)
        self.raiz.iconify()

    def cerrarJuego(self):
        self.raiz.destroy()

if __name__ == "__main__":
    raiz = Tk()
    game = JuegoMemoria(raiz)
    raiz.mainloop()
