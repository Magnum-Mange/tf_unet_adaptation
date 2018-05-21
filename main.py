from tf_unet import unet, util, image_util
import os
import random
import numpy as np

#preparing data loading
data_provider = image_util.ImageDataProvider("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\train\\*", data_suffix = "t1ce.nii", mask_suffix = "seg.nii")

#setup & training
output_path = "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\unet_trained\\"
net = unet.Unet(layers=3, features_root=64, channels=1, n_class=2, cost = "dice_coefficient")
trainer = unet.Trainer(net)
path = trainer.train(data_provider, output_path, training_iters=5, epochs=2)

#verification
...

##counter = 0
##filelist = os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\")
##random.shuffle(filelist)
##testdata = np.empty((1, 240, 240, 1))
##testlabels = np.empty((1, 240, 240, 1))
##
##for f in filelist:
##    if counter == 1:
##        break
##    if f[-11:-7] == "t1ce":
##        testdata[counter] = np.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f)
##        try:
##            s = "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\Folder4\\" + f
##            s.replace("t1ce", "seg")
##            testlabels[counter] = np.load(s)
##        except FileNotFoundError:
##            testlabels[counter] = np.zeros((240, 240, 1))
##        counter += 1
##        print(counter)

##testdata = np.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\31Brats17_TCIA_471_1_t1ce.nii.npy")
##testlabels = np.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\31Brats17_TCIA_471_1_seg.nii.npy")
testdata = np.zeros((240, 240));
testlabels = np.zeros((240, 240));
t1ce_images = [img for img in os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\") if "t1ce" in img]
numTestImg = len(t1ce_images)
print(np.shape(testdata), "WOOOO")
print(np.shape(testlabels))
testdata = np.zeros((numTestImg, 240, 240))
##testdata = np.expand_dims(testdata, 0)
##testdata[0] = numTestImg
testlabels = np.zeros((numTestImg, 240, 240))
##testlabels = np.expand_dims(testlabels, 0)
##testlabels[0] = numTestImg
counter + 
for f in os.listdir("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\"):
    if f[-11:-7] == "t1ce":
        testdata[counter] = np.load("C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f)
        try:
            s = "C:\\Users\\Magnus\\Documents\\GitHub\\DD2424\\tf_unet\\test\\" + f
            s.replace("t1ce", "seg")
            testlabels[counter] = np.load(s)
        except FileNotFoundError:
            testlabels[counter] = np.zeros((240, 240))

testdata = np.expand_dims(testdata, 3)
print(np.shape(testdata))
testlabels = np.expand_dims(testlabels, 3)
    
prediction = net.predict(path, testdata)

print("Error_rate: ", unet.error_rate(prediction, util.crop_to_shape(testlabels, prediction.shape)))

img = util.combine_img_prediction(np.expand_dims(testdata[5000], axis = 0), np.expand_dims(testlabels[5000], axis = 0), np.expand_dims(prediction[5000], axis = 0))
util.save_image(img, "prediction.jpg")
