import os
import colorama

def iniciar_dependencias():
    colorama.init()

def separador():
    print("")
    print("8888888 8888888 8888888 8888888 8888888 8888888 8888888 8888888 8888888")
    print("")


def presentacion():
    os.system("clear")
    separador()
    print("     .o8             o8o  oooo              \n\
     \"888             `\"'  `888              \n\
 .oooo888   .oooo.   oooo   888  oooo    ooo \n\
d88' `888  `P  )88b  `888   888   `88.  .8'  \n\
888   888   .oP\"888   888   888    `88..8'   \n\
888   888  d8(  888   888   888     `888'    \n\
`Y8bod88P\" `Y888\"\"8o o888o o888o     .8'     \n\
                                 .o..P'      \n\
                                 `Y8P'       \n\
                                             ")

def show(things,kindof, accion=None, **cabecera):
    if kindof.upper() == "ALERTA" or kindof.upper() == "ALERTAS":
        context = Context(MostrarAlertas(things))
        context.execute_strategy()
    if kindof.upper() == "OPCION" or kindof.upper() == "OPCIONES":
        context = Context(MostrarOpciones(things, cabecera,accion))
        context.execute_strategy()

class Strategy:
    def execute(self):
        pass

class MostrarOpciones(Strategy):

    def __init__(self,opciones,cabecera,accion):
        self.opciones = opciones
        self.cabecera = cabecera
        self.accion = accion

    def execute(self):
        if self.accion and self.accion == "clear":
            os.system("clear")
            presentacion()
        if self.cabecera:
            for dato in self.cabecera:
                print(colorama.Fore.GREEN + self.cabecera[dato])
        print(colorama.Fore.BLUE + "~~~~~~~~~~>Opciones<~~~~~~~~~~")
        for opcion in self.opciones:
            print(">",opcion,self.opciones[opcion])
        colorama.Style.RESET_ALL

class MostrarAlertas(Strategy):

    def __init__(self, alertas):
        self.alertas = alertas

    def execute(self):
        print(colorama.Fore.RED + "¡¡¡¡≈!!!!")
        if isinstance(self.alertas,str):
            print(">",self.alertas)
        else:
            for alerta in self.alertas:
                print(">",alerta)
        print("¡¡¡¡≈!!!!")
        colorama.Style.RESET_ALL

class MostrarOpcionesConAlerta(Strategy):

    def __init__(self, alertas, alerta_cabecera):
        self.alertas = alertas

    def execute(self):
        print(colorama.Fore.RED + self.cabecera)
        print(colorama.Fore.BLUE + "~~~~~~~~~~>Opciones<~~~~~~~~~~")
        for opcion in self.opciones:
            print(">",opcion,self.opciones[opcion])
        colorama.Style.RESET_ALL


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()
