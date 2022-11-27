class Key:
    valueA = 0
    valueB = 0

    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB

    def __eq__(self, other):
        if(isinstance(other, self)):
            return self.valueA == other.valueA and self.valueB == other.valueB

    def __str__(self):
        return f"[ValueA: {self.valuea} | ValueB: {self.valueB}]<-)"