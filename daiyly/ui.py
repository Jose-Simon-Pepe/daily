import tomli

class Ui:

    def __init__(self):
        self.dm = None
        self.opciones_principales = self.getOpciones("principales")

    def load_toml(self) -> dict:
        with open('daiyly/opciones.toml','rb') as f:
            toml_data: dict = tomli.load(f)
            return toml_data

    def loadOpciones(self):
        data: dict = self.load_toml()
        return(data) 

    def getOpciones(self, cuales):
        data = self.loadOpciones()
        cuales = "opciones_"+cuales
        filtered = {key: data[key] for key in [cuales]}
        return filtered
    

    def show(self,thing):
        print(thing)

    def run(self):
        self.menu_principal()

    def menu_principal(self):
        for opcion in self.opciones_principales:
            print(opcion,self.opciones_principales[opcion])
        to_do = input("Que deseas hacer?")
        recibido = self.dm.dependencias["router"].routeGet(to_do,self.dm)


if __name__ == "__main__":
   ui = Ui()
   ui.run()
