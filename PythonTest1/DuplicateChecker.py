from PIL import Image
import shutil, os, pickle

class Duplicate(object):
    """stuff stuff"""

    def check(route):
        total = 0
        for file in route:
            total += 1

        if not os.path.isfile("nameList.db"):
            Duplicate.build(route, 50)

        with open("nameList.db", "rb") as database:
            nameList = pickle.load(database)

        fileIndex = 0
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
                    if name == nameGroup[0] and file != nameGroup[1]:
                        print("There's a copy of this image!")  
                        print(str(nameGroup[0])+"\t"+str(nameGroup[1]))
                        print(str(name)+"\t"+str(file))
                        
                        if os.path.isfile(str(nameGroup[1])):
                            shutil.move(str(nameGroup[1]),"output/ " +str(nameGroup[1]).split(str("\ ").rstrip(" "))[-1])
                        if os.path.isfile(str(file)):
                            shutil.move(str(file),'output/ '+str(file).split(str("\ ").rstrip(" "))[-1])

                        #input("\nPress enter to continue the script...\n\n")
                nameList.append((name, file))
                #image2.save('output/thumbnails/'+str(name)+'.png')
                image2.close()
                image1.close()
            
                print(str(fileIndex)+"/"+str(total)+"\n")
                #test("\nPress enter to continue the script...\n\n")
            else:
                print("\n\nFile Skipped!\n\n")
        return print('\nDone!\n')
    
    def build(route, maxFiles = 15):
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
                nameList.append((name, file.lstrip("input/ ")))
            print(str(fileIndex)+"/"+str(total))

            if fileIndex > maxFiles:
                break

        with open("nameList.db",'wb') as database:
            pickle.dump(nameList, database)
        return print("/n/nDatabase build!/n/n")