

class Router:
    def __init__(self):
        self.dm = None

    def routeGet(self, to_do):
        call = getattr(self,to_do) 
        return call()

    def Procesamiento(self):
        print("¡Hola!")
    
    def Revisiones_semanales(self):
        pass

    def Estudio(self):
        pass

    def Ejecutar(self):
        pass

 
if __name__ == "__main__":
    pass
