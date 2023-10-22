#Libreria usada para la creacion de la ventana
import tkinter as tk
#libreria usada para el fondo en conjunto con tkinter
from tkinter import PhotoImage

#creacion de la ventana
Ventana = tk.Tk()
#nombre de la ventana
Ventana.title("Numeros primos")
#Parte del codigo para el icono de la ventana
#Ventana.iconbitmap("ico.ico")
#Se le pasa el atributo -fullscreen de forma true diciendo que ponga la ventana en toda la pantalla
Ventana.attributes("-fullscreen", True)

#Se crea la funcion para la comprobacion de los numeros primos
def Funcion():

    #se declaran nuestras 2 variables a usar, uno es para mandar la informacion a un label
    #la otra declaramos numero como entero y le decimos que su valor es el que se mete en nuestro cuadro entry
    MandarTxt=str
    Numero=int(EntryText.get())

    #Ponemos el limite con un if "si numero es mayor a 100 entonces..." mandamos el mensaje visto y concatenamos el numero
    if Numero > 100:

        MandarTxt= "El limite fijado es de 100\n introduce un numero menor a:\n"+str(Numero)

    #ponemos que si la condicion anterior no se cumple entonces seria "si numero es menor a 100 entonces..."
    else:

        #hacemos una comprobación de que la variable numero sea mayor a 1 y la condicion anterior y esta ya limitamos
        #que 100>Numero>1
        if Numero > 1:

            #Se crea la variable cont la usaremos como contador de aumento
            cont = 0

            #se crea un ciclo for para i en el rango 2, hasta numero con esto decimos que empice en 2 y termine hasta
            #el numero que tenga la variable Numero
            for i in range(2, Numero):

                #Se crea la variable resto ya que trabajaremos con los reciduos de la operacion Numero%i
                #donde resto es la variable, numero el delimitante y i el ciclo
                resto =Numero%i

                #creamos un print para mostar en consola todas estas operaciones y ver el funcionamiento del codigo
                print("{}%{}={}".format(Numero, i, resto))

                #comprobamos mediante otro if si resto es igual a 0 aumentaremos contador para que el ciclo siga o no
                if resto == 0:
                    cont += 1
            #Mediante otro if preguntamos si el cont es igual a 0 en todos sus datos, mandamos a la variable un string
            #concatenando nuestro numero diciendo que es primo
            if cont == 0:
                MandarTxt = "El " + str(Numero) + " es numero primo"

            #lo mismo que el anterio pero diciendo que si no es igual a 0 y que no es primo
            else:
                MandarTxt = "El " + str(Numero) + " no es numero primo"

        #Este else esta relacionado al primero, en el cual decimos "si numero es menor a 0 entonces..."
        else:
            MandarTxt = "El " + str(Numero) + " no es numero primo"

    #lo usamos para mandarle el texto a un label del nombre y le ponemos de dato la variable MandarTxt
    EsONoPrimo["text"] = MandarTxt

#Usando nuestra segunda libreria, para poner el fondo a la ventana
imagen = PhotoImage(file="Fondo.png")

#Ponemos un label que llevara la imagen y le decimos que se situe en el fondo y que sea del tamaño de la ventana
fondolabel=tk.Label(Ventana, image=imagen)
fondolabel.place(x=0, y=0, relwidth=1, relheight=1)

#Creamo nuestro titulo de la ventana, con tkinter ponemos un label, asociado a la pantalla de nombre ventana
TxtPrincipal=tk.Label(Ventana, text="Ingresa un numero", font="Arial 60")

#para posicionar usamos grid le decimos que este en la columna 0 fila 0
#que ocupe 2 columnas y tenga un marge exterior de en y del 1200
TxtPrincipal.grid(row=0, column=0, columnspan=2, pady=120)

#Cramos nuestra entrada de texto en este caso numeros, asociado a la ventana
#un ancho de 20, con arial 40 y que este centrado el texto que lleve dentro
EntryText = tk.Entry (Ventana, width=20, font="Arial 40", justify="center")

#Usamos grid,columna 0, fila 1, margen x exterior de 100, margen interior x de 1 y y de 100
EntryText.grid(row=1, column=0, padx=100, ipadx=1, ipady=100)

#Creamos el boton asociado a la ventana, este le dira al programa que al ser oprimido
#mande a usar la fucion que hicimos al inicio
Boton=tk.Button(Ventana, text="Comprobar", command=Funcion, font="Arial 20")

#se usa grid, fila 2, columna 1, margen y 50 y x 50
Boton.grid(row=2, column=1, pady=50, padx=50)

#creamos un label este mostrar si es un numero primo o no, aqui es donde cae lo que manda la funcion
EsONoPrimo = tk.Label(Ventana, font="Arial 40")
#fila 1, columna 1, margen x de 1 y y de 0
EsONoPrimo.grid(row=1, column=1, padx=1, pady=0)

#esto nos ayuda en tkinter para que se pueda mostrar la ventana
Ventana.mainloop()
