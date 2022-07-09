import unittest
from main import (
    evaluar,
    mostrar,
    prefijo,
    postfijo
)

class manejadordeexpresionessobrebooleanos(unittest.TestCase):
    def test_evaluar(self):
        self.assertEqual(evaluar("=>","false","false"),"true")
        self.assertEqual(evaluar("=>","false","true"),"true")
        self.assertEqual(evaluar("=>","true","false"),"false")
        self.assertEqual(evaluar("=>","true","true"),"true")

        self.assertEqual(evaluar("&","false","false"),"false")
        self.assertEqual(evaluar("&","false","true"),"false")
        self.assertEqual(evaluar("&","true","flase"),"false")
        self.assertEqual(evaluar("&","true","true"),"true")

        self.assertEqual(evaluar("|","false","false"),"false")
        self.assertEqual(evaluar("|","false","true"),"true")
        self.assertEqual(evaluar("|","true","flase"),"true")
        self.assertEqual(evaluar("|","true","true"),"true")

        self.assertEqual(evaluar("^","true",""),"false")
        self.assertEqual(evaluar("^","false",""),"true")
    def test_mostrar(self):
        self.assertEqual(mostrar("=>","true","false"),"(true => false)")

        self.assertEqual(mostrar("&","false","true | false"),"false & (true | false)")
        self.assertEqual(mostrar("&","true","false"),"true & false")

        self.assertEqual(mostrar("|","false","true & false"),"false | (true & false)")
        self.assertEqual(mostrar("|","true","false"),"true | false")

        self.assertEqual(mostrar("^","false",""),"^ false")
        self.assertEqual(mostrar("^","true",""),"^ true")
        self.assertEqual(mostrar("^","","false"),"^ false")
        self.assertEqual(mostrar("^","","true"),"^ true")
    def test_prefijo(self):
        self.assertEqual(prefijo("EVAL",["|", "&","=>","true", "true" ,"false" ,"true"]),"true")
        self.assertEqual(prefijo("MOSTRAR",['|', '&', '=>', 'true', 'true', 'false', 'true']),"(true => true) & false | true")
        self.assertEqual(postfijo("EVAL",["true", "false","=>","false","|","true", "false","^","|","&"]),"false")
        self.assertEqual(postfijo("MOSTRAR",["true" ,"false" ,"=>", "false", "|" ,"true", "false" ,"^" ,"|", "&"]),"(true => false) | false & (true | ^ false)")





##if __name__ == "__main__":
   ## unittest.main()
    