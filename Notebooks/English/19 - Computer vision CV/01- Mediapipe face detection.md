<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

Usage example of MediaPipe Face Detection Solution API in Python (see also http://solutions.mediapipe.dev/face_detection).


```
!pip install mediapipe
```

Upload images that contain face(s) within 2 meters from the camera to test the short range model. We take two example images from the web: https://unsplash.com/photos/JyVcAIUAcPM and https://unsplash.com/photos/auTAb39ImXg. 

Also upload images that contain face(s) within 5 meters from the camera to test the full range model. We take two example images from the web: https://unsplash.com/photos/ezgW6z6oIvA and https://unsplash.com/photos/_veZpXKU71c. 


```
# Upload images that contain face(s) within 2 meters from the camera.
from google.colab import files
uploaded_short_range = files.upload()

# Upload images that contain face(s) within 5 meters from the camera.
from google.colab import files
uploaded_full_range = files.upload()
```


```
import cv2
from google.colab.patches import cv2_imshow
import math
import numpy as np

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480
def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  cv2_imshow(img)

# Preview the images.
short_range_images = {name: cv2.imread(name) for name in uploaded_short_range.keys()}
for name, image in short_range_images.items():
  print(name)   
  resize_and_show(image)

full_range_images = {name: cv2.imread(name) for name in uploaded_full_range.keys()}
for name, image in full_range_images.items():
  print(name)   
  resize_and_show(image)
```

    garrett-jackson-auTAb39ImXg-unsplash.jpg
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_5_1.png)
    


    radu-florin-JyVcAIUAcPM-unsplash.jpg
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_5_3.png)
    


    brooke-cagle-ezgW6z6oIvA-unsplash.jpg
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_5_5.png)
    


    tracey-hocking-_veZpXKU71c-unsplash.jpg
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_5_7.png)
    


All MediaPipe Solutions Python API examples are under mp.solutions.

For the MediaPipe Face Mesh solution, we can access this module as mp_face_detection = mp.solutions.face_detection.

You may change the parameter min_detection_confidence during the initialization. Run help(mp_face_detection.FaceDetection) to get more informations about the parameter.


```
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection

help(mp_face_detection.FaceDetection)
```


```
# Prepare DrawingSpec for drawing the face landmarks later.
mp_drawing = mp.solutions.drawing_utils 
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
```


```
# Run MediaPipe Face Detection with short range model.

with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5, model_selection=0) as face_detection:
  for name, image in short_range_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    print(f'Face detections of {name}:')
    if not results.detections:
      continue
    annotated_image = image.copy()
    for detection in results.detections:
      mp_drawing.draw_detection(annotated_image, detection)
    resize_and_show(annotated_image)
```

    Face detections of garrett-jackson-auTAb39ImXg-unsplash.jpg:
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_9_1.png)
    


    Face detections of radu-florin-JyVcAIUAcPM-unsplash.jpg:
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_9_3.png)
    



```
# Run MediaPipe Face Detection with full range model.

with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5, model_selection=1) as face_detection:
  for name, image in full_range_images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    print(f'Face detections of {name}:')
    if not results.detections:
      continue
    annotated_image = image.copy()
    for detection in results.detections:
      mp_drawing.draw_detection(annotated_image, detection)
    resize_and_show(annotated_image)
```

    Face detections of brooke-cagle-ezgW6z6oIvA-unsplash.jpg:
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_10_1.png)
    


    Face detections of tracey-hocking-_veZpXKU71c-unsplash.jpg:
    


    
![png](01-%20Mediapipe%20face%20detection_files/01-%20Mediapipe%20face%20detection_10_3.png)
    

