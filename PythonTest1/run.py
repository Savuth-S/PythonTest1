##Librerias
from Glitchcore_Generator import *
from Duplicate_Checker import *
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

def clean(folder):
    route = glob.glob(folder)
    supportedFormats = ["BMP", "DIB", "EPS", "GIF", "ICNS", "ICO", "IM", "JPG", "JPEG", "MSP", "PCX", "PNG", "PPM", "SGI", "TGA", "TIFF", "WEBP"]
    for file in glob.glob(folder):
        ext = str(file).split(".")[-1].upper()
        isNotSupported = True
        
        for format in supportedFormats:
            if ext == format:
                isNotSupported = False
                break
                
        if isNotSupported:
            index = route.index(file)
            del route[route.index(file)]
    return route

##Codigo
checkDirectoryStructure()
route = clean("input/*.*")

Glitch2.glitch(route) 
#Duplicate.build(route, len(route))
#Duplicate.check(route)
