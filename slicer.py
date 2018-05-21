import nibabel
import os
import numpy as np
import time

oldTime = time.time()
j = 1
for f in os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder3\\"):
    print(j)
    img = nibabel.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder3\\" + f)
    data = img.get_data()
    for i in range(155):
##        print(i)
        slicee = data[:, :, i]
##        newFile = open("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + str(i) + f, "w")
##        newFile.write(slicee)
        np.save("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + str(i) + f, slicee)
    j += 1
##        newFile.close()
##    os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder3\\" + f)
print(time.time() - oldTime)
