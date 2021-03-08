##Librerias
from PIL import Image
import numpy as np
from random import *

#Atributos
class Glitch1(object):
    """Generates glitch like image from imput"""

    def gemify(a):
        calc = np.sin(a)
    
        if a < randint(10,50):
            return 0
        elif calc >= uniform(0.6,1) and a > 127:
            return 255
        else: return 0
    
    def maskify(image,image2):
        image = image.convert('RGB')
        r, g, b = image.split()
        r.paste(g, None, g)
        g.paste(b, None, b)
        b.paste(r, None, r)
        a = Image.merge('RGB', (r, g, b))
        a = a.convert('L')
        
        image = Image.merge('RGBA', (r, g, b, a))
        return image

    def generate(route):
        total = 0
        for file in route:
            total += 1
    
        fileindex = 0
        for file in route:
            fileindex += 1
            print(file)
            image1 = Image.open(file)

            if str(file).split(".")[-1] == "gif":
                imageSequence = []
                for frame in range(0,image1.n_frames):
                    image1.seek(frame)
                    tempImage = image1
                    tempImage = tempImage.convert('RGBA')

                    image2 = Image.eval(tempImage, lambda a: Glitch1.gemify(a))
                    image2 = Glitch1.maskify(image2,tempImage.convert('RGB'))

                    tempImage.alpha_composite(image2)
                    image2.close()

                    imageSequence.append(tempImage)
                imageSequence[0].save('output/'+str(fileindex)+'-tmparrq352a.'+str(file).split(".")[-1], save_all=True, append_images=imageSequence[1:], duration=image1.info['duration'], loop=0, optimize=False)
                tempImage.close()
            else:
                image1 = image1.convert('RGBA')
                
                image2 = Image.eval(image1, lambda a: Glitch1.gemify(a))
                image2 = Glitch1.maskify(image2,image1.convert('RGB'))
        
                image1.alpha_composite(image2)
                image2.close()
                
                if str(file).split(".")[-1] == "png":
                    image1.save('output/'+str(fileindex)+'-tmparrq352a.'+str(file).split(".")[-1])
                else:
                    image1 = image1.convert('RGB')
                    image1.save('output/'+str(fileindex)+'-tmparrq352a.'+str(file).split(".")[-1])

            print(str(fileindex)+"/"+str(total)+"\n")
            image1.close()
        return print('\nDone!\n')