from tkinter import *
import random
from PIL import Image, ImageTk
import string

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
        self.raiz.iconbitmap("icono.ico")
        self.coincidenciasEncontradas = 0
        self.componentes()

    def componentes(self):       
        self.imagenFondo = Image.open("fondo-01-01.png")
        self.imagenFondo = self.imagenFondo.resize((500, 500))
        self.imagenFondo = ImageTk.PhotoImage(self.imagenFondo)

        self.canvas = Canvas(self.raiz, width=500, height=500, bg="#8FB7F2")
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.imagenFondo)

        self.tituloJuego = Label(self.raiz, text="¡Juego de Memoria!", font=("Arial", 24), fg="white" ,bg="#8FB7F2")
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

    def limpiarJuego(self):
        self.coincidenciasEncontradas = 0
        self.botones = []
        self.jugada = []
        self.numeroBotonesVolteados = 0

    def comenzarJuego(self):
        self.limpiarJuego()
        tipo = self.opcionLetraNumero.get()
        dificultad = self.dificultadOpcion.get()
        self.ventanaLetras(tipo, dificultad)

    def generarBotones(self, ventana, elementos):
        random.shuffle(elementos)
        elementosRepetidos = elementos * 2
        random.shuffle(elementosRepetidos)
        colores = [ROJO, CELESTE, NARANJA, AMARILLO, VIOLETA]

        longitudArray = len(elementos)

        if longitudArray == 8:
            filas = 4
            columnas = 4
        elif longitudArray == 12:
            filas = 4
            columnas = 6
        else:
            filas = 4
            columnas = 8

        self.botones = [] 
        self.jugada = []  
        self.numeroBotonesVolteados = 0

        for i in range(filas):
            for j in range(columnas):
                color = colores[(i * 4 + j) % len(colores)]
                elemento = elementosRepetidos.pop()
                texto = ""
                botonInfo = {"valor": elemento, "visible": False, "boton": None}  
                
                boton = Button(ventana, text=texto, bg=color, width=7, height=3 , font=("helvetica", 20), fg="white")
                boton.grid(row=i, column=j)                
               
                boton.botonInfo = botonInfo               
             
                boton.config(command=lambda btn=boton: self.voltearBoton(btn))

                botonInfo["boton"] = boton
                self.botones.append(botonInfo)

    def voltearBoton(self, boton):
            botonInfo = boton.botonInfo

            if not botonInfo["visible"] and self.numeroBotonesVolteados < 2:
                boton.config(text=botonInfo["valor"])
                botonInfo["visible"] = True
                self.jugada.append(botonInfo)
                self.numeroBotonesVolteados += 1

                if self.numeroBotonesVolteados == 2:
                    self.raiz.after(1000, self.validarCoincidencia)

    def validarCoincidencia(self):
        if len(self.jugada) == 2:
            if self.jugada[0]["valor"] == self.jugada[1]["valor"]:
                self.numeroBotonesVolteados = 0
                self.jugada = []
                self.coincidenciasEncontradas += 1              
                if self.coincidenciasEncontradas == len(self.botones) // 2:
                    self.mostrarVictoria()
            else:
                self.raiz.after(200, self.ocultarBotones)

    def ocultarBotones(self):
        for b in self.jugada:
            b["boton"].config(text="")
            b["boton"].botonInfo["visible"] = False
        self.numeroBotonesVolteados = 0
        self.jugada = []
 
    def ventanaLetras(self, tipo, dificultad):
        if tipo == 1:         
            elemento = random.sample(string.ascii_uppercase, dificultad)
        if tipo == 2:
            elemento = list(range(1, dificultad + 1))

        ventanaLetras = Toplevel(self.raiz)
        ventanaLetras.resizable(0, 0)
        ventanaLetras.config(bg="yellow")
        ventanaLetras.config(width="600", height="600")
        ventanaLetras.config(bd=5)
        ventanaLetras.config(relief="ridge")
        ventanaLetras.config(cursor="hand2")
        ventanaLetras.iconbitmap("icono.ico")
        ventana2 = Frame(ventanaLetras)
        botonVolver = Button(ventanaLetras, text="Volver", bg=CELESTE, fg="white" , command=lambda: self.volver(ventanaLetras))
        botonVolver.pack(side="bottom", fill="x")
        ventana2.pack(anchor="w")
        self.generarBotones(ventana2, elemento)
        self.raiz.iconify()
    
    def mostrarVictoria(self):
        ventanaVictoria = Toplevel(self.raiz)
        ventanaVictoria.title("¡Ganaste!")
        ventanaVictoria.iconbitmap("icono.ico")
        ventanaVictoria.geometry("300x100")
        ventanaVictoria.configure(bg=CELESTE, relief="ridge", bd=5)
        ventanaVictoria.resizable(False, False)
        etiquetaGanaste = Label(ventanaVictoria, text="¡Ganaste!", font=("Arial", 20), bg=CELESTE, fg="white")
        etiquetaGanaste.pack(pady=20, anchor="center")
        ventanaVictoria.after(3000, ventanaVictoria.destroy)


    def volver(self, ventanaLetras ):
        ventanaLetras.destroy()
        raiz.iconify()  
        raiz.update()  
        raiz.deiconify() 

    def cerrarJuego(self):
        self.raiz.destroy()

if __name__ == "__main__":
    raiz = Tk()
    game = JuegoMemoria(raiz)
    raiz.mainloop()
