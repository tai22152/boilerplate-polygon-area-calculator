class Rectangle:
    def __init__(self, width, height):
        self.height = height;
        self.width = width;

    def __repr__(self) ->str:
        s = f"Rectangle(width={str(self.width)}, height={str(self.height)})"
        return s;



    def set_width(self, width):
        self.width = width;
    
    def set_height(self, height):
        self.height = height;
    
    def get_area(self):
        area = self.width * self.height;
        return area;
    
    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height);
        return perimeter;

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal;
    
    def get_picture(self):
        if(self.width >=50 or self.height >= 50):
            return "Too big for picture.";
        pic = f"";
        for n in range(0,self.height,1):
            pic+=f"{'*'*self.width}\n";
        return pic;

    def get_amount_inside(self, shape):
        
        width_times = self.width // shape.width;
        height_times = self.height // shape.height;
        return width_times * height_times;


class Square(Rectangle):
    def __init__(self, length):
       self.height = length;
       self.width = length;
    def set_side(self, length):
        self.height = length;
        self.width = length;
    
    def __repr__(self) ->str:
        s = f"Square(side={self.width})"
        return s;
