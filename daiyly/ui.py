import tomli
import os
import visuales

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
    

    def show(self,thing,kindof):
        visuales.show(thing,kindof)

    def run(self):
        visuales.iniciar_dependencias()
        visuales.presentacion()
        self.menu_principal()

    def menu_principal(self):
        visuales.show(self.opciones_principales,"Opciones")
        to_do_index = input("Que deseas hacer?")
        if to_do_index in self.opciones_principales:
            to_do = self.opciones_principales[to_do_index]
            recibido = self.dm.dependencias["router"].routeGet(to_do.replace(" ","_"))
        else:
            visuales.show("Auch, parece que esa opcion no existe. Reintenta.","Alerta")
            self.menu_principal()

if __name__ == "__main__":
   ui = Ui()
   visuales.show("iniciando sin dependency manager","Alerta")
   ui.run()
