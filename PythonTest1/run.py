##Librerias
from Glitchcore_Generator import *
from Duplicate_Checker import *
import glob, os, argparse

##Funciones
def checkDirectoryStructure():
    if not os.path.isdir("input"):
       os.mkdir("input")

    if not os.path.isdir("output"):
       os.mkdir("output")
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

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--route', required=True, dest='route',
                        help="theres no help")

parsed_args = parser.parse_args()
                        
route = clean(str(parsed_args.route)+"/*.*")

if len(route) > 0:
    #Glitch2.glitch(route) 
    #Duplicate.build(route, len(route))
    Duplicate.check(route)
    file_index = 0
