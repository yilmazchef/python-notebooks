Task Description

-   Create an image by yourself Using Python Code.
-   Take 2 images, crop some part of both images and swap them.
-   Take 2 images and combine them to form a single image. For example collage.

First we will be exploring various details about image processing and OpenCV library in python.

## What is Image processing?

Images are multi-dimensional arrays in the computer world. 2D arrays for Black and white images and 3D arrays for RGB.

Colored images are stored in the form of three-dimensional (3D) arrays in the computer, where only 0–255 values are stored furthermore 0 and 255 represent black and white color respectively.

**Image processing** deals with manipulation of digital images through a digital computer. Image processing focuses on developing a computer system that is able to perform processing on an image. The input of that system is a digital image and the system process that image using efficient algorithms, and gives an image as an output.

**Pixel** is the smallest unit of an image. Technically it is an entry inside an array at a particular position of row and column. Each pixel consists of three colors namely, Red, Green, and Blue. Upon combining these different colors are formed. Multiple pixels together form a complete image.

**Video processing** means, performing operations on the video frame by frame. Frames are nothing but just the particular instance of the video i.e. an image in a single point of time. We may have multiple frames even in a single second. Video is nothing but a continuous stream of images. The repeated loop of capturing the image and displaying it gives out a video which can also be processed inside the loop to get a processed video.

Python provides lots of libraries for image processing, including −

-   **OpenCV** − Image processing library mainly focused on real-time computer vision with application in wide-range of areas like 2D and 3D feature toolkits, facial & gesture recognition, Human-computer interaction, Mobile robotics, Object identification and others.
-   **Numpy and Scipy libraries** − For image manipuation and processing.
-   **Sckikit** − Provides lots of alogrithms for image processing.
-   **Python Imaging Library (PIL)** − To perform basic operations on images like create thumnails, resize, rotation, convert between different file formats etc.

## Here we will be using OpenCV module.

-   OpenCV is one of the most popular computer vision libraries. If you want to start your journey in the field of computer vision, then a thorough understanding of the concepts of OpenCV is of paramount importance.
-   **OpenCV** is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. When it is integrated with various libraries, such as `[Numpy](https://www.geeksforgeeks.org/python-numpy/)` which is a highly optimized library for numerical operations, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.
-   The general color code is RGB but the color code format is used in OpenCV is BGR(Blue Green Red).

## Install OpenCV

To install OpenCV on your system, run the following pip command:

```
pip install opencv-python
```

## Rotate an Image

First of all, import the cv2 module.

```
import cv2
```

Now to read the image, use the imread() method of the cv2 module, specify the path to the image in the arguments and store the image in a variable as below:

```
img = cv2.imread("pyimg.jpg")
```

The image is now treated as a matrix with rows and columns values stored in img.

Actually, if you check the type of the img, it will give you the following result:

```
>>>print(type(img))<class 'numpy.ndarray'>
```

It’s a [NumPy array](https://likegeeks.com/numpy-array-tutorial/)! That why image processing using OpenCV is so easy. All the time you are working with a NumPy array.

To display the image, you can use the imshow() method of cv2.

```
cv2.imshow('Original Image', img) cv2.waitKey(0)
```

The waitkey() functions take time as an argument in milliseconds as a delay for the window to close. Here we set the time to zero to show the window forever until we close it manually.

To rotate this image, you need the width and the height of the image because you will use them in the rotation process as you will see later.

```
height, width = img.shape[0:2]
```

The shape attribute returns the height and width of the image matrix. If you print

```
img.shape[0:2]
```

Okay, now we have our image matrix and we want to get the rotation matrix. To get the rotation matrix, we use the _getRotationMatrix2D()_ method of cv2. The syntax of _getRotationMatrix2D()_ is:

```
cv2.getRotationMatrix2D(center, angle, scale)
```

Here the **center** is the center point of rotation, the **angle** is the angle in degrees and **scale** is the scale property which makes the image fit on the screen.

To get the rotation matrix of our image, the code will be:

```
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
```

The next step is to rotate our image with the help of the rotation matrix.

To rotate the image, we have a cv2 method named _wrapAffine_ which takes the original image, the rotation matrix of the image and the width and height of the image as arguments.

```
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
```

The rotated image is stored in the rotatedImage matrix. To show the image, use imshow() as below:

```
cv2.imshow('Rotated Image', rotatedImage)cv2.waitKey(0)
```

## Capturing Image using WebCam:

```
import cv2 cap = cv2.VideoCapture(0) # here, 0 — to access internal webcam & 1 to access external webcam ret , photo = cap.read() # clicks the photoret cv2.imwrite(“my”,photo) # stores in a filecap.release() cv2.imshow(“my”, photo) # displays the photocv2.waitKey() # used to set the expiry time for the picture to be displayedcv2.destroyAllWindows() #used to destroy or close the picture window without crashing it
```

Video Streaming using WebCam:

```
import cv2cap = cv2.VideoCapture(0)ret, photo = cap.read()while True: ret, photo = cap.read() cv2.imshow('hi', photo) if cv2.waitKey(10) ==13:  breakcv.destroyAllwindows()
```

## Convert image to grayscale (Black & White)

The easy way to convert an image in grayscale is to load it like this:

```
img = cv2.imread("pyimg.jpg", 0)
```

There is another method using BGR2GRAY.

To convert a color image into a grayscale image, use the BGR2GRAY attribute of the cv2 module. This is demonstrated in the example below:

Import the cv2 module:

```
import cv2
```

Read the image:

```
img = cv2.imread("pyimg.jpg")
```

Use the cvtColor() method of the cv2 module which takes the original image and the COLOR\_BGR2GRAY attribute as an argument. Store the resultant image in a variable:

```
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

Display the original and grayscale images:

```
cv2.imshow("Original Image", img)cv2.imshow("Gray Scale Image", gray_img)cv2.waitKey(0)
```

## Resize an Image

To resize an image, you can use the resize() method of openCV. In the resize method, you can either specify the values of x and y axis or the number of rows and columns which tells the size of the image.

Import and read the image:

```
import cv2img = cv2.imread("pyimg.jpg")
```

Now using the resize method with axis values:

```
newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75)cv2.imshow('Resized Image', newImg)cv2.waitKey(0)
```

Now using the row and column values to resize the image:

```
newImg = cv2.resize(img, (550, 350))cv2.imshow('Resized Image', newImg)cv2.waitKey(0)
```

We say we want 550 columns (the width) and 350 rows (the height).

## Creating an image using Python code

![](https://miro.medium.com/max/1400/1*S3Sg8EwSpW-AK3bGdWizTQ.png)

The output is as follows:

![](https://miro.medium.com/max/1288/1*-S2tTkDm3M5Il-FeiunGJg.png)

Take 2 images, crop some part of both images and swap them.

![](https://miro.medium.com/max/1400/1*ptLL4KO0dfBfNNH8aeahBQ.png)

The result:

![](https://miro.medium.com/max/948/1*DPrvDZektnlVBtguh4cqzQ.jpeg)

![](https://miro.medium.com/max/1400/1*8pAm7yk52_AC9Mz288PZaA.jpeg)

![](https://miro.medium.com/max/1400/1*-ZIsUdQbKHh2rfj-L5FUlA.png)

Take 2 images and combine them to form a single image. For example collage.

![](https://miro.medium.com/max/1400/1*nEMxB8LFmIAh2Y-GpIW3YA.png)

Output:

![](https://miro.medium.com/max/1400/1*NGqFJGvpVmnBqcyez5rH7A.png)

Horizontal Collage

![](https://miro.medium.com/max/1194/1*xGl8fVNpBeiTP5RbH4kV-A.png)

Vertical Collage

_More content at_ [**_plainenglish.io_**](http://plainenglish.io/)