import time
import matplotlib.pyplot as plt




def funcion_alpha_beta_recursiva(n: int)->int:
    #
    if 0<=n<28:
        return n
    elif n>=28:
        return funcion_alpha_beta_recursiva(n-7*1)+funcion_alpha_beta_recursiva(n-7*2)+funcion_alpha_beta_recursiva(n-7*3)+funcion_alpha_beta_recursiva(n-7*4)
def funcion_alpha_beta_cola(n: int, lista_de_sucesiones: list, i=0)->int:
    if 0<=n<28:
        return lista_de_sucesiones[n+i]
        ## Utilizaremos la lista de los primeros 28 numeros naturales
        # Para ampliar el valor  con los elementos bases que ya existen o con los calculados y se incorpora con la llamada recursiva anterior 
        # y el valor i sera un indice que sirve para ir desplazandove por la lista de suceciones:
        # # sucesionAB[28] = lista_de_sucesiones[21+0]+lista_de_sucesiones[14+0]+lista_de_sucesiones[7+0]+lista_de_sucesiones[0+0]
        # de esta forma nos aseguramos de incorporar un resultado para numeros mayotes o iguales a 28
    elif n>=28:
        lista_de_sucesiones.append(lista_de_sucesiones[21+i]+lista_de_sucesiones[14+i]+lista_de_sucesiones[7+i]+lista_de_sucesiones[0+i])

        return funcion_alpha_beta_cola(n-1,lista_de_sucesiones,i+1)
def funcion_alpha_beta_iterativa(n: int)->int:
    lista_de_sucesiones=[i for i in range(28)]
    if 0<=n<28:
        return n
    elif n>=28:
        #de igual forma que en funcion de cola utilizarmeos i para desplazarnos por la lista_de_sucesiones
        # E igual usaremos la idea para ir gneeando los valores solo que ahora no de manera recursiva si no con otro ciclo
        i=0
        for j in range(28,n+1):
             lista_de_sucesiones.append(lista_de_sucesiones[21+i]+lista_de_sucesiones[14+i]+lista_de_sucesiones[7+i]+lista_de_sucesiones[0+i])
             i=i+1
        return lista_de_sucesiones[len(lista_de_sucesiones)-1]
        


if '__main__' == __name__:
    print("ingrese el numero de pruebas es decir un n tal que las pruebas seran con numeros de 0 hasta n")
    final = int(input("Ingrese el numero final de pruebas de n: "))
    pasos = int(input(f"Ingrese el numero pasos desde 0 hasta {final}: "))

    # Inicializacion de variables
    valores = [i for i in range(0, final+pasos, pasos)]
    
    X=1
    Y=0
    Z=9
    alpha=((X+Y)%5)+3
    beta=((Y+Z)%5)+3
    k=alpha*beta
    # Arreglos de tuplas con los tiempos de ejecucion de las funciones y sus respectivos resultados
    resultados_recursiva = []
    resultados_recursiva_cola = []
    resultados_iterativo = []

    for n in valores:

        # Version Recursiva
        tiempo_inicial = time.time()
        resultado = funcion_alpha_beta_recursiva(n)
        tiempo_final = time.time()

        resultados_recursiva.append((resultado, tiempo_final - tiempo_inicial))

        # Version Recursiva de cola
        # Lista de los primeros 49 numeros naturales
        lista_de_sucesiones = [i for i in range(k)]
    
        tiempo_inicial = time.time()
        resultado = funcion_alpha_beta_cola(n, lista_de_sucesiones)
        tiempo_final = time.time()

        resultados_recursiva_cola.append((resultado, tiempo_final - tiempo_inicial))

        # Version Iterativa
        tiempo_inicial = time.time()
        resultado = funcion_alpha_beta_iterativa(n)
        tiempo_final = time.time()

        resultados_iterativo.append((resultado, tiempo_final - tiempo_inicial))

    # Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"-----------------------------------------------------------------------------------")
    print(f"n \t\t|| Funcion Recursiva \t || Funcion Recursiva Cola || Funcion Iterativo")
    print(f"-----------------------------------------------------------------------------------")
    for i in range(len(valores)):
        if resultados_recursiva[i][0] < 10000:
            print(f"{valores[i]} \t\t|| {resultados_recursiva[i][0]} \t\t\t || {resultados_recursiva_cola[i][0]} \t\t\t  || {resultados_iterativo[i][0]}")
        else:
            print(f"{valores[i]} \t\t|| {resultados_recursiva[i][0]} \t\t\t || {resultados_recursiva_cola[i][0]} \t\t\t  || {resultados_iterativo[i][0]}")

    print(f"\n\nTiempos de ejecucion en segundos:")
    print(f"-----------------------------------------------------------------------------------")
    print(f"n \t\t|| Funcion Recursiva \t|| Funcion Recursiva Cola \t||Funcion Iterativa")
    print(f"-----------------------------------------------------------------------------------")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t|| {resultados_recursiva[i][1]:.5f} \t\t|| {resultados_recursiva_cola[i][1]:.5f} \t\t\t|| {resultados_iterativo[i][1]:.5f}")


    # Graficamos los resultados
    plt.plot(valores, [i[1] for i in resultados_recursiva], label="Recursiva")
    plt.plot(valores, [i[1] for i in resultados_recursiva_cola], label="Recursiva Cola")
    plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
    plt.xlabel("Valor de n")
    plt.ylabel("Segundos")
    plt.title("Tiempos de resultados de la ejecucion")
    plt.legend()
    plt.show()

#COMPARAONDO RECURSIVA DE COLA CON ITERATIVA
    print(f"Comparacion de Recursiva de cola con la Iterativa")
# Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva Cola \t|| Iterativa")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
         print(f"{valores[i]} \t\t|| {resultados_recursiva_cola[i][0]} \t\t|| {resultados_iterativo[i][0]}")

    print(f"\n\nTiempos de ejecucion en segundos:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva Cola \t|| Iterativa")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t|| {resultados_recursiva_cola[i][1]:.5f} \t\t|| {resultados_iterativo[i][1]:.5f}")


     # # Graficamos los resultados
    plt.plot(valores, [i[1] for i in resultados_recursiva_cola], label="Recursiva Cola")
    plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
    plt.xlabel("Valor de n")
    plt.ylabel("Segundos")
    plt.title("Tiempos de resultados de la ejecucion")
    plt.legend()
    plt.show()

#COMPARAONDO RECURSIVA DE COLA CON ITERATIVA
    print(f"Comparacion de recursiva con recursiva de cola")
# Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva \t|| Recursiva de cola")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
         print(f"{valores[i]} \t\t|| {resultados_recursiva[i][0]} \t\t|| {resultados_recursiva_cola[i][0]}")

    print(f"\n\nTiempos de ejecucion en segundos:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva Cola \t|| Iterativo")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t|| {resultados_recursiva[i][1]:.5f} \t\t|| {resultados_recursiva_cola[i][1]:.5f}")


     # # Graficamos los resultados
    plt.plot(valores, [i[1] for i in resultados_recursiva], label="Recursiva")
    plt.plot(valores, [i[1] for i in resultados_recursiva_cola], label="Recursiva Cola")
    plt.xlabel("Valor de n")
    plt.ylabel("Segundos")
    plt.title("Tiempos de resultados de la ejecucion")
    plt.legend()
    plt.show()

#COMPARAONDO RECURSIVA DE COLA CON ITERATIVA
    print(f"Comparacion de recursiva con la iterativa")
# Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva \t|| Iterativo")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
         print(f"{valores[i]} \t\t|| {resultados_recursiva[i][0]} \t\t|| {resultados_iterativo[i][0]}")

    print(f"\n\nTiempos de ejecucion en segundos:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t|| Recursiva \t|| Iterativo")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t|| {resultados_recursiva[i][1]:.5f} \t\t|| {resultados_iterativo[i][1]:.5f}")


     # # Graficamos los resultados
    plt.plot(valores, [i[1] for i in resultados_recursiva], label="Recursiva")
    plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
    plt.xlabel("Valor de n")
    plt.ylabel("Segundos")
    plt.title("Tiempos de resultados de la ejecucion")
    plt.legend()
    plt.show()


