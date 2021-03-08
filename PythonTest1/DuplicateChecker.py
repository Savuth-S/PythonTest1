from PIL import Image
import shutil, os, pickle

class Duplicate(object):
    """stuff stuff"""

    def check(route):
        total = 0
        for file in route:
            total += 1

        if not os.path.isfile("nameList.db"):
            Duplicate.build(route)

        with open("nameList.db", "rb") as database:
            nameList = pickle.load(database)

        fileIndex = 0
        duplicateDictionary = {}
        for file in route:
            fileIndex += 1
            print(file)
            if os.path.isfile(str(file)):
                image1 = Image.open(file)
                image1 = image1.convert('RGBA')
                image2 = image1.resize((int(image1.size[0]/(image1.size[0]/3)), int(image1.size[1]/(image1.size[0]/4))), Image.NEAREST)
            
                list1 = list(image2.getdata())
                name = ""
                for group in list1:
                    added = 0
                    for item in group:
                        added += item
                    name = name+str(hex(added).lstrip("0x").rstrip("L"))

                for nameGroup in nameList:
                    if name == nameGroup[0] and file.lstrip("input\ ") != nameGroup[1]:
                        print("There's a copy of this image!")
                        print(str(nameGroup[0])+"\t"+str(nameGroup[1]))
                        print(str(name)+"\t"+str(file.lstrip("input\ ")))

                        tempIndex = 0
                        for index in duplicateDictionary[name]:
                            tempIndex = index
                        tempIndex+=1
                        
                        if os.path.isfile("input/"+str(nameGroup[1])):
                            shutil.move("input/"+str(nameGroup[1]),"output/duplicates/"+str(duplicateDictionary[name][0])+'_'+str(nameGroup[1]))
                        if os.path.isfile(str(file)):
                            shutil.move(str(file),'output/duplicates/'+str(tempIndex)+'_'+str(file.lstrip("input\ ")))

                        #input("\nPress enter to continue the script...\n\n")
                    else:
                        duplicateDictionary[name].append(fileIndex)
                #image2.save('output/thumbnails/'+str(name)+'.png')
                image2.close()
                image1.close()
            
                print(str(fileIndex)+"/"+str(total)+"\n")
                #input("\nPress enter to continue the script...\n\n")
            else:
                print("\n\nFile Skipped!\n\n")
        return print('\nDone!\n')
    
    def build(route):
        total = 0
        for file in route:
            total += 1

        nameList = list((" ", " "))
        fileIndex = 0
        for file in route:
            #print(file)
            fileIndex += 1
            if os.path.isfile(str(file)):
                image1 = Image.open(file)
                image1 = image1.convert('RGBA')
                image2 = image1.resize((int(image1.size[0]/(image1.size[0]/3)), int(image1.size[1]/(image1.size[0]/4))), Image.NEAREST)
            
                list1 = list(image2.getdata())
                image1.close()
                image2.close()
                name = ""
                for group in list1:
                    added = 0
                    for item in group:
                        added += item
                    name = name+str(hex(added).lstrip("0x").rstrip("L"))

                for nameGroup in nameList:
                    if name == nameGroup[0]:
                        None
                    else:
                        nameList.append((name, file.lstrip("input\ ")))

        with open("nameList.db",'wb') as database:
            pickle.dump(nameList, database)
        print(str(fileIndex)+"/"+str(total))

        return print("\n\nDatabase build!\n\n")