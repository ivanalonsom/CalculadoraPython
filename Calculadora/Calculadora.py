from tkinter import *

raiz = Tk()
raiz.geometry("400x500")
miFrame = Frame(raiz)
miFrame.pack(expand=True, fill="both")

# ------------ VARIABLES GLOBALES ------------
numeroPantalla = StringVar()
operador = ""  # podia igualar a "" y ya
op_anterior = ""
resultado = 0
nuevos_numeros = False
# Creo esto para evitar que al pulsar dos veces seguidas un operador este me opere el numero consigo mismo.

# ------------ PANTALLA ------------
pantalla = Entry(miFrame, textvariable=numeroPantalla, font=("Arial", 24))  # Aumentar el tamaño de la fuente
pantalla.grid(row=0, column=0, padx=10, pady=20, columnspan=4, sticky="nsew")
# Sin columnspan sale mal porque toma el elemento "pantalla" como columna 1 y este hace a esa columna mucho
# más ancha que la 2, 3 y 4. Tenemos que decirle que "pantalla" ocupe las 4 columnas
pantalla.config(bg="black", fg="#03f943", justify="right")

# ------------ PULSACIONES TECLADO ------------

def num_pulsado(num):
    global operador
    global op_anterior
    global nuevos_numeros

    if num == '0' and numeroPantalla.get() == "":
        return
    elif num == '.' and numeroPantalla.get() == "":
        numeroPantalla.set("0.")
    else:
        if '.' in numeroPantalla.get() and num == '.':
            return
        if operador != "":
            numeroPantalla.set(num)
            op_anterior = operador
            operador = ""
        else:
            numeroPantalla.set(numeroPantalla.get() + num)
    nuevos_numeros = True

def suma(num):
    global operador
    global resultado
    global nuevos_numeros

    operador = "suma"
    if op_anterior == operador and not nuevos_numeros:
        return
    else:
        resultado += float(num)
        numeroPantalla.set(str(resultado).rstrip('0').rstrip('.') if '.' in str(resultado) else str(resultado))
        # Cambio numeroPantalla.set(resultado) por eso para que si tengo un 6, al darle a sumar no me lo cambie a 6.0
        nuevos_numeros = False


def resta(num):
    global operador
    global resultado
    global nuevos_numeros

    operador = "resta"
    if op_anterior == operador and not nuevos_numeros:
        return
    elif resultado==0:
        resultado = float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False
    else:
        resultado -= float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False

def mult(num):
    global operador
    global resultado
    global nuevos_numeros

    operador = "multiplica"
    if op_anterior == operador and not nuevos_numeros:
        return
    elif resultado!=0:
        resultado *= float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False
    else:
        resultado = float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False

def div(num):
    global operador
    global resultado
    global nuevos_numeros

    operador = "divide"
    if op_anterior == operador and not nuevos_numeros:
        return
    elif resultado == 0:
        resultado = float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False
    else:
        resultado /= float(num)
        numeroPantalla.set(resultado)
        nuevos_numeros = False
def el_resultado():
    global resultado
    global operador
    global op_anterior

    if op_anterior == "suma":
        numeroPantalla.set(resultado + float(numeroPantalla.get() ) )
    elif op_anterior == "resta":
        numeroPantalla.set(resultado - float(numeroPantalla.get() ) )
    elif op_anterior == "multiplica":
        numeroPantalla.set(resultado * float(numeroPantalla.get() ) )
    elif op_anterior == "divide":
        numeroPantalla.set(resultado / float(numeroPantalla.get() ) )

    resultado = 0

btn_font = ("Arial", 18)

# ------------ FILA 1 ------------

boton7 = Button(miFrame, text="7", width=5, height=2, font=btn_font, command=lambda: num_pulsado("7"))
boton7.grid(row=1, column=0, sticky="nsew")

boton8 = Button(miFrame, text="8", width=5, height=2, font=btn_font, command=lambda: num_pulsado("8"))
boton8.grid(row=1, column=1, sticky="nsew")

boton9 = Button(miFrame, text="9", width=5, height=2, font=btn_font, command=lambda: num_pulsado("9"))
boton9.grid(row=1, column=2, sticky="nsew")

botonDiv = Button(miFrame, text="/", width=5, height=2, font=btn_font, command=lambda: div(numeroPantalla.get()))
botonDiv.grid(row=1, column=3, sticky="nsew")

# ------------ FILA 2 ------------
boton4 = Button(miFrame, text="4", width=5, height=2, font=btn_font, command=lambda: num_pulsado("4"))
boton4.grid(row=2, column=0, sticky="nsew")

boton5 = Button(miFrame, text="5", width=5, height=2, font=btn_font, command=lambda: num_pulsado("5"))
boton5.grid(row=2, column=1, sticky="nsew")

boton6 = Button(miFrame, text="6", width=5, height=2, font=btn_font, command=lambda: num_pulsado("6"))
boton6.grid(row=2, column=2, sticky="nsew")

botonMult = Button(miFrame, text="X", width=5, height=2, font=btn_font, command=lambda: mult(numeroPantalla.get()))
botonMult.grid(row=2, column=3, sticky="nsew")

# ------------ FILA 3 ------------
boton1 = Button(miFrame, text="1", width=5, height=2, font=btn_font, command=lambda: num_pulsado("1"))
boton1.grid(row=3, column=0, sticky="nsew")

boton2 = Button(miFrame, text="2", width=5, height=2, font=btn_font, command=lambda: num_pulsado("2"))
boton2.grid(row=3, column=1, sticky="nsew")

boton3 = Button(miFrame, text="3", width=5, height=2, font=btn_font, command=lambda: num_pulsado("3"))
boton3.grid(row=3, column=2, sticky="nsew")

botonRest = Button(miFrame, text="-", width=5, height=2, font=btn_font, command=lambda: resta(numeroPantalla.get()))
botonRest.grid(row=3, column=3, sticky="nsew")

# ------------ FILA 4 ------------
boton0 = Button(miFrame, text="0", width=5, height=2, font=btn_font, command=lambda: num_pulsado("0"))
boton0.grid(row=4, column=0, sticky="nsew")

boton_coma = Button(miFrame, text=".", width=5, height=2, font=btn_font, command=lambda: num_pulsado("."))
boton_coma.grid(row=4, column=1, sticky="nsew")

boton_igual = Button(miFrame, text="=", width=5, height=2, font=btn_font, command=lambda: el_resultado())
boton_igual.grid(row=4, column=2, sticky="nsew")

botonSuma = Button(miFrame, text="+", width=5, height=2, font=btn_font, command=lambda: suma(numeroPantalla.get()))
botonSuma.grid(row=4, column=3, sticky="nsew")

# Configurar columnas y filas para que se expandan
for i in range(4):
    miFrame.grid_columnconfigure(i, weight=1)
for i in range(5):
    miFrame.grid_rowconfigure(i, weight=1)

raiz.mainloop()
