from tkinter import Tk, Button, Entry

num_1 = ""
num_2 = ""
operador = ""

def actualizar_pantalla(evento):
    global num_1, num_2, operador
    boton = evento.widget
    valor = boton['text']
    if (valor in "0123456789"):
        if (operador == ""):
            num_1 += valor
        else:
            num_2 += valor
    elif valor in "+-*/":
        operador = valor
    elif valor == "=":
        if not (num_1=="" and num_2=="" and operador==""):
            resultado = ""
            numero1 = float(num_1)
            numero2 = float(num_2)
            if operador=="+":
                   resultado += str(numero1+numero2)
            elif operador=="-":
                   resultado += str(numero1-numero2)
            elif operador=="*":
                   resultado += str(numero1*numero2)
            elif operador=="/":
                if numero2 == 0:
                    resultado = "No se puede dividir por 0"
                else:
                    resultado += str(numero1/numero2)
            num_1=""
            num_2=""
            operador=""


    pantalla.insert("end", num_1+operador+num_2)


# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x253")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)


boton_1.bind("<Button-1>", actualizar_pantalla)
boton_2.bind("<Button-1>", actualizar_pantalla)
boton_3.bind("<Button-1>", actualizar_pantalla)
boton_4.bind("<Button-1>", actualizar_pantalla)
boton_5.bind("<Button-1>", actualizar_pantalla)
boton_6.bind("<Button-1>", actualizar_pantalla)
boton_7.bind("<Button-1>", actualizar_pantalla)
boton_8.bind("<Button-1>", actualizar_pantalla)
boton_9.bind("<Button-1>", actualizar_pantalla)
boton_punto.bind("<Button-1>", actualizar_pantalla)
boton_mas.bind("<Button-1>", actualizar_pantalla)
boton_menos.bind("<Button-1>", actualizar_pantalla)
boton_multiplicacion.bind("<Button-1>", actualizar_pantalla)
boton_division.bind("<Button-1>", actualizar_pantalla)
boton_igual.bind("<Button-1>", actualizar_pantalla)

root.mainloop()