

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_coord(self):
        return self.x, self.y
    
    def set_coord(self, x, y):
        self.x = x
        self.y = y
    
point = Point(10, 20)
print(point.get_coord())
point.set_coord(15,10)
print(point.get_coord())