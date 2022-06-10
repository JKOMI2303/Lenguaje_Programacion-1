from math import sqrt

class cuaternion(object):
    def __init__(self,r,i,j,k) -> None:
        self.r=r
        self.i=i
        self.j=j
        self.k=k

    def __invert__(self):
        return cuaternion(self.r, -self.i, -self.j, -self.k)
    
    
    def __add__(self, other):
        "    x.__add__(y) <==> x+y"
        if(type(other)==int):
            return cuaternion(self.r + other,
                          self.i + other,
                          self.j + other,
                          self.k + other)
        elif(type(other)==float):
            return cuaternion(self.r + other,
                          self.i + other,
                          self.j + other,
                          self.k + other)
        else:
            return cuaternion(self.r + other.r,
                          self.i + other.i,
                          self.j + other.j,
                          self.k + other.k)
    def __mul__(self, other):
        "    x.__mul__(y) <==> x*y"
        return cuaternion(self.r*other.r-self.i*other.i-self.j*other.j-self.k*other.k,
                          self.r*other.i+self.i*other.r+self.j*other.k-self.k*other.j,
                          self.r*other.j+self.j*other.r+self.k*other.i-self.i*other.k,
                          self.r*other.k+self.k*other.r+self.i*other.j-self.j*other.i)
       

    def __str__(self):
        "    x.__str__() <==> str(x)"
        return "%g%+gi%+gj%+gk" % (self.r, self.i, self.j, self.k)

    def __repr__(self):
        "    x.__repr__() <==> repr(x)"
        return "cuaternion(%g, %g, %g, %g)" % (self.r, self.i, self.j, self.k)
if __name__ == "__main__":


    cuar1=cuaternion(1,2,3,4)
    cuar3=cuaternion(2,3,4,5)
    cuar2=cuar1*cuar3
    x=3
    print(type(x)==int)
    print(str(cuar2))