class Item():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Item({self.id}, {self.name}, {self.type})"