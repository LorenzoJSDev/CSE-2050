class Color:
    def __init__(self, name, code):
        self.color_name = name
        self.color_code = code
    
    def __str__(self):
        return f"the color name is {self.color_name}"
    


class Shape:

    def __init__(self,name):
        self.shape_name = name


    def print_name(self):
        return f"This is a shape name {self.shape_name}"
    



class Sqaure(Shape):
    #if you make a new constructure in the subclass you can not access the self varibles in the superclass unless you use super init
    def __init__(self, s_name, side, color):
        super().__init__(s_name)
        self.side = side
        self.color = color
    
red = Color("Red", "#FF0000")
s = Sqaure("sqaure", 5, red)
print(s.color)