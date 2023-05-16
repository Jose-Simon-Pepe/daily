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
        self.opciones = data
        return(data) 

    def getOpciones(self, cuales):
        data = self.loadOpciones()
        filtered = data["opciones_"+cuales][0]
        return filtered
    

    def show(self,thing):
        print(thing)

    def run(self):
        self.menu_principal()

    def menu_principal(self):
        for opcion in self.opciones_principales:
            print(opcion,self.opciones_principales[opcion])
        to_do_index = input("Que deseas hacer?")
        to_do = self.opciones_principales[to_do_index]
        recibido = self.dm.dependencias["router"].routeGet(to_do)


if __name__ == "__main__":
   ui = Ui()
   ui.run()
