class Key:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __eq__(self, other):
        if isinstance(other, Key):
            return self.height == other.height and self.width == other.width

    def __str__(self):
        return f"[ValueA: {self.valuea} | ValueB: {self.width}]<-)"
