from pickle import TRUE
from re import X
from tkinter import E
from unicodedata import name
import unittest

import libreria_cuartenion as cu

class TesCuternion(unittest.TestCase):
    def test_invert(self):
        a=cu.cuaternion(1,2,3,4)
        aneg=~a
        x=1
        y=-1
        self.assertEqual(aneg.r>0,x>0)
        self.assertEqual(aneg.i<0,y<0)
        self.assertEqual(aneg.j<0,y<0)
        self.assertEqual(aneg.k<0,y<0)
    def test_med(self):
        a=cu.cuaternion(1,2,3,4)
        aneg=-a
        self.assertEqual(type(aneg),float)
    def test_sum(self):
        a=cu.cuaternion(1,2,3,4)
        b=cu.cuaternion(5,6,7,8)
        x=2
        y=2.75
        c=a+b
        d=a+x
        e=a+y

        self.assertEqual(a.r+b.r,c.r)
        self.assertEqual(a.i+b.i,c.i)
        self.assertEqual(a.j+b.j,c.j)
        self.assertEqual(a.k+b.k,c.k)

        self.assertEqual(a.r+x,d.r)
        self.assertEqual(a.i+x,d.i)
        self.assertEqual(a.j+x,d.j)
        self.assertEqual(a.k+x,d.k)

        self.assertEqual(a.r+y,e.r)
        self.assertEqual(a.i+y,e.i)
        self.assertEqual(a.j+y,e.j)
        self.assertEqual(a.k+y,e.k)

    def test_mul(self):
        a=cu.cuaternion(1,2,3,4)
        b=cu.cuaternion(5,6,7,8)
        x=2
        y=2.75
        c=a*b
        d=a*x
        e=a*y
        self.assertEqual(a.r*b.r-a.i*b.i-a.j*b.j-a.k*b.k,c.r)
        self.assertEqual(a.r*b.i+a.i*b.r+a.j*b.k-a.k*b.j,c.i)
        self.assertEqual(a.r*b.j-a.i*b.k+a.j*b.r+a.k*b.i,c.j)
        self.assertEqual(a.r*b.k+a.i*b.j-a.j*b.i+a.k*b.r,c.k)

        self.assertEqual(a.r*x-a.i*x-a.j*x-a.k*x,d.r)
        self.assertEqual(a.r*x+a.i*x+a.j*x-a.k*x,d.i)
        self.assertEqual(a.r*x-a.i*x+a.j*x+a.k*x,d.j)
        self.assertEqual(a.r*x+a.i*x-a.j*x+a.k*x,d.k)

        self.assertEqual(a.r*y-a.i*y-a.j*y-a.k*y,e.r)
        self.assertEqual(a.r*y+a.i*y+a.j*y-a.k*y,e.i)
        self.assertEqual(a.r*y-a.i*y+a.j*y+a.k*y,e.j)
        self.assertEqual(a.r*y+a.i*y-a.j*y+a.k*y,e.k)


