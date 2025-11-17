class Vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mult__(self,other):
        return Vector3D(self.x*other.x,self.y*other.y,self.z*other.z)
    def __eq__(self,other):
        return  Vector3D(self.x==other.x,self.y==other.y,self.z==other.z)
v1=Vector3D(3,5,7)
v2=Vector3D(1,2,3)
print("Vector1 = ",v1)
print("Vector2 = ",v2)
print("Addition = ",v1+v2)
print("Substraction = ",v1-v2)
print("Multiplication = ",v1*v2)
print("Equallity = ",v1 == v2)
        
    