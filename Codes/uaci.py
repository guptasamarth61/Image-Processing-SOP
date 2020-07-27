from PIL import Image
import math
#TO BE COMPLETED
# Same as NPCR both are used for sensitivity analysis two encrypted image is required

"""
Unified average avereage inensity changed rate
this code calculates average intensity change rate of pixels
"""
def uaci(loc1,loc2):
    image1 = Image.open(loc1)
    image2 = Image.open(loc2)
    pixel1=image1.load()
    pixel2=image2.load()
    width,height=image1.size
    value=0.0
    for y in range(0,height):
        for x in range(0,width):
            value=(abs(pixel1[x,y][0]-pixel2[x,y][0])/255)+value

    value=(value/(width*height))*100
    return value

#print(uaci("encrypted16.png","encrypted116.png"))