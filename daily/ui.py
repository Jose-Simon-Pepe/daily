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
        self.opcion_actual = None
        self.menu_principal()

    def menu_principal(self):
        cabecera = ""
        accion = ""
        while self.opcion_actual == None:
            visuales.show(self.opciones_principales,"Opciones",accion, cabecera=cabecera)
            # visuales! to_do_index = input("Que deseas hacer?")
            visuales.show("Que deseas hacer","Respuesta","input")
            if to_do_index in self.opciones_principales:
                to_do = self.opciones_principales[to_do_index]
                self.opcion_actual = to_do
                recibido = self.dm.dependencias["router"].routeGet(to_do.replace(" ","_"))
                if to_do.endswith("..."):
                    accion = "input"
                else:
                    accion = None
                respuesta = visuales.show(recibido,"respuesta",accion)
                self.dm.dependencias["router"].routeGet(respuesta)
            else:
                cabecera = "Auch! parece que esa opcion no existe. Reintenta"
                accion = "clear"

if __name__ == "__main__":
   ui = Ui()
   visuales.show("iniciando sin dependency manager","Alerta")
   ui.run()
