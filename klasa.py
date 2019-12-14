import sys

class Klasa:
    def __init__(self,x):
        self.x = x
    def string(self,s):
        return self.x.join(s)
k = Klasa('x')
print(k.string(sys.argv))
class Inna:
    def __str__(self):
        return "Siema"
i = Inna()
print(i)

