class MyExeptionClaass(Exception):
    def __init__(self, number):
        if number:
            self.number = number
        else:
            self.number = None

    def reaction(self):
        print("something goes wrong")
        if self.number == 5:
            return "MyExeptionClaass", self.number
        else:
            return "MyExeptionClaass has been raised"

try:
    raise MyExeptionClaass(4)
except MyExeptionClaass as ex:
    print(ex.reaction())
