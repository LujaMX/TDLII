import re
import keyword
import GUI
from tkinter import END,messagebox, ttk
from tkinter import *
import tkinter as tk
import numpy as np
import queue

word = queue.Queue()
pila = []

slrTabla = np.loadtxt("GR2slrTable.txt", skiprows=0)
slrReglas = np.loadtxt("GR2slrRulesId.txt", skiprows=0)

root = tk.Tk()
root.title("Analizador léxico")
root.config(width=700, height=500)

tk.Label(root, text="Código: ").place(x=140,y=30)
txtCodigo = Text(root,width=30, height=10)
txtCodigo.place(x=50,y=50)

tabla = ttk.Treeview(root,columns=("Token","Código"))
tabla.place(x=60,y=270)

operators = {'=' : 'opAsignacion','+' : 'opSuma','-' : 'opSuma','/' : 'opMultiplicacion','*' : 'opMultiplicacion','<' : 'opRelacional','>' : 'opRelacional'
                ,'||' : 'opLogico' ,'&&' : 'opLogico', '$' : 'pesos'}
operators_key = operators.keys()

operatorsRel = {'==' : 'opRelacional','<=' : 'opRelacional','>=' : 'opRelacional','!=' : 'opRelacional'}
operatorsRel_key = operatorsRel.keys()

data_type = {'int' : 'tipo de dato', 'float': 'tipo de dato' , 'char' : 'tipo de dato', 'void' : 'tipo de dato' }
data_type_key = data_type.keys()

punctuation_symbol = { ';' : 'punto y coma', ',' : 'coma', '(' : 'parentesis izquierdo' , ')' : 'parentesis derecho',
                        '{' : 'llave izquierda', '}' : 'llave derecha'}
punctuation_symbol_key = punctuation_symbol.keys()

reservedWords = { 'if' : 'condicion if', 'while' : 'ciclo while', 'else' : 'condicion else', 'return' : 'retorno'}
reservedWords_key = reservedWords.keys()

codigos = {'tipo de dato' : '0', 'punto y coma' : '2', 'coma' : '3', 'parentesis izquierdo' : '4', 'parentesis derecho' : '5',
           'llave izquierda' : '6', 'llave derecha' : '7','opAsignacion' : '8', 'condicion if' : '9',
           'ciclo while' : '10','retorno' : '11', 'condicion else' : '12', 'opSuma' : '14', 'opLogico' : '15', 'opMultiplicacion' : '16',
           'opRelacional' : '17', 'pesos' : '18'}
codigos_key= codigos.keys()

def validateID(token):
    # Comprobar si el nombre de la variable comienza con una letra o un guión bajo (_)
    if not token[0].isalpha() and token[0] != '_':
        return False
    
    # Comprobar si el nombre de la variable solo contiene letras, números y guiones bajos (_)
    if not all(caracter.isalnum() or caracter == '_' for caracter in token):
        return False
    
    # Comprobar si el nombre de la variable es una palabra reservada de Python
    if keyword.iskeyword(token):
        return False
    
    # Si ha pasado todas las comprobaciones, el nombre de la variable es válido
    return True

def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def SintacAnalisis():
    print("hola")

    dataFlag = False
    a=txtCodigo.get(1.0,"end-1c")
    a = a + " $"

    count=0
    program = a.split("\n")
    for line in program:
        count = count + 1
        print("line #" , count, "\n" , line)

        status=0
        tokens=line.split(' ')
        print("Tokens are " , tokens)
        print("Line#", count, "properties \n")

        for token in tokens:
            # Comprobar si el nombre de la variable comienza con una letra o un guión bajo (_)
            if not token[0].isalpha() and token[0] != '_':

                if token[0]=="<" or token[0]==">" or token[0]=="=" or token[0]=="!":
                    if token in operatorsRel_key:
                        print("lexema: ",token, "is", operatorsRel[token])
                        tabla.insert("",END,text=token,values=(operatorsRel[token],codigos[operatorsRel[token]]))
                        word.put(codigos[operatorsRel[token]])
                        status = 1
                if token in operators_key:
                    print("lexema: ",token, "is", operators[token])
                    tabla.insert("",END,text=token,values=(operators[token],codigos[operators[token]]))
                    word.put(codigos[operators[token]])
                    status=1
                if token in punctuation_symbol_key:
                    print ("lexema: ",token, "is", punctuation_symbol[token])   
                    tabla.insert("",END,text=token,values=(punctuation_symbol[token],codigos[punctuation_symbol[token]]))
                    word.put(codigos[punctuation_symbol[token]])
                    status=1
                if token.isdigit() or isNumeric(token):
                    print("lexema: ",token, "is", "constante")
                    tabla.insert("",END,text=token,values=("constante","13"))
                    word.put('13')              

            # Comprobar si el nombre de la variable solo contiene letras, números y guiones bajos (_)
            elif not all(caracter.isalnum() or caracter == '_' for caracter in token):
                print ("lexema: ", token, "error")
                tabla.insert("",END,text=token,values=("Error","Error"))
                word.put('40')
            
            # Comprobar si el nombre de la variable es una palabra reservada de Python
            elif keyword.iskeyword(token):
                if token in reservedWords_key:
                    print("lexema: ",token, "is", reservedWords[token])
                    tabla.insert("",END,text=token,values=(reservedWords[token],codigos[reservedWords[token]]))
                    word.put(codigos[reservedWords[token]])
            
            elif token in data_type_key:
                print("lexema: ",token, "is", data_type[token]) 
                tabla.insert("",END,text=token,values=(data_type[token],codigos[data_type[token]]))
                word.put(codigos[data_type[token]])
            # Si ha pasado todas las comprobaciones, el nombre de la variable es válido
            else:
                print ("lexema: ", token, "ID")
                tabla.insert("",END,text=token,values=("id","1"))
                word.put('1')
        dataFlag=False
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")
        Analisis2()


def Analisis2():
    print(word)
    estado = int(word.get())
    print(estado)

    bandera = 0
    pila.append(slrTabla[0][0])
    while bandera < 10:
        accion = int ( slrTabla[int(pila[-1])][int(word.get())] )
        if(accion > 0):
           pila.append(int(word.get()))
           pila.append(accion)
        if(accion < 0):
            iteraciones = int (slrReglas[1][abs(accion)]) * 2
            for i in range(0, iteraciones):
                pila.pop()
            pila.append(int ( slrTabla[int(pila[-1])][int (slrReglas[0][abs(accion)])] ))

        if(word.get() == 18):
            print("Palabra aceptada")
        bandera + 1

btnMostrar=tk.Button(root,text= "Mostrar",command=SintacAnalisis)
btnMostrar.place(x=320,y=120)
root.mainloop()