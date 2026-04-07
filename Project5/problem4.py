class AA:
    def __init__(self, a=0):
        self.a = a
    def pritnout(self):
        print(self.a)

class BB(AA):
    def __init__(self, b=0):
        self.b = b
    def printout(self):
        print(self.b)

class CC(BB):
    def __init__(self, c=0):
        self.c = c
    def printout(self):
        print(self.c)
