# This code allowes to classify point and rectangle objects and do a few operations with them.

# A point is classified by its x and y coordinates in a cartesian plan.
# A rectangle is classified by the location of one of its bottom left corner(x,y), its heigth and it width.


class Points:
        """DEFINES POINTS ON A CARTESIAN PLANE BASED ON X,Y COORDINATES."""
        
        def __init__(self, initX, initY):
                self.x = initX
                self.y = initY
                
        def getX(self):
                return self.x
        
        def getY(self):
                return self.y
        
        def __str__(self): # Allowes to print x and y as strings.
                return "x=" + str(self.x) + ", y=" + str(self.y)

        
class Rectangles:
        """DEFINES RECTANGLES ON A CARTESIAN PLANE BASED ON CORNERPOINT LOCATION (Points(x,y), WIDTH AND HEIGTH."""
        
        def __init__(self, cornerpoint, width, heigth):
                self.corn = cornerpoint
                self.width = width
                self.heigth = heigth
        
        def getCorner(self): 
                return self.corn
                 
        def getWidth(self):
                return self.width
        
        def getHeigth(self):
                return self.heigth
        
        def area(self): # Returns the area of the rectangle. 
                return (self.width*self.heigth)
        
        def perimiter(self): # Returns the perimiter of the rectangle.
                return (self.width*2)+(self.heigth*2)
        
        def transpose(self): # Inverts heigth and width transposing the rectangle.
                oldWidth = self.width
                oldHeigth = self.heigth
                
                self.width = oldHeigth
                self.heigth = oldWidth
                
        def contains(self,point):  
                """ Defines if a point is contained within the area or perimiter of a Rectangles()."""
                
                # if the x value of a given point is smaller than the x value of the rectangle's left corners or
                # bigger than x value of the rectangle's right corners, then point is always found outside the rectangle.
                if point.x > (self.corn).getX()+self.width or point.x < (self.corn).getX():
                        return False
                else:
                        # if instead the x value of a point is found within the x values of the left and right corners of the rectangle, the point will be inside
                        # the rectangle only if its y value is found between the y values of the lower and upper corners.
                        if point.y > (self.corn).getY()+self.heigth or point.y < (self.corn).getY():
                                return False
                        else:
                                return True
                                
        def collides(self, rect):
                """Defines if 2 Rectangles() in a Cartesian plane collide (overlap)."""
                
                if self.contains(rect.corn):
                        return True
                
                # if x of the bottom left corner of the tested rectangle is found within the x values of the base of the reference rectangle then
                # the 2 rectangles are in collision if y of the base of the tested rectangle is larger than y of the base of the reference rectangle.
                
                if (rect.corn).getX()<=(self.corn).getX()+self.width and (rect.corn).getX()>=(self.corn).getX()\
                and (rect.corn).getY()+rect.heigth>=(self.corn).getY():
                        return True
                
                # if x of the bottom left corner of the tested rectangle does not fall inside the x values of the base of the reference rectangle
                # the two rectangles will collide only if the fallowing are all true:
                # - x of the bottom left corner of the tested rectangle is smaller or equal than x of the bottom right corner of the reference rectangle;
                # - x of the bottom right corner of the tested rectangle is larger or equal than x of the bottom left corner of the reference rectangle;
                # - y of the lower base of the tested rectangle is smaller or equal than y of the upper base of the reference rectangle;
                # - y of the upper base of the tested rectangle is larger or equal than y of the lower base of the reference reclangle.
                
                if  (rect.corn).getX()<=(self.corn).getX()+self.width and (rect.corn).getX()+rect.width>=(self.corn).getX()\
                and (rect.corn).getY()+rect.heigth>=(self.corn).getY() and (rect.corn).getY()<=(self.corn).getY()+self.heigth:
                        return True
                        
                else:
                        return False
                
        
        def __str__(self): # allows to print corner, width and heigth as strings.
                return "corner=(" + str(self.corn) + "), width=" + str(self.width) + ", heigth=" + str(self.heigth)

             
rec = Rectangles(Points(3,3), 3, 2)  # This will be used as a reference rectangle: Returns True if tested with collides(rec) because it will coincide with itself.
rec2 = Rectangles(Points(5,4), 2, 2) # Created to partially overlap with rec in a cartesian plane
rec3 = Rectangles(Points(2,2), 2, 4) # Partially overlaps
rec4 = Rectangles(Points(5,2), 2, 4) # Partially overlaps
rec5 = Rectangles(Points(7,1), 3, 2) # Does not overlap 
rec6 = Rectangles(Points(1,1), 1, 1) # Does not overlap
rec7 = Rectangles(Points(2,2), 6, 2) # Partially overlaps
rec8 = Rectangles(Points(2,2), 6, 4) # Fully overlaps
rec9 = Rectangles(Points(2,6), 6, 4) # Does not overlap


print ("Testing sample rectangles...")
print(rec.collides(rec)) # Returns True
print(rec.collides(rec2))# Returns True
print(rec.collides(rec3))# Returns True
print(rec.collides(rec4))# Returns True
print(rec.collides(rec5))# Returns False 
print(rec.collides(rec6))# Returns False
print(rec.collides(rec7))# Returns True
print(rec.collides(rec8))# Returns True
print(rec.collides(rec9))# Returns False               