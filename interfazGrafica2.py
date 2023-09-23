from tkinter import *
import random
from PIL import Image, ImageTk

raiz = Tk()
raiz.title("Juego de Memoria")
raiz.resizable(0,0) #permitir que la ventana sea modificable en el tamaño
raiz.geometry("500x500") #tamaño de la ventana
raiz.config(bg="#668CD9")

imagen_de_fondo = Image.open("fondo-01-01.png")  
imagen_de_fondo = imagen_de_fondo.resize((500, 500))
imagen_de_fondo = ImageTk.PhotoImage(imagen_de_fondo)

canvas = Canvas(raiz, width=500, height=500)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=imagen_de_fondo)# Coloca la imagen en el Canvas

miLabel=Label(raiz, text="¡Juego de Memoria!", font=("Arial", 24),  fg="#F2B035")
miLabel.place(x=105, y=70) #posiciona el label dentro del frame

tipoOpcion = IntVar(value=2)
Radiobutton(raiz, text="LETRAS", variable=tipoOpcion, value=1, bg="#D90707", fg="#ffffff", width=10 , relief="ridge").place(x=150, y=190)
Radiobutton(raiz, text="NUMEROS", variable=tipoOpcion, value=2, bg="#668CD9", fg="#ffffff", width=10 , relief="ridge").place(x=270, y=190)

dificultadOpcion = IntVar(value=8)
Radiobutton(raiz, text="FACIL", variable=dificultadOpcion, bg="#F2600C", fg="#ffffff", width=10 , relief="ridge", value=8).place(x=90, y=250)
Radiobutton(raiz, text="MEDIO",  variable=dificultadOpcion, bg="#F2B035", fg="#ffffff", width=10 ,  relief="ridge", value=12).place(x=210, y=250)
Radiobutton(raiz, text="DIFICIL",  variable=dificultadOpcion, bg="#7229D9", fg="#ffffff", width=10 , relief="ridge", value=16).place(x=330, y=250)

def botones(ventana, elementos):
    random.shuffle(elementos)
    elementos_repetidos = elementos * 2
    random.shuffle(elementos_repetidos)
    colores = ["#D90707", "#668CD9", "#F2600C", "#F2B035", "#7229D9"]

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
            texto = f"{elemento}"
            boton = Button(ventana, text=texto, bg=color, width=12, height=5, font=("helvetica", 12), fg="white")
            boton.grid(row=i, column=j)


def ventanaLetras(tipo, dificultad):
    if tipo == 1:
        elemento= [chr(ord('A') + i) for i in range(dificultad)]
    if tipo == 2:
        elemento =list(range(1, dificultad+1))

    ventanaLetras = Toplevel(raiz)
    ventanaLetras.resizable(0,0)
    ventanaLetras.config(bg="yellow")  #color del frame
    ventanaLetras.config(width="600", height="600") #tañamo del frame
    ventanaLetras.config(bd=5) #tamaño del borde
    ventanaLetras.config(relief="ridge") #tipo de borde
    ventanaLetras.config(cursor="hand2") #cambia el cursor 
    ventana2 = Frame(ventanaLetras)
    ventana2.pack(anchor="w")    
    botones(ventana2, elemento)
    raiz.iconify()


botonJugar = Button(raiz, text="Jugar", activeforeground="red", width=10, height=2, cursor="hand2", bg="#668CD9", fg="#ffffff", font=("Arial", 16), relief="ridge", bd=5, command=lambda: ventanaLetras(tipoOpcion.get(), dificultadOpcion.get()))
botonJugar.place(x=190,y=310)

def close_window():
    raiz.destroy()

buttonSalir = Button(raiz,text = "Salir", activeforeground="red",width=6, height=1,  cursor="hand2", bg="#F2B035", fg="#ffffff", font=("Arial", 10), relief="ridge", bd=5,command = close_window)
buttonSalir.place(x=225,y=400)

raiz.mainloop()

      
