##Librerias
from Glitchcore import *
from DupliChecker import *
import glob, os

##Funciones
def checkDirectoryStructure():
    if not os.path.isdir("input"):
       os.mkdir("input")

    if not os.path.isdir("output"):
       os.mkdir("output")

    if not os.path.isdir("output/thumbnails"):
       os.mkdir("output/thumbnails")
    return None

##Codigo
checkDirectoryStructure()
route = glob.glob("input/*.png")
#Glitch1.generate(route) 
Duplicate.build(route, len(route))
Duplicate.check(route)
