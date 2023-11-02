import tkinter as tk
from tkinter import PhotoImage

Ventana = tk.Tk()
Ventana.title("Numeros primos")
Ventana.attributes("-fullscreen", True)

def Funcion(event=None):  # Agregamos event como argumento con un valor predeterminado None
    ENumero = (EntryText.get())

    try:
        Numero = int(ENumero)
        #MandarTxt = ""

        if Numero == int(Numero) and Numero > 100:
            MandarTxt = "El límite fijado es de 100\nIntroduce un número menor a:\n" + str(Numero)
        else:
            if Numero > 1:
                cont = 0
                for i in range(2, Numero):
                    resto = Numero % i
                    print("{}%{}={}".format(Numero, i, resto))
                    if resto == 0:
                        cont += 1
                if cont == 0:
                    MandarTxt = "El " + str(Numero) + " es un número primo"
                else:
                    MandarTxt = "El " + str(Numero) + " no es un número primo"
            else:
                MandarTxt = "El " + str(Numero) + " no es un número primo"

        EsONoPrimo.config(text=MandarTxt)

    except ValueError:
        Numero = str(ENumero)
        MandarTxt = "El dato ingresado: \n " + str(Numero) + " \n no es tipo numerico."
        EsONoPrimo.config(text=MandarTxt)

imagen = PhotoImage(file="Fondo.png")
fondolabel = tk.Label(Ventana, image=imagen)
fondolabel.place(x=0, y=0, relwidth=1, relheight=1)

TxtPrincipal = tk.Label(Ventana, text="Ingresa un número", font="Arial 60")
TxtPrincipal.grid(row=0, column=0, columnspan=2, pady=120)

EntryText = tk.Entry(Ventana, width=20, font="Arial 40", justify="center")
EntryText.grid(row=1, column=0, padx=100, ipadx=1, ipady=100)

# Vincular el evento "Return" (Enter) en el Entry a la función Funcion
EntryText.bind("<Return>", Funcion)

Boton = tk.Button(Ventana, text="Comprobar", command=Funcion, font="Arial 20")
Boton.grid(row=2, column=1, pady=50, padx=50)

EsONoPrimo = tk.Label(Ventana, font="Arial 40")
EsONoPrimo.grid(row=1, column=1, padx=1, pady=0)

Ventana.mainloop()
