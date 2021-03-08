##Librerias
from Glitchcore import *
from FilenameGenerator import *
import glob, os

##Funciones
def invert(image):
    image = Image.eval(image, lambda a: 255-a)
    return image

##Codigo
#Glitch1.generate(glob.glob('input/*.*')) 
Name.generate(glob.glob('input/*.*'))