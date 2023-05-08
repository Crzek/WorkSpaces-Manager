

class WorkSpace():

    def __init__(self, name: str) -> None:
        self.Name = name
        self.Apps: list[object] = []
        self.NumberApps: int = len(self.Apps)

    def __str__(self) -> str:
        return f"{self.Name} -> {self.NumberApps}"

    def __repr__(self) -> str:
        return self.__str__()

    def updateNumberApps(self):
        self.NumberApps = len(self.Apps)

    def rename(self, newName: str):
        self.Name = newName

    def deleteApp(self, Name: str, Id: str = None):
        if (Id == None):
            for app in self.Apps:
                if (Name == self.Name):
                    self.Apps.remove(app)

    def printWSpace(self):
        print(f"Name {self.Name}")
        for app in self.Apps:
            print(f"{app.Name} {app.Id}")
