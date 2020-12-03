# Image Object Dimension Measurement
1. This allows you to determine the dimension of an object by its picture.
2. You can also get the distance between your camera and the object in the image
3. This might have potential to substitute some expensive sensors in stuff like self-driving vehicles, also has the potential for use in areal surverys and much more!
4. You will need a set-up of 2 cameras (recomended to be placed 5cm apart, one in the front and another in the back). But you can also have the same camera take 2 pictures by just moving it 5cm forward from its original position (You have to be very careful and accurate while doing this and avoid human error, if you want to get some accurate results).

> ## NOTE: For the principle behind the working of this, [refer here](https://surajsjain.ml/img_objdim_doc.html)

# Specific Requirements are needed
This program needs specific requirements to run. So, it is recomended that you use the dockerfile if you want to try it out. </br>
Some of the Specific requirements are:
1. Python version 3.5-3.7 (So, use docker if your PC is running Python 3.8+)
2. Tensorflow version less than 2.0
3. Keras version 2.1.3
4. h5py version 2.10.0

# Installing instructions
1. Github was not allowing me to upload the .h5 model as it was a large file. [So, download the h5 YOLO model from here](https://drive.google.com/file/d/1O97Mrev9BQNx92GqehY_CjeivokK3oOg/view). Feel free to use your own YOLO model.
2. Copy the .h5 model to the directory `Yolo/`.

# Recomended steps for running
1. Copy the pictures that you have taken into the directory named `pics/`.
2. (Recomended in order to avoid inconsistency in requirements) Build and run the docker Image.
3. Enter the distance that you have maintained between the 2 cameras (Or distance between the positions of the same camera while taking the pictures).
4. Enter the file names of the images that you have taken, and make sure that you enter the proper file extension of the images too.
