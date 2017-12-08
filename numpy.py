import numpy as np
from PIL import Image
 
# gradient between 0 and 1 for 256*256
array = np.linspace(0,1,256*256)
 
# reshape to 2d
mat = np.reshape(array,(256,256))
 
# Creates PIL image
img = Image.fromarray(np.uint8(mat * 255) , 'L')
 
#img.show()  use if you just want to display image
 
img.save("image.png") # use to save
