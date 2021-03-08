from PIL import Image
import shutil, os

class Name(object):
    """Generates unique filename based on pixel color"""

    def generate(route):
        total = 0
        for file in route:
            total += 1

        fileindex = 0
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
            
            if os.path.isfile('output/'+str(name)+'.png'):
                print("There's a copy of this image!")

                shutil.copyfile('output/'+str(name)+'.png','output/duplicate')
                image1.save('output/duplicates/'+str(fileindex)+'-'+str(name)+'.png')

                input("\nPress enter to continue the script...\n\n")
            else:
                image1.save('output/'+str(name)+'.png')
            image2.close()
            image1.close()
            
            print(str(fileindex)+"/"+str(total)+"\n")