import json,os

directory = os.path.dirname(__file__)
path = os.path.join(directory, "info.json")

with open(path) as file:
    info = json.load(file)


class Cookie:
    name = ""
    description = ""
    sugar = "",
    forP = "",
    fat = ""
    i = -1

    def setLabel(self, index):
        if index == -1:
             return
        
        self.i = index;
        self.name = info["name"][index]
        self.description = info["description"][index]
        self.sugar = info["sugar"][index]
        self.forP = info["for"][index]
        self.fat = info["fat"][index]


