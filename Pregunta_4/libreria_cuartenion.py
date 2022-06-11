import math
from re import A

class cuaternion(object):
    def __init__(self,r,i,j,k) -> None:
        self.r=r
        self.i=i
        self.j=j
        self.k=k

    def __invert__(self): ## overload of ~
        return cuaternion(self.r, -self.i, -self.j, -self.k)  # ∼(a + bi + cj + dk) = a − bi − cj − dk
    
    
    def __add__(self, other): ## overload of +
        "    x.__add__(y) <==> x+y"
        if(type(other)==int):
            return cuaternion(self.r + other,
                          self.i + other,
                          self.j + other, #(a1+b1i+c1j+d1k)+ int = (a1+int)+(b1int)i+(c1+int)j+(d1+int)k
                          self.k + other)
        elif(type(other)==float):
            return cuaternion(self.r + other,
                          self.i + other,
                          self.j + other, #(a1+b1i+c1j+d1k)+ float = (a1+float)+(b1float)i+(c1+float)j+(d1+float)k
                          self.k + other)
        else:
            return cuaternion(self.r + other.r,
                          self.i + other.i,
                          self.j + other.j,  #(a1+b1i+c1j+d1k)+(a2+b2i+c2j+d2k) = (a1+a2)+(b1+b2)i+(c1+c2)j+(d1+d2)k
                          self.k + other.k)

    def __mul__(self, other):## overload of *
        "x.__mul__(y) <==> x*y"
        if(type(other)==int):
            return cuaternion(self.r*other-self.i*other-self.j*other-self.k*other,
                              self.r*other+self.i*other+self.j*other-self.k*other,#(a1 + b1i + c1j + d1k) ∗ int = a1int − b1int − c1int − d1int+ (a1int + b1int  + c1int − d1int)i+ (a1int − b1int + c1int + d1int)j+ (a1int + b1int − c1int + d1int)k
                              self.r*other-self.i*other+self.j*other+self.k*other,
                              self.r*other+self.i*other-self.j*other+self.k*other)
        elif(type(other)==float):
            return cuaternion(self.r*other-self.i*other-self.j*other-self.k*other,
                              self.r*other+self.i*other+self.j*other-self.k*other, #(a1 + b1i + c1j + d1k) ∗ float = a1float − b1float − c1float − d1float+ (a1float + b1float  + c1float − d1float)i+ (a1float − b1float + c1float + d1float)j+ (a1float + b1float − c1float + d1a2)k
                              self.r*other-self.i*other+self.j*other+self.k*other,
                              self.r*other+self.i*other-self.j*other+self.k*other)
        else:
            return cuaternion(self.r*other.r-self.i*other.i-self.j*other.j-self.k*other.k,
                              self.r*other.i+self.i*other.r+self.j*other.k-self.k*other.j, #(a1 + b1i + c1j + d1k) ∗ (a2 + b2i + c2j + d2k) = a1a2 − b1b2 − c1c2 − d1d2+ (a1b2 + b1a2 + c1d2 − d1c2)i+ (a1c2 − b1d2 + c1a2 + d1b2)j+ (a1d2 + b1c2 − c1b2 + d1a2)k
                              self.r*other.j-self.i*other.k+self.j*other.r+self.k*other.i,
                              self.r*other.k+self.i*other.j-self.j*other.i+self.k*other.r)
    def __neg__(self): #overload of & in this case we are remplace the "&" for "-" , in python unary operators only can overload for unary, &-> this is binary operator 
        "    x.__neg__() <==> -(x)"
        return math.sqrt(self.r*self.r +
                         self.i*self.i + #  &(a + bi + cj + dk) = Raiz(a^2+b^2+c^2+d^2)-> -(a + bi + cj + dk) = Raiz(a^2+b^2+c^2+d^2)
                         self.j*self.j +
                         self.k*self.k)    
       

    def __str__(self):
        "    x.__str__() <==> str(x)"
        return "%g%+gi%+gj%+gk" % (self.r, self.i, self.j, self.k)

    def __repr__(self):
        "    x.__repr__() <==> repr(x)"
        return "cuaternion(%g, %g, %g, %g)" % (self.r, self.i, self.j, self.k)

#Para crear un artenion digamos x para 4 enteros a,b,c,d hacer a=cuaternion(a,b,c,d)
if __name__=='__main__':
    a=cuaternion(1,2,3,4)
    b=cuaternion(2,3,4,5)
    c=a+b
    print(c)
    c=a+5
    print(c)
    c=a+5.555
    print(c)
    c=c*a
    print(c)
    c=-a
    print(c)
    c= ~a
    print(c)
    c=a*4
    print(c)
    c=a*4.5
    print(c)
