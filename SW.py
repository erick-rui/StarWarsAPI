class Starship:
    def __init__(self, dataDict):
        self.data = dataDict
        self.name = self.data.get('name')
        self.price = self.data.get("cost_in_credits")


    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCapacity(self):
        return self.data.get("cargo_capacity")

    def getClass(self):
        return self.data.get("starship_class")

    def getModel(self):
        return self.data.get("model")

    def getManufacturer(self):
        return self.data.get("manufacturer")

    def getValueOf(self, userKey=""):
        return self.data.get(userKey)

    def __repr__(self):
        print("The", self.getModel(), "is a", self.getClass(), "built by", self.getManufacturer(), "with a cargo capacity of",
    self.getCapacity(), "units. It costs", self.price, "credits.")

class Planet:
    def __init__(self, dataDict):
        self.data = dataDict
        self.name = self.data.get('name')
        self.climate = self.data.get("climate")

    def getValueOf(self, userKey=""):
        return self.data.get(userKey)

    def __repr__(self):
        print("Name:", self.name, 
        "\nClimate:", self.getValueOf("climate"), 
        "\nTerrain:", self.getValueOf("terrain"))

class Vehicle:
    def __init__(self, dataDict):
        self.data = dataDict
        self.name = self.data.get('name')
        self.model = self.data.get("model")

    def getValueOf(self, userKey=""):
        return self.data.get(userKey)

    def __repr__(self):
        print("Name:", self.name, "\nModel:", self.getValueOf("model"), "\nPrice:", self.getValueOf("cost_in_credits"))
