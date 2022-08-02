import unittest
from main import(
    Herencia,
    Tabla_metodos_virtuales
)

class manejador_tablas_metodos_virtuales(unittest.TestCase):

    def test_definir_describir(self):
        tabla=Tabla_metodos_virtuales()
        self.assertEqual(tabla.definir(["Prueba","p"]), "Clase: Prueba metodos {'p': 'Prueba'}")
        self.assertEqual(tabla.describir(["Prueba"]), "p -> Prueba :: p\n")
        self.assertEqual(tabla.definir(["Hijo",":","Prueba","a","b"]), "Clase: Hijo metodos {'p': 'Prueba', 'a': 'Hijo', 'b': 'Hijo'}")
        self.assertEqual(tabla.describir(["Hijo"]), "p -> Prueba :: p\na -> Hijo :: a\nb -> Hijo :: b\n")
        self.assertEqual(tabla.definir(["Hijo2",":","Hijo","c","h","j","z"]), "Clase: Hijo2 metodos {'p': 'Prueba', 'a': 'Hijo', 'b': 'Hijo', 'c': 'Hijo2', 'h': 'Hijo2', 'j': 'Hijo2', 'z': 'Hijo2'}")
        self.assertEqual(tabla.describir(["Hijo2"]), "p -> Prueba :: p\na -> Hijo :: a\nb -> Hijo :: b\nc -> Hijo2 :: c\nh -> Hijo2 :: h\nj -> Hijo2 :: j\nz -> Hijo2 :: z\n")
        self.assertEqual(tabla.definir(["Prueba","a","b"]), " Error: La clase Prueba ya existe")
        self.assertEqual(tabla.describir(["Prueba3"]), " Error: la Prueba3 no existe")
        self.assertEqual(tabla.definir(["Prueba4","a","a"]), "Error: El metodo a no se pueden repetir")

#if __name__ == "__main__":
  # unittest.main()