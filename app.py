import subprocess


class App:
    def __init__(self, name: str, id: str = None, description: str = ""):
        self.Name = name
        self.Id = id
        self.Description = description

    def __str__(self) -> str:
        return f"NAme: {self.get_Name()} -- Id:{self.get_Id()}"

    def __repr__(self) -> str:
        return self.__str__()

    def get_Id(self):
        return self.Id

    def get_Name(self):
        return self.Name

    def openAppID(self):
        subprocess.run(
            ['powershell.exe', 'Start-Process', '-Id', self.get_Id()])

    def closeAppID(self):
        subprocess.run(
            ['powershell.exe', 'Stop-Process', '-Id', self.get_Id()])
