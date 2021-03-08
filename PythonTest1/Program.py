##Librerias
from Glitchcore import *
from DuplicateChecker import *
import glob, os

##Funciones
def invert(image):
    image = Image.eval(image, lambda a: 255-a)
    return image

##Codigo
route = glob.glob("input/*.*")
#Glitch1.generate(route) 
Duplicate.build(route)
#Duplicate.check(route)
