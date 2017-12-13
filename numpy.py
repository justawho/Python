import numpy as np
from PIL import Image
 
# gradient between 0 and 1 for 256*256
array = np.linspace(0,1,256*256)
 
for i in range(256*256):
    array[i] = array[i] * i / 5.0
 
# reshape to 2d
mat = np.reshape(array,(256,256))
 
# Creates PIL image
uint8Array = np.uint8(mat * 255)  # convert 0-1 float to 0-255 8 bit number (for image input)
img = Image.fromarray(uint8Array , 'L')  # make image
 
#img.show()  use if you just want to display image
 
img.save("image.png") # use to save
