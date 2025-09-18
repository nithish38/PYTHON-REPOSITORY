class car:
    def __init__(self,brand,model,colour):
        self.brand=brand
        self.model=model
        self.colour=colour
    def display(self):
        print(self.brand)
        print(self.model)
        print(self.colour)
ob=car("BMW","M5","Black")
ob.display()
