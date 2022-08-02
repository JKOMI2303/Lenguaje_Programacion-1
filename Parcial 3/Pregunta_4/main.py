
class Herencia:
    def __init__(self, nombre_clase : str  , metodos_clase:list,metodos_herencia={},clase_padre=None):
        self.nombre_clase=nombre_clase 
        self.metodos_herencia= metodos_herencia ## se inicializa el atributo con un diccionario que va a contener todos los metodos de las herencias con sus clases respectivas
        self.clase_padre=clase_padre ## clase padre en la herencia simple

        if(isinstance(self.clase_padre, Herencia)):
            self.metodos_herencia=clase_padre.metodos_herencia.copy() ## si la clase pasada como parametro al constructor es una instancia en la clase Herencia se copian sus metodos a la Clase(hija) en la hernecia simple
        for x in metodos_clase:
            self.metodos_herencia[x]= nombre_clase ##los metodos de la clase padre que existen se reemplazan x=nombre del metodo valor=nombre de la clase

class Tabla_metodos_virtuales:
    def __init__(self) -> None:
        self.tabla={} ## tabla que maneja las clases y sus metodos 
    def definir(self,accion :list):
        hijo=accion[0]
        if hijo in self.tabla:
            return f" Error: La clase {hijo} ya existe"
        else:
            if accion[1]==":": ## hereda de la clase padre que esta en accion[2]
                padre=accion[2]
                if padre in self.tabla:
                    clasepadre=self.tabla[padre]
                    metodoshijo=accion[3:]
                else:
                    return f" Error: la clase {padre} no existe"
            else:
                clasepadre=None
                metodoshijo =accion[1:]

            for x in metodoshijo:
                contador=metodoshijo.count(x)
                if(contador>1):
                    return f"Error: El metodo {x} no se pueden repetir"
                else:
                    pass
            clasehijo= Herencia(hijo,metodoshijo,{},clasepadre)

            self.tabla[hijo]=clasehijo

            return f"Clase: {hijo} metodos {clasehijo.metodos_herencia}"
    def describir(self,accion: str):
        if accion[0] in self.tabla:
            clase=self.tabla[accion[0]]
            meetodos_clases=clase.metodos_herencia.copy()
            resultado=""
            for metodo in meetodos_clases.keys():
               resultado+=f"{metodo} -> {clase.metodos_herencia[metodo]} :: {metodo }\n"
            
            return resultado
        else:
            return  f" Error: la {accion[0]} no existe"



if __name__ == "__main__":
    tabla = Tabla_metodos_virtuales()
    while True:
        print("\nIngrese una accion:\nCLASS <tipo> <nombre>\nDESCRIBIR <nombre> <expr>\nSALIR\n\n")
        accion = input("")
        accion = accion.strip().split()
        if accion:
            if accion[0] == "CLASS":
                mensaje = tabla.definir(accion[1:])
            elif accion[0] == "DESCRIBIR":
                mensaje = tabla.describir(accion[1:])
            elif accion[0] == "SALIR":
                exit()

            else:
                mensaje = "Ingrese una acción válida"
        else:
            mensaje = "No ha ingresado ninguna accion"
    
        print(mensaje)

    