class Player:
    
    def __init__(self,name,symbol,id):
        self.name = name
        self.symbol = symbol
        self.id = id
    
    def __str__(self):
        out = f"{self.name},{self.symbol}"
        return out
    
    def getId(self):
        return self.id