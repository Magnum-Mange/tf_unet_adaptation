import random
import os
import math
import shutil

filelist = os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\")
random.shuffle(filelist)
cutoff = math.floor(0.2 * len(filelist))
counter = 0
moved = set()
for f in filelist:
    if counter > cutoff:
        break
    if "t1ce" in f:
        shutil.copyfile("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f, "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f)
##        moved.add(
        os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f)
        filelist.remove(f)
        try:
            shutil.copyfile("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f.replace("t1ce", "seg"), "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f.replace("t1ce", "seg"))
            os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f.replace("t1ce", "seg"))
            filelist.remove(f.replace("t1ce", "seg"))
            counter += 1
        except FileNotFoundError:
            continue
    if "seg" in f:
        counter += 1
        shutil.copyfile("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f, "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f)
        os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f)
        filelist.remove(f)
        shutil.copyfile("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f.replace("seg", "t1ce"), "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f.replace("seg", "t1ce"))
        os.remove("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f.replace("seg", "t1ce"))
        filelist.remove(f.replace("seg", "t1ce"))
    counter += 1
