##ADDING ATTRIBUTES

class Point:
    pass

p1= Point()
p2 = Point()

p1.x = 5
p1.y = 2


p2.x = 9
p2.y = 6

print(p1.x,  p1.y)
print(p2.x,  p2.y)


## MAKING DO SOMETHING
print("MAKING DO SOMETHING")
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)




#RETURN DISTANCE BEETWEEN TWO POINTS
print("RETURN DISTANCE BEETWEEN TWO POINTS")
import math

class Point:
    def move(self, x:float, y:float)-> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other:"Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)

print(point2.calculate_distance(point1))

point1.move(2,3)
print(point2.calculate_distance(point1))

print("INITIALIZING  THE OBJECT")

class Point2:
    def __init__(self, x:float, y:float) -> None:
        self.move(x, y)
    
    def move(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def reset(self)-> None:
        self.move(0,0)

    def calculate_distance(self,other:"Point2") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    
point1 = Point2(2,4)
print("point1", point1.x, point1.y)
point2 = Point2(6,3)
print("point2",point2.x, point2.y)

print("Distance point 1 to point 2: ", point1.calculate_distance(point2))




    
