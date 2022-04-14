<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

Usage example of MediaPipe Pose Solution API in Python (see also http://solutions.mediapipe.dev/pose).


```
!pip install mediapipe
```

Upload any image that that has a person. We take two example images from the web: https://unsplash.com/photos/v4zceVZ5HK8 and https://unsplash.com/photos/e_rhazQLaSs.



```
from google.colab import files
uploaded = files.upload()
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

# Read images with OpenCV.
images = {name: cv2.imread(name) for name in uploaded.keys()}
# Preview the images.
for name, image in images.items():
  print(name)   
  resize_and_show(image)
```

    david-hofmann-e_rhazQLaSs-unsplash.jpg
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_5_1.png)
    


    thao-le-hoang-v4zceVZ5HK8-unsplash.jpg
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_5_3.png)
    


All MediaPipe Solutions Python API examples are under mp.solutions.

For the MediaPipe Pose solution, we can access this module as `mp_pose = mp.solutions.pose`.

You may change the parameters, such as `static_image_mode` and `min_detection_confidence`, during the initialization. Run `help(mp_pose.Pose)` to get more informations about the parameters.


```
import mediapipe as mp
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles

help(mp_pose.Pose)
```


```
# Run MediaPipe Pose and draw pose landmarks.
with mp_pose.Pose(
    static_image_mode=True, min_detection_confidence=0.5, model_complexity=2) as pose:
  for name, image in images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Pose.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # Print nose landmark.
    image_hight, image_width, _ = image.shape
    if not results.pose_landmarks:
      continue
    print(
      f'Nose coordinates: ('
      f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
      f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_hight})'
    )

    # Draw pose landmarks.
    print(f'Pose landmarks of {name}:')
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    resize_and_show(annotated_image)
```

    Downloading model to /usr/local/lib/python3.7/dist-packages/mediapipe/modules/pose_landmark/pose_landmark_heavy.tflite
    Nose coordinates: (182.0577621459961, 255.44222474098206)
    Pose landmarks of david-hofmann-e_rhazQLaSs-unsplash.jpg:
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_8_1.png)
    


    Nose coordinates: (206.92650318145752, 202.37878853082657)
    Pose landmarks of thao-le-hoang-v4zceVZ5HK8-unsplash.jpg:
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_8_3.png)
    



```
# Run MediaPipe Pose and plot 3d pose world landmarks.
with mp_pose.Pose(
    static_image_mode=True, min_detection_confidence=0.5, model_complexity=2) as pose:
  for name, image in images.items():
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print the real-world 3D coordinates of nose in meters with the origin at
    # the center between hips.
    print('Nose world landmark:'),
    print(results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.NOSE])
    
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
```

    Nose world landmark:
    x: -0.6137464046478271
    y: 0.04928246885538101
    z: -0.4365992546081543
    visibility: 0.9999992847442627
    
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_9_1.png)
    


    Nose world landmark:
    x: -0.04833628237247467
    y: -0.5876999497413635
    z: -0.37148377299308777
    visibility: 0.9999998807907104
    
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_9_3.png)
    



```
# Run MediaPipe Pose with `enable_segmentation=True` to get pose segmentation.
with mp_pose.Pose(
    static_image_mode=True, min_detection_confidence=0.5, 
    model_complexity=2, enable_segmentation=True) as pose:
  for name, image in images.items():
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw pose segmentation.
    print(f'Pose segmentation of {name}:')
    annotated_image = image.copy()
    red_img = np.zeros_like(annotated_image, dtype=np.uint8)
    red_img[:, :] = (255,255,255)
    segm_2class = 0.2 + 0.8 * results.segmentation_mask
    segm_2class = np.repeat(segm_2class[..., np.newaxis], 3, axis=2)
    annotated_image = annotated_image * segm_2class + red_img * (1 - segm_2class)
    resize_and_show(annotated_image)
```

    Pose segmentation of david-hofmann-e_rhazQLaSs-unsplash.jpg:
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_10_1.png)
    


    Pose segmentation of thao-le-hoang-v4zceVZ5HK8-unsplash.jpg:
    


    
![png](06-%20Mediapipe%20pose_files/06-%20Mediapipe%20pose_10_3.png)
    

