---
created: 2022-03-07T11:45:10 (UTC +01:00)
tags: []
source: https://www.computervision.zone/lessons/face-attendance-video-lesson/
author: 
---

# Face Attendance - Video Lesson - Computer Vision Zone

> ## Excerpt
> Face Attendance – Video Lesson Complete In this project we are going to learn how to perform Facial recognition with high accuracy. We will first briefly go through the theory and learn the basic implementation. Then we will create an Attendance project that will use webcam to detect faces and record the attendance […]

---
<iframe loading="lazy" title="FACE RECOGNITION  + ATTENDANCE PROJECT | OpenCV Python | Computer Vision" src="https://www.youtube.com/embed/sz25xxF_AVE?feature=oembed" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" width="800" height="450" frameborder="0"></iframe>

In this project we are going to learn how to perform Facial recognition with high accuracy. We will first briefly go through the theory and learn the basic implementation. Then we will create an Attendance project that will use webcam to detect faces and record the attendance live in an excel sheet.

## Installations

The installation process for this project is a bit more than usual. First we have to download a C++ compiler. We can do this by installing Visual Studios. You can download the community version for free from their [website][1]. Once the intaller we will run it and select the ‘Desktop development with C++’. The download and installation will take some time as it is a few Gbs.

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/visualStudio-950x480.jpg)

After completing and restarting the computer, now we will head on to our Pycharm project. Here we will install the required packages. Below is the list.

-   cmake
-   dlib
-   face\_recognition
-   numpy
-   opencv-python

## Understanding the problem

Although many face recognition algorithms have been developed over the years, their speed and accuracy balance has not been quiet optimal . But some recent advancements have shown promise. A good example is Facebook, where they are able to tag you and your friends with just a few images of training and with accuracy as high as 98%. So how does this work . Today we will try to replicate similar results using a face recognition library developed by Adam Geitgey. Lets look at the 4 problems he explained in his [article][2].

Face recognition is a series of several problems:

1.  First, look at a picture and find all the faces in it
2.  Second, focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.
3.  Third, be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.
4.  Finally, compare the unique features of that face to all the people you already know to determine the person’s name.

## Face Recognition

### Importing

First we will import the relevant libraries

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>import</span><span> </span><span>face_recognition</span></p><p><span>import</span><span> </span><span>cv2</span></p><p><span>import</span><span> </span><span>numpy </span><span>as</span><span> </span><span>np</span></p></div></td></tr></tbody></table>

The Process of Recognition can be divided into 3 steps.

### Step 1

#### Loading Images and Converting to RGB.

The Face Recognition package consists of a load image function that loads the image. Once imported the image has to be converted to RGB.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>imgElon</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>load_image_file</span><span>(</span><span>'ImagesBasic/Elon Musk.jpg'</span><span>)</span></p><p><span>imgElon</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>cvtColor</span><span>(</span><span>imgElon</span><span>,</span><span>cv2</span><span>.</span><span>COLOR_BGR2RGB</span><span>)</span></p><p><span>imgTest</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>load_image_file</span><span>(</span><span>'ImagesBasic/Elon Test.jpg'</span><span>)</span></p><p><span>imgTest</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>cvtColor</span><span>(</span><span>imgTest</span><span>,</span><span>cv2</span><span>.</span><span>COLOR_BGR2RGB</span><span>)</span></p></div></td></tr></tbody></table>

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/Elon-Musk.jpg)

Elon Musk

### Step 2

#### Find Faces Locations and Encodings

In the second step we will use the true functionality of the face recognition library. First we will find the faces in our images . This is done using HOG (Histogram of Oriented Gradients) at the backend. Once we have the face they are warped to remove unwanted rotations. Then the image is feed to a pretrained neural network that out puts 128 measurements that are unique to that particular face. The parts that the model measures is not known as this is what the model learns by itself when it was trained. Lucky for us all this is done is just 2 lines of code. Once we have the face locations and the encodings we can draw rectangles around our faces.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>faceLoc</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_locations</span><span>(</span><span>imgElon</span><span>)</span><span>&amp;</span><span>#91;0]</span></p><p><span>encodeElon</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_encodings</span><span>(</span><span>imgElon</span><span>)</span><span>&amp;</span><span>#91;0]</span></p><p><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>imgElon</span><span>,</span><span>(</span><span>faceLoc</span><span>&amp;</span><span>#91;3],faceLoc&amp;#91;0]),(faceLoc&amp;#91;1],faceLoc&amp;#91;2]),(255,0,255),2) # top, right, bottom, left</span></p><p><span>faceLocTest</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_locations</span><span>(</span><span>imgTest</span><span>)</span><span>&amp;</span><span>#91;0]</span></p><p><span>encodeTest</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_encodings</span><span>(</span><span>imgTest</span><span>)</span><span>&amp;</span><span>#91;0]</span></p><p><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>imgTest</span><span>,</span><span>(</span><span>faceLocTest</span><span>&amp;</span><span>#91;3],faceLocTest&amp;#91;0]),(faceLocTest&amp;#91;1],faceLocTest&amp;#91;2]),(255,0,255),2)</span></p></div></td></tr></tbody></table>

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/Elon1.jpg)

### Step 3

#### Compare Faces and Find Distance

Once we have the encodings for both faces, then we can compare these 128 measurements of these two faces to find similarities. To compare the package uses one of the most common machine Learning methods linear SVM classifier. We can use the compare\_faces function to find if the faces match. This function returns True or False. Similarly we can use the face\_distance function to find how likely is the faces match in terms of numbers. This is helpul particularly when there are multiple faces to detect from.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>results</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>compare_faces</span><span>(</span><span>&amp;</span><span>#91;encodeElon], encodeTest)</span></p><p><span>faceDis</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_distance</span><span>(</span><span>&amp;</span><span>#91;encodeElon], encodeTest)</span></p><p><span>cv2</span><span>.</span><span>putText</span><span>(</span><span>imgTest</span><span>,</span><span>f</span><span>'{results} {round(faceDis&amp;#91;0],2)} '</span><span>,</span><span>(</span><span>50</span><span>,</span><span>50</span><span>)</span><span>,</span><span>cv2</span><span>.</span><span>FONT_HERSHEY_COMPLEX</span><span>,</span><span>1</span><span>,</span><span>(</span><span>255</span><span>,</span><span>0</span><span>,</span><span>255</span><span>)</span><span>,</span><span>3</span><span>)</span></p></div></td></tr></tbody></table>

If we run this with the test image we get the value True, indicating that the face found is of Elon Musk. The is distance between the faces is 0.44. The lower the distance the better the match.

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/Elon2-1.jpg)

Let try it with another testing image. This time we will test it with an image of Bill Gates. As we can see the result is False and the distance is much higher than before indicating a bad match.

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/Elon2-2.jpg)

## Attendance Project

Now using the methods we have seen above, we will develop an attendance system where the user is automatically logged when they are detected in the camera. We will store the name along with the time when they appeared.

### Importing Images

As we have imported before we can use the same face\_recognition.load\_image\_file() function to import our images. But when we have multiple images, importing them individually can become messy. Therefore we will write a script to import all images in a given folder at once. For this we will need the os library so we will import that first. We will store all the images in one list and their names in another.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>import</span><span> </span><span>face_recognition</span></p><p><span>import</span><span> </span><span>cv2</span></p><p><span>import</span><span> </span><span>numpy </span><span>as</span><span> </span><span>np</span></p><p><span>import</span><span> </span><span>os</span></p></div></td></tr></tbody></table>

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>path</span><span> </span><span>=</span><span> </span><span>'ImagesAttendance'</span></p><p><span>images</span><span> </span><span>=</span><span> </span><span>&amp;</span><span>#91;]&nbsp;&nbsp;&nbsp;&nbsp; # LIST CONTAINING ALL THE IMAGES</span></p><p><span>className</span><span> </span><span>=</span><span> </span><span>&amp;</span><span>#91;]&nbsp;&nbsp;&nbsp;&nbsp;# LIST CONTAINING ALL THE CORRESPONDING CLASS Names</span></p><p><span>myList</span><span> </span><span>=</span><span> </span><span>os</span><span>.</span><span>listdir</span><span>(</span><span>path</span><span>)</span></p><p><span>print</span><span>(</span><span>"Total Classes Detected:"</span><span>,</span><span>len</span><span>(</span><span>myList</span><span>)</span><span>)</span></p><p><span>for</span><span> </span><span>x</span><span>,</span><span>cl </span><span>in</span><span> </span><span>enumerate</span><span>(</span><span>myList</span><span>)</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>curImg</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>imread</span><span>(</span><span>f</span><span>'{path}/{cl}'</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>images</span><span>.</span><span>append</span><span>(</span><span>curImg</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>className</span><span>.</span><span>append</span><span>(</span><span>os.path</span><span>.</span><span>splitext</span><span>(</span><span>cl</span><span>)</span><span>&amp;</span><span>#91;0])</span></p></div></td></tr></tbody></table>

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/Elon-Musk-660x480.jpg)

### Compute Encodings

Now that we have a list of images we can iterate through those and create a corresponding encoded list for known faces. To do this we will create a function. As earlier we will first convert it into RGB and then find its encoding using the face\_encodings() function. Then we will append each encoding to our list.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>def</span><span> </span><span>findEncodings</span><span>(</span><span>images</span><span>)</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>encodeList</span><span> </span><span>=</span><span> </span><span>&amp;</span><span>#91;]</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>for</span><span> </span><span>img </span><span>in</span><span> </span><span>images</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>img</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>cvtColor</span><span>(</span><span>img</span><span>,</span><span> </span><span>cv2</span><span>.</span><span>COLOR_BGR2RGB</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>encode</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_encodings</span><span>(</span><span>img</span><span>)</span><span>&amp;</span><span>#91;0]</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>encodeList</span><span>.</span><span>append</span><span>(</span><span>encode</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>return</span><span> </span><span>encodeList</span></p></div></td></tr></tbody></table>

Now we can simply call this function with the images list as the input arguments.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>encodeListKnown</span><span> </span><span>=</span><span> </span><span>findEncodings</span><span>(</span><span>images</span><span>)</span></p><p><span>print</span><span>(</span><span>'Encodings Complete'</span><span>)</span></p></div></td></tr></tbody></table>

### The While loop

The while loop is created to run the webcam. But before the while loop we have to create a video capture object so that we can grab frames from the webcam.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>cap</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>VideoCapture</span><span>(</span><span>0</span><span>)</span></p></div></td></tr></tbody></table>

#### Webcam Image

First we will read the image from the webcam and then resize it to quarter the size. This is done to increase the speed of the system. Even though the image being used is 1/4 th of the original, we will still use the original size while displaying. Next we will convert it to RGB.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>while</span><span> </span><span>True</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>success</span><span>,</span><span> </span><span>img</span><span> </span><span>=</span><span> </span><span>cap</span><span>.</span><span>read</span><span>(</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>imgS</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>resize</span><span>(</span><span>img</span><span>,</span><span> </span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>)</span><span>,</span><span> </span><span>fx</span><span>=</span><span>0.25</span><span>,</span><span> </span><span>fy</span><span>=</span><span>0.25</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>imgS</span><span> </span><span>=</span><span> </span><span>cv2</span><span>.</span><span>cvtColor</span><span>(</span><span>imgS</span><span>,</span><span> </span><span>cv2</span><span>.</span><span>COLOR_BGR2RGB</span><span>)</span></p></div></td></tr></tbody></table>

#### Webcam Encodings

Once we have the webcam frame we will find all the faces in our image. The face\_locations function is used for this purpose. Later we will find the face\_encodings as well.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>facesCurFrame</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_locations</span><span>(</span><span>imgS</span><span>)</span></p><p><span>encodesCurFrame</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_encodings</span><span>(</span><span>imgS</span><span>,</span><span> </span><span>facesCurFrame</span><span>)</span></p></div></td></tr></tbody></table>

#### Find Matches

Now we can match the current face encodings to our known faces encoding list to find the matches. We will also compute the distance. This is done to find the best match in case more than one face is detected at a time.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>for</span><span> </span><span>encodeFace</span><span>,</span><span>faceLoc </span><span>in</span><span> </span><span>zip</span><span>(</span><span>encodesCurFrame</span><span>,</span><span>facesCurFrame</span><span>)</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>matches</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>compare_faces</span><span>(</span><span>encodeListKnown</span><span>,</span><span> </span><span>encodeFace</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>faceDis</span><span> </span><span>=</span><span> </span><span>face_recognition</span><span>.</span><span>face_distance</span><span>(</span><span>encodeListKnown</span><span>,</span><span> </span><span>encodeFace</span><span>)</span></p></div></td></tr></tbody></table>

Once we have the list of face distances we can find the minimum one, as this would be the best match.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>matchIndex</span><span> </span><span>=</span><span> </span><span>np</span><span>.</span><span>argmin</span><span>(</span><span>faceDis</span><span>)</span></p></div></td></tr></tbody></table>

Now based on the index value we can determine the name of the person and display it on the original Image.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>if</span><span> </span><span>matches</span><span>&amp;</span><span>#91;matchIndex]:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>name</span><span> </span><span>=</span><span> </span><span>className</span><span>&amp;</span><span>#91;matchIndex].upper()</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>y1</span><span>,</span><span>x2</span><span>,</span><span>y2</span><span>,</span><span>x1</span><span>=</span><span>faceLoc</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>y1</span><span>,</span><span> </span><span>x2</span><span>,</span><span> </span><span>y2</span><span>,</span><span> </span><span>x1</span><span> </span><span>=</span><span> </span><span>y1</span><span>*</span><span>4</span><span>,</span><span>x2</span><span>*</span><span>4</span><span>,</span><span>y2</span><span>*</span><span>4</span><span>,</span><span>x1</span><span>*</span><span>4</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span> </span><span>(</span><span>x1</span><span>,</span><span> </span><span>y1</span><span>)</span><span>,</span><span> </span><span>(</span><span>x2</span><span>,</span><span> </span><span>y2</span><span>)</span><span>,</span><span> </span><span>(</span><span>0</span><span>,</span><span> </span><span>255</span><span>,</span><span> </span><span>0</span><span>)</span><span>,</span><span> </span><span>2</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span> </span><span>(</span><span>x1</span><span>,</span><span> </span><span>y2</span><span> </span><span>-</span><span> </span><span>35</span><span>)</span><span>,</span><span> </span><span>(</span><span>x2</span><span>,</span><span> </span><span>y2</span><span>)</span><span>,</span><span> </span><span>(</span><span>0</span><span>,</span><span> </span><span>255</span><span>,</span><span> </span><span>0</span><span>)</span><span>,</span><span> </span><span>cv2</span><span>.</span><span>FILLED</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>putText</span><span>(</span><span>img</span><span>,</span><span> </span><span>name</span><span>,</span><span> </span><span>(</span><span>x1</span><span> </span><span>+</span><span> </span><span>6</span><span>,</span><span> </span><span>y2</span><span> </span><span>-</span><span> </span><span>6</span><span>)</span><span>,</span><span> </span><span>cv2</span><span>.</span><span>FONT_HERSHEY_DUPLEX</span><span>,</span><span> </span><span>1.0</span><span>,</span><span> </span><span>(</span><span>255</span><span>,</span><span> </span><span>255</span><span>,</span><span> </span><span>255</span><span>)</span><span>,</span><span> </span><span>1</span><span>)</span></p></div></td></tr></tbody></table>

#### Marking Attendance

Lastly we are going to add the automated attendance code. We will start by writing a function that requires only one input which is the name of the user. First we open our Attendance file which is in csv format. Then we read all the lines and iterate through each line using a for loop. Next we can split using comma ‘,’. This will allow us to get the first element which is the name of the user. If the user in the camera already has an entry in the file then nothing will happen. On the other hand if the user is new then the name of the user along with the current time stamp will be stored. We can use the datetime class in the date time package to get the current time.

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>def</span><span> </span><span>markAttendance</span><span>(</span><span>name</span><span>)</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>with</span><span> </span><span>open</span><span>(</span><span>'Attendance.csv'</span><span>,</span><span>'r+'</span><span>)</span><span> </span><span>as</span><span> </span><span>f</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>myDataList</span><span> </span><span>=</span><span> </span><span>f</span><span>.</span><span>readlines</span><span>(</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>nameList</span><span> </span><span>=&amp;</span><span>#91;]</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>for</span><span> </span><span>line </span><span>in</span><span> </span><span>myDataList</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>entry</span><span> </span><span>=</span><span> </span><span>line</span><span>.</span><span>split</span><span>(</span><span>','</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>nameList</span><span>.</span><span>append</span><span>(</span><span>entry</span><span>&amp;</span><span>#91;0])</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>if</span><span> </span><span>name </span><span>not</span><span> </span><span>in</span><span>&nbsp;&nbsp;</span><span>line</span><span>:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>now</span><span> </span><span>=</span><span> </span><span>datetime</span><span>.</span><span>now</span><span>(</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>dt_string</span><span> </span><span>=</span><span> </span><span>now</span><span>.</span><span>strftime</span><span>(</span><span>"%H:%M:%S"</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span>f</span><span>.</span><span>writelines</span><span>(</span><span>f</span><span>'n{name},{dt_string}'</span><span>)</span></p></div></td></tr></tbody></table>

![](https://www.murtazahassan.com/wp-content/uploads/2020/05/List.png)

Comma Separated Values Storied in Attendance File

## Labeling Unknown faces as well

To find the unknown faces we will replace

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>if</span><span> </span><span>matches</span><span>&amp;</span><span>#91;matchIndex]:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>name</span><span> </span><span>=</span><span> </span><span>classNames</span><span>&amp;</span><span>#91;matchIndex].upper()</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>#print(name)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>y1</span><span>,</span><span>x2</span><span>,</span><span>y2</span><span>,</span><span>x1</span><span> </span><span>=</span><span> </span><span>faceLoc</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>y1</span><span>,</span><span> </span><span>x2</span><span>,</span><span> </span><span>y2</span><span>,</span><span> </span><span>x1</span><span> </span><span>=</span><span> </span><span>y1</span><span>*</span><span>4</span><span>,</span><span>x2</span><span>*</span><span>4</span><span>,</span><span>y2</span><span>*</span><span>4</span><span>,</span><span>x1</span><span>*</span><span>4</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span>(</span><span>x1</span><span>,</span><span>y1</span><span>)</span><span>,</span><span>(</span><span>x2</span><span>,</span><span>y2</span><span>)</span><span>,</span><span>(</span><span>0</span><span>,</span><span>255</span><span>,</span><span>0</span><span>)</span><span>,</span><span>2</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span>(</span><span>x1</span><span>,</span><span>y2</span><span>-</span><span>35</span><span>)</span><span>,</span><span>(</span><span>x2</span><span>,</span><span>y2</span><span>)</span><span>,</span><span>(</span><span>0</span><span>,</span><span>255</span><span>,</span><span>0</span><span>)</span><span>,</span><span>cv2</span><span>.</span><span>FILLED</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>cv2</span><span>.</span><span>putText</span><span>(</span><span>img</span><span>,</span><span>name</span><span>,</span><span>(</span><span>x1</span><span>+</span><span>6</span><span>,</span><span>y2</span><span>-</span><span>6</span><span>)</span><span>,</span><span>cv2</span><span>.</span><span>FONT_HERSHEY_COMPLEX</span><span>,</span><span>1</span><span>,</span><span>(</span><span>255</span><span>,</span><span>255</span><span>,</span><span>255</span><span>)</span><span>,</span><span>2</span><span>)</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>markAttendance</span><span>(</span><span>name</span><span>)</span></p></div></td></tr></tbody></table>

with this

<table><tbody><tr><td data-settings="show"></td><td><div><p><span>if</span><span> </span><span>faceDis</span><span>&amp;</span><span>#91;matchIndex]&amp;lt; 0.50:</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>name</span><span> </span><span>=</span><span> </span><span>classNames</span><span>&amp;</span><span>#91;matchIndex].upper()</span></p><p><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>markAttendance</span><span>(</span><span>name</span><span>)</span></p><p><span>else</span><span>:</span><span> </span><span>name</span><span> </span><span>=</span><span> </span><span>'Unknown'</span></p><p><span>#print(name)</span></p><p><span>y1</span><span>,</span><span>x2</span><span>,</span><span>y2</span><span>,</span><span>x1</span><span> </span><span>=</span><span> </span><span>faceLoc</span></p><p><span>y1</span><span>,</span><span> </span><span>x2</span><span>,</span><span> </span><span>y2</span><span>,</span><span> </span><span>x1</span><span> </span><span>=</span><span> </span><span>y1</span><span>*</span><span>4</span><span>,</span><span>x2</span><span>*</span><span>4</span><span>,</span><span>y2</span><span>*</span><span>4</span><span>,</span><span>x1</span><span>*</span><span>4</span></p><p><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span>(</span><span>x1</span><span>,</span><span>y1</span><span>)</span><span>,</span><span>(</span><span>x2</span><span>,</span><span>y2</span><span>)</span><span>,</span><span>(</span><span>0</span><span>,</span><span>255</span><span>,</span><span>0</span><span>)</span><span>,</span><span>2</span><span>)</span></p><p><span>cv2</span><span>.</span><span>rectangle</span><span>(</span><span>img</span><span>,</span><span>(</span><span>x1</span><span>,</span><span>y2</span><span>-</span><span>35</span><span>)</span><span>,</span><span>(</span><span>x2</span><span>,</span><span>y2</span><span>)</span><span>,</span><span>(</span><span>0</span><span>,</span><span>255</span><span>,</span><span>0</span><span>)</span><span>,</span><span>cv2</span><span>.</span><span>FILLED</span><span>)</span></p><p><span>cv2</span><span>.</span><span>putText</span><span>(</span><span>img</span><span>,</span><span>name</span><span>,</span><span>(</span><span>x1</span><span>+</span><span>6</span><span>,</span><span>y2</span><span>-</span><span>6</span><span>)</span><span>,</span><span>cv2</span><span>.</span><span>FONT_HERSHEY_COMPLEX</span><span>,</span><span>1</span><span>,</span><span>(</span><span>255</span><span>,</span><span>255</span><span>,</span><span>255</span><span>)</span><span>,</span><span>2</span><span>)</span></p></div></td></tr></tbody></table>

All this does is to check if the distance to our min face is less than 0.5 or not. If its not then this means the person is unknown so we change the name to unknown and don’t mark the attendance.

[1]: https://visualstudio.microsoft.com/downloads/
[2]: https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
