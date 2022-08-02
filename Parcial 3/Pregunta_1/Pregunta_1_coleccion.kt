abstract class Coleccion<T>() {

    // variable pila es representada como una lista mutable, aqui se van a almacenar los elementos
    val pila: MutableList<T> = mutableListOf<T>()

    abstract fun agregar(elem: T) // esto nos asegura que se pueda almacenar cualquier objeto y una funcion abstracta que sera luego reescribida ya que si la clase es conjunto no se repiten y si es bolsa solo se agrega


    // Elimina elementos de la coleccion:
    fun eliminar(elem: T) {
        if (this.buscar(elem)) {
            pila.remove(elem)
        } else {
            println("El elemento $elem no existe")
        }
    }

    // Busca elementos en la coleccion:
    fun buscar(elem: T): Boolean {
        return pila.contains(elem)
    }

    //  imprime los elementos de la coleccion:
    fun imprimir(){
        println(pila.toString())
    }    
    
    //  indica si el conjunto esta vacio o no
    fun esvacio(){
        if (pila.isEmpty()) {
            println("El conjunto está vacío (no tiene elementos).")
        } else {
            println("El conjunto no está vacio.")
        }
    }
}

class Conjunto<T>() : Coleccion<T>() { // clase conjunto que extiende de collecion
    // Funcion agregar para agregar elementos al conjunto, los elementos no se pueden repetir:
    override fun agregar(elem: T) {
        if (!this.buscar(elem)) {
            pila.add(elem)
        }
    }
}

class Bolsa<T>() : Coleccion<T>() {

    // Funcion agregar para agregar elementos a la bolsa, los elementos se pueden repetir:
    override fun agregar(elem: T) {
        pila.add(elem)
    }
}


