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
route = glob.glob("input/*.*")
supportedFormats = ["BMP", "DIB", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "MSP", "PCX", "PNG", "PPM", "SGI", "TGA", "TIFF", "WebP"]

index = 0
for file in route:
    ext = str(file).split(".")[-1].upper()
    isNotSupported = True
    for format in supportedFormats:
        if ext == format:
            isSupported = False

    if isNotSupported:
        del route[index]
    index += 1

#Glitch1.generate(route) 
Duplicate.build(route, len(route))
Duplicate.check(route)
