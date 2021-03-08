from PIL import Image
import shutil, os

class Name(object):
    """Generates unique filename based on pixel color"""

    def generate(route):
        total = 0
        for file in route:
            total += 1

        fileindex = 0
        namelist = list()
        for file in route:
            fileindex += 1
            print(file)
            image1 = Image.open(file)
            image2 = image1.resize((int(image1.size[0]/(image1.size[0]/3)), int(image1.size[1]/(image1.size[0]/4))), Image.NEAREST)
            
            list1 = list(image2.getdata())
            name = ""
            for group in list1:
                added = 0
                for item in group:
                    added += item
                name = name+str(hex(added).lstrip("0x").rstrip("L"))
            
            for namegroup in namelist:
                if name == namegroup[0]:
                    print("There's a copy of this image!")
                    print(str(namegroup[0])+"\t"+str(namegroup[1]))
                    print(str(name)+"\t"+str(file.lstrip("input/")))

                    image1.save('output/duplicates/'+str(fileindex)+'-'+str(name)+'.png')
                    image1 = Image.open("input/"+str(namegroup[1]))
                    image1.save('output/duplicates/'+str(fileindex-1)+'-'+str(name)+'.png')

                    input("\nPress enter to continue the script...\n\n")
            namelist.append((name, file.lstrip("input/")))

            image2.save('output/thumbnails/'+str(name)+'.png')
            image2.close()
            image1.close()
            
            print(str(fileindex)+"/"+str(total)+"\n")