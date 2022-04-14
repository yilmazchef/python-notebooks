<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>


```
!pip install mediapipe
```


```
from google.colab import files
import cv2
from google.colab.patches import cv2_imshow
import numpy as np

import mediapipe as mp
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils
```

Mediapipe Objectron provides pre-trained models for shoe, chair, cup and camera.

***
#Objectron Shoe Model

Upload any image that that has a person with visible upper body to the Colab. We take two examples image from the web: https://unsplash.com/photos/8dukMg99Hd8 and https://unsplash.com/photos/PqbL_mxmaUE


```
# Upload image files.
uploaded = files.upload()

# Read images with OpenCV.
shoe_images = {name: cv2.imread(name) for name in uploaded.keys()}

# Preview the images.
for name, image in shoe_images.items():
  print(name)   
  cv2_imshow(image)
```



<input type="file" id="files-9b88b4dc-793a-4b0e-8f7f-8f98e7182c37" name="files[]" multiple disabled
   style="border:none" />
<output id="result-9b88b4dc-793a-4b0e-8f7f-8f98e7182c37">
 Upload widget is only available when the cell has been executed in the
 current browser session. Please rerun this cell to enable.
 </output>
 <script src="/nbextensions/google.colab/files.js"></script> 


    Saving aisfaris-jr-8dukMg99Hd8-unsplash.jpg to aisfaris-jr-8dukMg99Hd8-unsplash.jpg
    Saving andres-jasso-PqbL_mxmaUE-unsplash.jpg to andres-jasso-PqbL_mxmaUE-unsplash.jpg
    aisfaris-jr-8dukMg99Hd8-unsplash.jpg
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_4_2.png)
    


    andres-jasso-PqbL_mxmaUE-unsplash.jpg
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_4_4.png)
    



```
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name='Shoe') as objectron:
  # Run inference on shoe images.
  for name, image in shoe_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Objectron.
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw box landmarks.
    if not results.detected_objects:
      print(f'No box landmarks detected on {name}')
      continue
    print(f'Box landmarks of {name}:')
    annotated_image = image.copy()
    for detected_object in results.detected_objects:
      mp_drawing.draw_landmarks(
          annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
      mp_drawing.draw_axis(annotated_image, detected_object.rotation, detected_object.translation)
    cv2_imshow(annotated_image)
```

    Box landmarks of aisfaris-jr-8dukMg99Hd8-unsplash.jpg:
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_5_1.png)
    


    Box landmarks of andres-jasso-PqbL_mxmaUE-unsplash.jpg:
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_5_3.png)
    


***
#Objectron Chair Model

Upload any image that that has chairs to the Colab. We take one example image from the web: https://unsplash.com/photos/7T8vSHYXq4U


```
# Upload image files.
uploaded = files.upload()

# Read images with OpenCV.
chair_images = {name: cv2.imread(name) for name in uploaded.keys()}

# Preview the images.
for name, image in chair_images.items():
  print(name)   
  cv2_imshow(image)
```



<input type="file" id="files-2f805c62-f30d-4fed-9a34-c9341d88c9e5" name="files[]" multiple disabled
   style="border:none" />
<output id="result-2f805c62-f30d-4fed-9a34-c9341d88c9e5">
 Upload widget is only available when the cell has been executed in the
 current browser session. Please rerun this cell to enable.
 </output>
 <script src="/nbextensions/google.colab/files.js"></script> 


    Saving s-o-c-i-a-l-c-u-t-7T8vSHYXq4U-unsplash.jpg to s-o-c-i-a-l-c-u-t-7T8vSHYXq4U-unsplash.jpg
    s-o-c-i-a-l-c-u-t-7T8vSHYXq4U-unsplash.jpg
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_7_2.png)
    



```
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name='Chair') as objectron:
  # Run inference on chair images.
  for name, image in chair_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Objectron.
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw box landmarks.
    if not results.detected_objects:
      print(f'No box landmarks detected on {name}')
      continue
    print(f'Box landmarks of {name}:')
    annotated_image = image.copy()
    for detected_object in results.detected_objects:
      mp_drawing.draw_landmarks(
          annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
      mp_drawing.draw_axis(annotated_image, detected_object.rotation, detected_object.translation)
    cv2_imshow(annotated_image)
```

    Box landmarks of s-o-c-i-a-l-c-u-t-7T8vSHYXq4U-unsplash.jpg:
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_8_1.png)
    


***
#Objectron Cup Model

Upload any image that that has cups to the Colab. We take one example image from the web: https://unsplash.com/photos/WJ7gZ3cilBA


```
# Upload image files.
uploaded = files.upload()

# Read images with OpenCV.
cup_images = {name: cv2.imread(name) for name in uploaded.keys()}

# Preview the images.
for name, image in cup_images.items():
  print(name)   
  cv2_imshow(image)
```



<input type="file" id="files-1fb2f88f-8536-4038-a59a-722a036de579" name="files[]" multiple disabled
   style="border:none" />
<output id="result-1fb2f88f-8536-4038-a59a-722a036de579">
 Upload widget is only available when the cell has been executed in the
 current browser session. Please rerun this cell to enable.
 </output>
 <script src="/nbextensions/google.colab/files.js"></script> 


    Saving vlad-ursache-WJ7gZ3cilBA-unsplash.jpg to vlad-ursache-WJ7gZ3cilBA-unsplash.jpg
    vlad-ursache-WJ7gZ3cilBA-unsplash.jpg
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_10_2.png)
    



```
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name='Cup') as objectron:
  # Run inference on cup images.
  for name, image in cup_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Objectron.
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw box landmarks.
    if not results.detected_objects:
      print(f'No box landmarks detected on {name}')
      continue
    print(f'Box landmarks of {name}:')
    annotated_image = image.copy()
    for detected_object in results.detected_objects:
      mp_drawing.draw_landmarks(
          annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
      mp_drawing.draw_axis(annotated_image, detected_object.rotation, detected_object.translation)
    cv2_imshow(annotated_image)
```

    Box landmarks of vlad-ursache-WJ7gZ3cilBA-unsplash.jpg:
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_11_1.png)
    


***
#Objectron Camera Model

Upload any image that that has cups to the Colab. We take one example image from the web: https://unsplash.com/photos/XzL8YAWdirE


```
# Upload image files.
uploaded = files.upload()

# Read images with OpenCV.
camera_images = {name: cv2.imread(name) for name in uploaded.keys()}

# Preview the images.
for name, image in camera_images.items():
  print(name)   
  cv2_imshow(image)
```



<input type="file" id="files-a602bfba-d3e3-4d5a-b5e3-47c5c789eec9" name="files[]" multiple disabled
   style="border:none" />
<output id="result-a602bfba-d3e3-4d5a-b5e3-47c5c789eec9">
 Upload widget is only available when the cell has been executed in the
 current browser session. Please rerun this cell to enable.
 </output>
 <script src="/nbextensions/google.colab/files.js"></script> 


    Saving hanson-lu-XzL8YAWdirE-unsplash.jpg to hanson-lu-XzL8YAWdirE-unsplash.jpg
    hanson-lu-XzL8YAWdirE-unsplash.jpg
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_13_2.png)
    



```
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name='Camera') as objectron:
  # Run inference on camera images.
  for name, image in camera_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Objectron.
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw box landmarks.
    if not results.detected_objects:
      print(f'No box landmarks detected on {name}')
      continue
    print(f'Box landmarks of {name}:')
    annotated_image = image.copy()
    for detected_object in results.detected_objects:
      mp_drawing.draw_landmarks(
          annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
      mp_drawing.draw_axis(annotated_image, detected_object.rotation, detected_object.translation)
    cv2_imshow(annotated_image)
```

    Box landmarks of hanson-lu-XzL8YAWdirE-unsplash.jpg:
    


    
![png](05-%20Mediapipe%20objectron_files/05-%20Mediapipe%20objectron_14_1.png)
    

