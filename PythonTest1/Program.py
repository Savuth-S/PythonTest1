##Librerias
from Glitchcore import *
import glob, os

##Funciones
def invert(image):
    image = Image.eval(image, lambda a: 255-a)
    return image

##Codigo
Glitch1.generate(glob.glob('input/*.*'))
    

    
    