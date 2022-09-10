class Saludo():
    def __init__(self,men):
        self.mensaje=men

    def saludar(self):
        print("Hola bienvenidos a phyton{0}".format(self.mensaje))

    def setMensaje(self, men):
        self.mensaje=men

    def numero(self):
        for i in range(3):
            self.saludar()

    def getMensaje(self):
        return self.mensaje