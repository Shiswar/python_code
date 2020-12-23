# This code is entirely the work of Shae Iswar

# This code will calculate the shortest path beween two points on the surface of a cube where each edge is of length 10
# The points will be described represented as an object of class Point() which has x, y, and z values



import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.co_ords = [self.x, self.y, self.z]
        self.planes = ["x", "y", "z"]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z
    


    

def shortest_path(point1, point2):

    diff_plane = [0, 0, 0] 

    diff1 = 0
    diff0 = 0
  
    for i in range(3):

        if p1.co_ords[i] == p2.co_ords[i]:
            diff_plane[i] = 1
            for i in diff_plane:
                if i == 0:
                    diff1 += ((p1.co_ords[i]-p2.co_ords[i])**2)
            
            rad = math.sqrt(diff1)
            return (2*math.pi*rad)/6
            


        elif p1.co_ords[i] in [0, 10] or p2.co_ords[i] in [0, 10]:
            diff_plane[i] = 1
    
    for i in range(3):
        if diff_plane[i] == 1:
            diff1 += abs(p1.co_ords[i]-p2.co_ords[i])
        else: 
            diff0 = abs(p1.co_ords[i]-p2.co_ords[i])
    
    return math.sqrt(diff0**2 + diff1**2)
    

    
p1 = Point(2, 1, 10)
p2 = Point(0, 5, 9)
print(shortest_path(p1, p2))
    



        

    
    
            

