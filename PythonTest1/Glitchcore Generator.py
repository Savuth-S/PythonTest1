##Librerias
from PIL import Image
import numpy as np
from random import *
import Console.py

#Atributos
class Glitch1(object):
    """Generates glitch like image from imput"""
    def gemify(pixelValue):
        calc = np.sin(pixelValue)
    
        if pixelValue < randint(10,50):
            return 0
        elif calc >= uniform(0.6,1) and pixelValue > 127:
            return 255
        else: return 0
    
    def maskify(image):
        image = image.convert('RGB')
        r, g, b = image.split()
        r.paste(g, None, g)
        g.paste(b, None, b)
        b.paste(r, None, r)
        a = Image.merge('RGB', (r, g, b))
        a = a.convert('L')
        a = Image.eval(a, lambda a: 0 if a > 254 else a)

        image = Image.merge('RGBA', (r, g, b, a))
        return image

    def maskify2(image):
        image = image.convert('RGB')
        r, g, b = image.split()
        r.paste(g, None, g)
        b.paste(r, None, r)
        
        a = Image.merge('RGB', (r, g, b))
        a = a.convert('L')
        a = Image.eval(a, lambda value: 0 if value > 254 else value)
        a = Image.eval(a, lambda value: value+76 if value > 20 else value)

        r, g, b = image.split()
        r = Image.eval(r, lambda a: 255)
        g = Image.eval(g, lambda a: 255)
        b = Image.eval(b, lambda a: 0)
        image = Image.merge('RGBA', (r, g, b, a))
        return image
        
    def generate(route):
        total = 0
        for file in route:
            total += 1
    
        fileindex = 0
        for file in route:
            fileindex += 1
            print(str(file).split(str("\ ").rstrip(" "))[-1])
            image1 = Image.open(file)

            if str(file).split(".")[-1] == "gif":
                imageSequence = []
                for frame in range(0,image1.n_frames):
                    image1.seek(frame)
                    tempImage = image1
                    tempImage = tempImage.convert('RGBA')
                    image3 = Image.eval(tempImage, lambda a: Glitch1.gemify(a))
                    image3 = Image.eval(image3, lambda a: 255-a)
                    image3 = Glitch1.maskify2(image3)

                    image2 = Image.eval(tempImage, lambda a: Glitch1.gemify(a))
                    image2 = Glitch1.maskify(image2)

                    tempImage.alpha_composite(image2)
                    tempImage.alpha_composite(image3)
                    image2.close()

                    imageSequence.append(tempImage)
                imageSequence[0].save('output/'+str(fileindex)+'-tmparrq352a.'+str(file).split(".")[-1], save_all=True, append_images=imageSequence[1:], loop=0, optimize=False)
                tempImage.close()
            else:
                image1 = image1.convert('RGBA')
                image3 = Image.eval(image1, lambda a: Glitch1.gemify(a))
                image3 = Image.eval(image3, lambda a: 255-a)
                image3 = Glitch1.maskify2(image3)

                image2 = Image.eval(image1, lambda a: Glitch1.gemify(a))
                image2 = Glitch1.maskify(image2)
                
                image2.alpha_composite(image3)
                image1.alpha_composite(image2)
                image2.close()
                image3.close()
                
                if str(file).split(".")[-1] == "png":
                    image1.save('output/'+str(fileindex)+'-tmparrq352a.png')
                else:
                    image1 = image1.convert('RGB')
                    image1.save('output/'+str(fileindex)+'-tmparrq352a.'+str(file).split(".")[-1])

            print(str(fileindex)+"/"+str(total)+"\n")
            image1.close()
        return print('\nDone!\n')