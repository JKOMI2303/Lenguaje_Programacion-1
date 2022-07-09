# Funcion evaluar recibe como argumento un operador y dos operandos y devuelve el resultado de la operacion.
from numpy import exp


def evaluar(operador: str, operando1: str, operando2: str) -> str:
    if operador == "=>":
        if(operando2=="false" and operando1=="true"):
            return "false"
        else:
            return "true"
    elif operador == "&":
        if(operando2=="true" and operando1=="true"):
            return "true"
        else:
            return "false"
    elif operador == "|":
        if(operando2=="false" and operando1=="false"):
            return "false"
        else:
            return "true"
    elif operador == "^":
        if operando1=="false":
            return "true"
        else:
           return "false"


# Funcion mostrar recibe como argumento un operador, dos operandos y devuelve la expresion en notacion infija.
def mostrar(operador: str, operando1: str, operando2: str) -> str:
    if operador in "&|":

        if operando2.find("|")!=-1 or operando2.find("&")!=-1 or operando2.find("=>")!=-1:
            operando2 = f"({operando2})"
        return operando1 + " " + operador + " " + operando2
    elif operador in "=>":
            operandos=operando1 + " " + operador + " " + operando2
            operandos=f"({operandos})"
            return operandos
    elif operador =="^":
        if(len(operando1)==0):
            return operador + " "+ operando2
        elif(len(operando2)==0):
            return operador+" " +operando1
        
# Funcion prefijo recibe como argumento una expresion en orden prefijo y devuelve la evaluacion de la expresion.
def prefijo(accion: str, expresion: list) -> str:
    stack = []

    # recorrer la expresion de derecha a izquierda:
    for i in range(len(expresion)-1, -1, -1):

        # si el caracter es un operador:
        if expresion[i] == "=>" or expresion[i] == "&" or expresion[i] == "|":
            # obtener los operandos:
            operando1 = stack.pop()
            operando2 = stack.pop()

            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":
                # calcular el resultado:
                resultado = evaluar(operador, operando1, operando2)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operando1, operando2)

            # insertar el resultado en la pila:
            stack.append(f"{resultado}")
        
        elif expresion[i] == "^":
            # obtener los operandos:
            operando1 = stack.pop()
            operando2 = ""
            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":
                # calcular el resultado:
                resultado = evaluar(operador, operando1, operando2)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operando1, operando2)

            # insertar el resultado en la pila:
            stack.append(f"{resultado}")


        # si el caracter es un operando:
        else:
            # insertar el operando en la pila:
            stack.append(expresion[i])

    # devolver el resultado:
    return stack[0]

# Funcion postfijo recibe como argumento una expresion en orden postfijo y devuelve la evaluacion de la expresion.
def postfijo(accion: str, expresion: list) -> str:
    stack = []

    # recorrer la expresion de izquierda a derecha:
    for i in range(0, len(expresion)):
        # si el caracter es un operador:
        if expresion[i] == "=>" or expresion[i] == "&" or expresion[i] == "|":
            # obtener los operandos:
            operando2 = stack.pop()
            operando1 = stack.pop()

            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":    
                # calcular el resultado:
                resultado = evaluar(operador, operando1, operando2)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operando1, operando2)
                
            # insertar el resultado en la pila:
            stack.append(f"{resultado}")
        elif expresion[i] == '^':
            # obtener los operandos:
            operando1 = stack.pop()
            operando2 = ""
            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":
                # calcular el resultado:
                resultado = evaluar(operador, operando1, operando2)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operando1, operando2)

            # insertar el resultado en la pila:
            stack.append(f"{resultado}")

        # si el caracter es un operando:
        else:
            # insertar el operando en la pila:
            stack.append(expresion[i])

    # devolver el resultado:
    return stack[0]

if __name__ == "__main__":
    # Pedir al usuario repetidamente una accion: EVAL, MOSTRAR, SALIR
    while True:
        accion = input("Ingrese una accion:\nEVAL <orden> <expr>\nMOSTRAR <orden> <expr>\nSALIR\n\n")
        accion = accion.strip().split()
        if accion[0] == "EVAL":

            if(len(accion)>=3):
                orden=accion[1]
                expr = accion[2:]
        # Si el orden no es PRE ni POST, se muestra un mensaje de ERROR.
                if orden == "PRE" or orden == "POST": 
        # Si el orden es PRE representa expresiones escritas en orden pre–fijo.
                    if orden == "PRE":
                        resultado = prefijo("EVAL", expr)
       
        # Si el orden es POST representa expresiones escritas en orden post–fijo.
                    elif orden == "POST":
                        resultado = postfijo("EVAL", expr)
                    print(f"{resultado}\n")
                else:
                    print("accion no valida")
            else:
                print("faltan argumentos en las acciones")

    # Si la accion es MOSTRAR, Representa una impresión en orden in–fijo o post-fijo de la expresión en <expr>
        elif accion[0] == "MOSTRAR":

            if(len(accion)>=3):
                orden=accion[1]
                expr = accion[2:]
      
                if orden == "PRE" or orden == "POST": 
                    if orden == "PRE":
                        resultado = prefijo("MOSTRAR", expr)
       
                    elif orden == "POST":
                        resultado = postfijo("MOSTRAR", expr)
                    print(f"{resultado}\n")
                else:
                    print("accion no valida")
            else:
                print("faltan argumentos en las acciones")

    # Si la accion es SALIR, terminar el programa.
        elif accion[0] == "SALIR":
            break

        else:
          print("Accion no valida")
