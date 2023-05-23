import tomli

class ListManager:
    def __init__(self, **options):
        self.dm = None

    def load_toml(self) -> dict:
        with open('daiyly/checklists.toml','rb') as f:
            toml_data: dict = tomli.load(f)
            return toml_data

    def loadChecklists(self):
        data: dict = self.load_toml()
        return(data) 

    def getChecklist(self, name):
        data = self.loadChecklists()
        filtered = data[name][0]
        return filtered

 
if __name__ == "__main__":
    lm = ListManager()
    print(lm.loadChecklists().keys())
