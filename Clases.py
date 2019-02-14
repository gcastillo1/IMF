# -*- coding: utf-8 -*-
""" programa de prueba de clases """
class datosVero:
        def __init__(self, numero):
            self.numero = numero
            print ("tenemos ", numero, "cuartos")

        def telefono(self):
            if self.numero == 1:
                self.telefono = "04120969193"
                print ( self.telefono)
            else:
                self.telefono = "04120965805"
                print (self.telefono)

        def email(self):
            self.email = "vero_july@hotmail.com"
            print (self.email)

print ("numero de cuartos en su casa")
veronica=datosVero(1)
print (" su numero de telefono")
veronica.telefono()
print (" su email")
veronica.email()
""" ahora vamos a practicar la herencia"""

class datosGus(datosVero):
        pass

gustavo=datosVero(2)
gustavo.telefono()
