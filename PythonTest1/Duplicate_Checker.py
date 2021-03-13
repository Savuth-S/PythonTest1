from PIL import Image
from Console_Commands import *
import time, os, shutil, pickle

class Duplicate(object):
    """stuff stuff"""
    def check(route):
        total_files = len(route)
        start = end = file_index = copies = errors = 0
        copies_list = errors_list = copies_index = list()
        Console.ETA(time.localtime(time.time())[5],0,0,0,True)
        
        if not os.path.isfile("database/namelist.db"):
            Duplicate.build(route, total_files)
        
        with open("database/namelist.db", "rb") as database:
            name_list = pickle.load(database)
            
        Console.clear()
        print("Current File: "+str(route[0]).split("\ ".rstrip(" "))[-1])
        Console.progressBar(total_files, file_index, str(file_index)+"/"+str(total_files))
        print("Copies found: "+ str(copies))
        print("Errors found: "+ str(errors))
            
        for file in route:
            start = time.time()
            file_index += 1
            
            if os.path.isfile(str(file)):
                image = Image.open(file)
                image = image.convert('RGBA')
                pixelmap = ""
                for nameGroup in name_list:
                    if file == nameGroup[1]:
                        pixelmap = nameGroup[0]
                        break

                for nameGroup in name_list:
                    if pixelmap == nameGroup[0] and file != nameGroup[1]:
                        if os.path.isfile(str(nameGroup[1])):
                            shutil.move(str(nameGroup[1]),"output/ " +str(nameGroup[1]).split("\ ".rstrip(" "))[-1])
                        if os.path.isfile(str(file)):
                            shutil.move(str(file),'output/ '+str(file).split("\ ".rstrip(" "))[-1])
                        
                        copies += 1
                        copies_list.append((str(nameGroup[0])+"  |  "+str(nameGroup[1]), str(pixelmap)+"  |  "+str(file)))
                        copies_index.append((nameGroup[1],(file_index-1, file_index)))
                        break

                #if file_index < 15 or file_index > totalFiles-16:
                #    Duplicate.saveThumbnail(image) #Make check if thumbs folder exists

                image.close()
            else:
                for fileGroup in copies_index:
                    if file == fileGroup[0]:
                        break
                    elif fileGroup[0] == copies_index[-1][0]:
                        print("\n\nERROR!: File Not Found!\n\n")
                        errors += 1
                        errors_list.append(("ERROR!: This File Was Not Found!", str(file)))
                        time.sleep(2)
             
            end = time.time()
            Console.clear()
            print("Current File: "+str(file).split("\ ".rstrip(" "))[-1])
            Console.progressBar(total_files, file_index, str(file_index)+"/"+str(total_files), Console.ETA(0, 0, total_files, file_index)+"\n")
            print("Copies found: "+ str(copies))
            print("Errors found: "+ str(errors))
            
        for groups in copies_list:
            print("\nThere's a copy of this image!")
            print("Original")
            print(str(groups[0]))
            print("Copy")
            print(str(groups[1]))
        for groups in errors_list:
            print("\nThere was an error with this file!")
            print(str(groups[0])+"\t"+str(groups[1]))
        
        return print("\nDone!\n")
    
    def build(route, max_files = 15):
        total_files = len(route)
        name_list = list()
        file_index = 0
        Console.ETA(time.localtime(time.time())[5],0,0,0,True)
        
        if os.path.isfile("database/nameList.db"):
            with open("database/nameList.db", "rb") as database:
                name_list = pickle.load(database)

        if not os.path.isdir("database"):
            os.mkdir("database")

        for file in route:
            start = time.time()
            file_index += 1
            if os.path.isfile(str(file)):
                image = Image.open(file)
                image = image.convert('RGBA')

                pixelmap = Duplicate.generatePixelmap(image)

                name_list.append((str(pixelmap), str(file)))
            
            Console.clear()
            print("Building files list...")
            end = time.time()
            Console.progressBar(total_files, file_index, str(file_index)+"/"+str(total_files), str(Console.ETA(start,end,total_files, file_index)))

            if file_index > max_files-1:
                break

        with open("namelist.db",'wb') as database:
            pickle.dump(nameList, database)
        Console.clear()
        time.sleep(5)
        return print("\n\nDatabase build!\n\n")

    def generatePixelmap(image):
        pixelmap = ""
        image = image.resize((int(image.size[0]/(image.size[0]/3)), 
                              int(image.size[1]/(image.size[0]/4))), 
                              Image.NEAREST)
            
        pixel_values= list(image.getdata())
        for channel in pixel_values:
            total = 0
            for value in channel:
                total += value
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
