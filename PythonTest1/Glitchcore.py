from PIL import Image
import numpy as np
from random import *

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
        for infile in route:
            total += 1
    
        fileindex = 0
        for infile in route:
            fileindex += 1
            print(infile)
            image1 = Image.open(infile)
            image1 = image1.convert('RGBA')
    
            image2 = Image.eval(image1, lambda a: Glitch1.gemify(a))
            image2 = Glitch1.maskify(image2,image1.convert('RGB'))
        
            image1.alpha_composite(image2)
            image2.close()
    
            image1.save('output/'+str(fileindex)+'-tmparrq352a.png')
            print(str(fileindex)+"/"+str(total)+"\n")
            image1.close()
        return print('\nDone!\n')

    


