from router import Router
from ui import Ui
from listmanager import ListManager

class DependencyManager:

    def __init__(self, toContain):
        self.dependencias = dict()
        for dependencia in toContain:
            self.dependencias[dependencia]=toContain[dependencia]
        for dependencia in self.dependencias:
            self.dependencias[dependencia].dm = self

if __name__ == "__main__":
    router = Router()
    ui = Ui()
    listmanager = ListManager()
    dm = DependencyManager({"router":router,"ui":ui,"listmanager":listmanager})    
    ui.run()
