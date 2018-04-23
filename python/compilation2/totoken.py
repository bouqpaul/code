class Token:
    
    def __init__(self, kind, value, position):
        self.kind = kind
        self.value = value
        self.position = position
    
    def __str__(self):
        return "{} : {}".format(self.kind, self.value)
    
    def equal(self, kind):
        return self.kind == kind