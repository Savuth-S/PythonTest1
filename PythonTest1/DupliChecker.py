from PIL import Image
import shutil, os, pickle

class Duplicate(object):
    """stuff stuff"""
    def check(route):
        totalFiles = len(route)
        if not os.path.isfile("namelist.db"):
            Duplicate.build(route, 50)
        
        with open("namelist.db", "rb") as database:
            nameList = pickle.load(database)

        fileIndex = 0
        for file in route:
            fileIndex += 1
            print(str(file).split("\ ".rstrip(" "))[-1])

            if os.path.isfile(str(file)):
                image = Image.open(file)
                image = image.convert('RGBA')
                pixelmap = Duplicate.generatePixelmap(image)

                for nameGroup in nameList:
                    if pixelmap == nameGroup[0] and file != nameGroup[1]:
                        print("There's a copy of this image!")  
                        print(str(nameGroup[0])+"\t"+str(nameGroup[1]))
                        print(str(name)+"\t"+str(file))
                        
                        if os.path.isfile(str(nameGroup[1])):
                            shutil.move(str(nameGroup[1]),"output/ " +str(nameGroup[1]).split("\ ".rstrip(" "))[-1])
                        if os.path.isfile(str(file)):
                            shutil.move(str(file),'output/ '+str(file).split("\ ".rstrip(" "))[-1])
                        input()

                if fileIndex < 15 or fileIndex > totalFiles-16:
                    Duplicate.saveThumbnail(image)

                image.close()
            
                print(str(fileIndex)+"/"+str(totalFiles)+"\n")
            else:
                print("\n\nERROR!: File Not Found!\n\n")
        return print('\nDone!\n')
    
    def build(route, maxFiles = 15):
        totalFiles = len(route)
        nameList = list((" ", " "))
        fileIndex = 0

        for file in route:
            fileIndex += 1
            if os.path.isfile(str(file)):
                image = Image.open(file)
                image = image.convert('RGBA')

                pixelmap = generatePixelmap(image)

                nameList.append((str(pixelmap), str(file)))

            print(str(fileIndex)+"/"+str(totalFiles))

            if fileIndex > maxFiles:
                break

        with open("namelist.db",'wb') as database:
            pickle.dump(nameList, database)
        return print("/n/nDatabase build!/n/n")

    def generatePixelmap(image):
        pixelmap = ""
        image = image.resize((int(image.size[0]/(image.size[0]/3)), 
                              int(image.size[1]/(image.size[0]/4))), 
                              Image.NEAREST)
            
        pixelValues= list(image.getdata())
        for channel in pixelValues:
            total = 0
            for pixelValue in channel:
                total += pixelValue
            pixelmap = pixelmap+str(hex(total).lstrip("0x").rstrip("L"))

        return pixelmap

    def saveThumbnail(image):
        image = image.resize((int(image.size[0]/(image.size[0]/3)), 
                              int(image.size[1]/(image.size[0]/4))), 
                              Image.NEAREST)
        image = image.resize((int(image.size[0]*(500/image.size[0])), 
                              int(image.size[1]*(500/image.size[0]))), 
                              Image.NEAREST)
        image.save('output/thumbnails/'+str(Duplicate.generatePixelmap(image))+'.png')
