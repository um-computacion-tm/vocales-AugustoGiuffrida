import unittest

def contar_vocales(mystring):
    resultado = {}
    mystring = mystring.lower()
    mystring = mystring.replace("á","a")
    mystring = mystring.replace("é","e")
    mystring = mystring.replace("í","i")
    mystring = mystring.replace("ó","o")
    mystring = mystring.replace("ú","u")
    mystring = mystring.replace(" ","")  
    for letra in mystring:

        if letra in "aeiou":
            if letra not in resultado:
                resultado[letra]=0
            resultado[letra] +=1    
    return resultado        


class TestContarVocales(unittest.TestCase):

    def test_nada(self):
        resultado= contar_vocales("zzz")
        self.assertEqual(resultado,{})

    def test_contar_a(self):
        resultado= contar_vocales("cas")
        self.assertEqual(resultado,{"a":1})

    def test_contar_aa(self):
        resultado= contar_vocales("casa")
        self.assertEqual(resultado,{"a":2})

    def test_contar_bese(self):
        resultado= contar_vocales("bese")
        self.assertEqual(resultado,{"e":2})

    def test_contar_besa(self):
        resultado= contar_vocales("besa")
        self.assertEqual(resultado,{"a":1,"e":1})       

    def test_Aérea(self):
        resultado= contar_vocales('Aérea')
        self.assertEqual(resultado, {"a":2,"e":2})

    def test_neUquén(self):
        resultado= contar_vocales('neUquén')
        self.assertEqual(resultado, {"e":2,"u":2})    

    def test_Riachuelo(self):
        resultado= contar_vocales('Riachuelo')
        self.assertEqual(resultado, {"a":1,"e":1, "i":1,"o":1, "u":1})        

    def test_Murciélago(self):
        resultado= contar_vocales('Murciélago')
        self.assertEqual(resultado, {"a":1,"e":1, "i":1,"o":1, "u":1}) 

unittest.main()

#while (True):
#    palabra = input("Ingrese palabra: ")
#    print(contar_vocales(palabra))
    
    