import math
import sys
from PIL import Image

filename = str(sys.argv[1])
print(filename)
im = Image.open(filename)
pix = im.load()
print (im.size)

LED_NUM = 44

barray = bytearray(LED_NUM)

byte_str = ""

counter = 0

for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        
        p = pix[y,x]
        if p[3] is 0:
            continue

        print (pix[x,y])
        r = p[0]
        g = p[1]
        b = p[2]

        r_full = r
        g_full = g
        b_full = b

        r /= 32
        g /= 32
        b /= 64

        r = math.floor(r)
        g = math.floor(g)
        b = math.floor(b)

        print(str(r)+","+str(g)+","+str(b))

        byte = r + g*8 + b*64

        '''
        1 2 4 8 16 32 64 128
        r r r g  g  g  b   b
        '''
       
        print("byte: "+str(byte))

        '''

        binary = (chr(byte))

        print("binary: "+str(binary))

        '''

        '''
        if byte < 10:
            byte_str += "00"
        elif byte < 100:
            byte_str += "0"
        '''

        byte_str += str(r_full)+","+str(g_full)+","+str(b_full)        
        #byte_str += str(byte)

        if counter < LED_NUM -1:
            byte_str += ","
        

        counter += 1

print("result: "+str(byte_str))


with open("main.ino", "a") as f:
    text = "uint8_t picture_"+filename+"[] = {"+byte_str+"};"
    f.write(text)
