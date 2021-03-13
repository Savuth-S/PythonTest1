##Librerias
from PIL import Image
from random import *
from Console_Commands import *
import os, numpy as np

#Atributos
class Glitch2(object):
    """Generates glitch like image from imput"""
    def glitch(route):
        errors_list = list()
        total_files = len(route)
        file_index = start = end = errors = 0
        Console.ETA(time.localtime(time.time())[5],0,0,0,True)
        
        for file in route:
            start = time.time()
            
            Console.clear()
            print("Current File: "+str(file.split("\ ".rstrip(' '))[-1]))
            Console.progressBar(total_files, file_index, str(file_index)+'/'+str(total_files), Console.ETA(start, end, total_files, file_index), "\n")
            print("Errors found: "+str(errors))
            
            if os.path.isfile(file):
                image = Image.open(file)
                file_index += 1
                
                if str(file).split('.')[-1].lower() == "gif":
                    frames_sequence = []
                    
                    for frame in range(0,image1.n_frames):
                        image.seek(frame)

                        artifacts = generateArtifacts(image)
                        
                        frames_sequence.append(image.convert("RGBA").alpha_composite(artifacts))
                        artifacts.close()
                    
                    frames_sequence[0].save("output/"+str(file_index)+"-tmparrq352a.gif", 
                                            save_all=True, append_images=imageSequence[1:], loop=0, optimize=False)
                    
                    frames_sequence.close()
                    image.close()
                else:
                    artifacts = generateArtifacts(image)
                    image = image.convert("RGBA").alpha_composite(artifacts)
                    
                    if str(file).split('.')[-1].lower() == "png":
                        image.save("output/"+str(file_index)+"-tmparrq352a.png")
                    else:
                        image.convert("RGB").save("output/"+str(file_index)+"-tmparrq352a."+str(file).split('.')[-1])
            else:
                print("\n\nERROR!: File Not Found!\n\n")
                errors += 1
                errorsList.append(("ERROR!: This File Was Not Found!", str(file)))
                time.sleep(2)
            
            end = time.time()
            Console.ETA(start, end, total_files, file_index)
        
        for groups in errors_list:
            print("\nThere was an error with this file!")
            print(str(groups[0])+"\t"+str(groups[1]))
        
        return print("\nDone!\n")

    def generateArtifacts(image, pixel = None):
        if pixel == None:
            image = Image.eval(image.convert("RGB"), lambda pixel: generateArtifacts(pixel = pixel))
            image = Glitch2.mixAndCut(image, Image.eval(image, lambda pixel: 255-pixel))
            return image
        else:
            calc = np.sin(pixel)
            if pixel < randint(10,50):
                return 0
            elif calc >= uniform(0.6,1) and pixel > 127:
                return 255
            else: return 0

    def mixAndCut(artifact1, artifact2):
        #Artifact image 1
        r, g, b = artifact1.convert('RGB').split()
        r.paste(g, None, g)
        g.paste(b, None, b)
        b.paste(r, None, r)
        #Makes alpha mask
        a = Image.merge('RGB', (r, g, b))
        a = a.convert('L')
        a = Image.eval(pixel, lambda pixel: 0 if pixel > 254 else a) #cleaning
        
        artifact1 = Image.merge('RGBA', (r, g, b, a))
        
        #Artifact image 2
        r, g, b = artifact2.convert("RGB").split()
        r.paste(g, None, g)
        b.paste(r, None, r)
        #Makes alpha mask2
        a = Image.merge('RGB', (r, g, b))
        a = a.convert('L')
        a = Image.eval(a, lambda value: 0 if value > 254 else value) #cleaning2
        a = Image.eval(a, lambda value: value+38 if value > 20 else value)
        a.paste(Image.new("L", image.size, 0), None, image2.split()[-1])

        r = g = Image.new("L", image.size,255)
        b = Image.new("L", image.size, 0)
        artifact2 = Image.merge('RGBA', (r, g, b, a))
        
        artifact1.alpha_composite(artifact2)
        
        artifact1.close()
        artifact2.close()
        return artifact1
    
