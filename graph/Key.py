class Key:
    height = 0
    width = 0

    def __init__(self, valueA, valueB):
        self.height = valueA
        self.width = valueB

    def __eq__(self, other):
        if(isinstance(other, self)):
            return self.height == other.height and self.width == other.width

    def __str__(self):
        return f"[ValueA: {self.valuea} | ValueB: {self.width}]<-)"