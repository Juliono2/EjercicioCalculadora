from tkinter import *
from tkinter import ttk
from Operaciones import Operaciones

class Calculadora:                                  # Clase para el manejo de funcionalidades de una calculadora
    def __init__(self):                             #Constructor
        self.entrada1 = StringVar()
        self.entrada2 = StringVar()
        self.resultado = 0
        self.operador = ""
        self.operaciones = Operaciones()            #Relacion de asociacion con rol "operaciones" de tipo Operaciones

    def ingresarValor(self, tecla):                 #Metodo para ingresar valores en los labels 
        if tecla >= "0" and tecla <= "9":                               #Cuando son numeros
            self.entrada2.set(self.entrada2.get() + str(tecla))
        elif tecla in ["+", "-", "*", "/", "^"]:                        #Cuando se ingresa un operador
            self.operador = tecla
            self.entrada1.set(self.entrada2.get() + tecla)
            self.entrada2.set("")

    def calcularResultado(self):                        #Metodo calcular resultados usa las operaciones y los
        valor1 = float(self.entrada1.get()[:-1])        #Valores obtenidos en los labels
        valor2 = float(self.entrada2.get())
        if self.operador == "+":
            self.resultado = self.operaciones.sumar(valor1, valor2)
        elif self.operador == "-":
            self.resultado = self.operaciones.restar(valor1, valor2)
        elif self.operador == "*":
            self.resultado = self.operaciones.multiplicar(valor1, valor2)
        elif self.operador == "/":
            self.resultado = self.operaciones.dividir(valor1, valor2)
        elif self.operador == "^":
            self.resultado = self.operaciones.potenciar(valor1, valor2)
        self.entrada2.set(str(self.resultado))
        self.entrada1.set("")
        self.operador = ""

    def borrar(self):                               #Metodo para borrar un caracter del texto
        entrada2_texto = self.entrada2.get()
        if len(entrada2_texto) > 0:
            nueva_entrada2 = entrada2_texto[:-1]
            self.entrada2.set(nueva_entrada2)
        elif len(self.entrada1.get()) > 0:          #Se considera el caso en el que el label 1 esta vacio
            nueva_entrada1 = self.entrada1.get()[:-1]
            self.entrada2.set(nueva_entrada1)
            self.entrada1.set("")

    def borrar_todo(self):                          #Metodo para borrar todito todo
        self.entrada1.set("")
        self.entrada2.set("")
        self.operador = ""
        self.resultado = 0

def main():                                         #Desplegar la interfaz grafica
    root= Tk()
    root.title("Calculadora")
    root.geometry("+500+80")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0)

    #Ejemplificamos la calculadora para en los comandos hacer uso de sus metodos
    calculadora = Calculadora()

    #Labels
    label_entrada1 = ttk.Label(mainframe, textvariable=calculadora.entrada1, anchor="e")
    label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,E))

    label_entrada2 = ttk.Label(mainframe, textvariable=calculadora.entrada2, anchor="e")
    label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,E))

    #Botones
    button0 = ttk.Button(mainframe, text="0", command=lambda: calculadora.ingresarValor("0"))
    button1 = ttk.Button(mainframe, text="1", command=lambda: calculadora.ingresarValor("1"))
    button2 = ttk.Button(mainframe, text="2", command=lambda: calculadora.ingresarValor("2"))
    button3 = ttk.Button(mainframe, text="3", command=lambda: calculadora.ingresarValor("3"))
    button4 = ttk.Button(mainframe, text="4", command=lambda: calculadora.ingresarValor("4"))
    button5 = ttk.Button(mainframe, text="5", command=lambda: calculadora.ingresarValor("5"))
    button6 = ttk.Button(mainframe, text="6", command=lambda: calculadora.ingresarValor("6"))
    button7 = ttk.Button(mainframe, text="7", command=lambda: calculadora.ingresarValor("7"))
    button8 = ttk.Button(mainframe, text="8", command=lambda: calculadora.ingresarValor("8"))
    button9 = ttk.Button(mainframe, text="9", command=lambda: calculadora.ingresarValor("9"))

    button_borrar = ttk.Button(mainframe, text="←", command=lambda: calculadora.borrar()) 
    button_borrar_todo = ttk.Button(mainframe, text="C", command=lambda: calculadora.borrar_todo())
    button_parentesis1 = ttk.Button(mainframe, text="(", command=lambda: calculadora.ingresarValor("("))
    button_parentesis2 = ttk.Button(mainframe, text=")", command=lambda: calculadora.ingresarValor(")"))
    button_punto = ttk.Button(mainframe, text=".", command=lambda: calculadora.ingresarValor("."))

    button_division = ttk.Button(mainframe, text="/", command=lambda: calculadora.ingresarValor("/"))
    button_multiplicacion = ttk.Button(mainframe, text="*", command=lambda: calculadora.ingresarValor("*"))
    button_suma = ttk.Button(mainframe, text="+", command=lambda: calculadora.ingresarValor("+"))
    button_resta = ttk.Button(mainframe, text="-", command=lambda: calculadora.ingresarValor("-"))

    button_igual = ttk.Button(mainframe, text="=", command=lambda: calculadora.calcularResultado())
    button_potencia = ttk.Button(mainframe, text="^", command=lambda: calculadora.ingresarValor("^"))

    #Deshabilitamos estos botones pues no tienen funcionalidad actualmente
    button_parentesis1.config(state="disabled")
    button_parentesis2.config(state="disabled")
    button_punto.config(state="disabled")

    #Adicionando los botones a pantalla
    button_parentesis1.grid(column=0, row=2)
    button_parentesis2.grid(column=1, row=2)
    button_borrar_todo.grid(column=2, row=2)
    button_borrar.grid(column=3, row=2)

    button7.grid(column=0, row=3)
    button8.grid(column=1, row=3)
    button9.grid(column=2, row=3)
    button_division.grid(column=3, row=3)

    button4.grid(column=0, row=4)
    button5.grid(column=1, row=4)
    button6.grid(column=2, row=4)
    button_multiplicacion.grid(column=3, row=4)

    button1.grid(column=0, row=5)
    button2.grid(column=1, row=5)
    button3.grid(column=2, row=5)
    button_suma.grid(column=3, row=5)

    button0.grid(column=0, row=6, columnspan=2, sticky=(W,E))
    button_punto.grid(column=2, row=6)
    button_resta.grid(column=3, row=6)

    button_potencia.grid(column=3, row=7)
    button_igual.grid(column=0, row=7, columnspan=3, sticky=(W,E))

    root.mainloop()

if __name__ == "__main__":
    main()