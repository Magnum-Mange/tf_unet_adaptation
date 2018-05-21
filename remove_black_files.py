import os
import numpy as np
counter = 0
for f in os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\"):
    print(counter)
    img = np.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f)
    if np.amax(img) == 0:
        os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f)
        print(f)
    counter += 1
        
