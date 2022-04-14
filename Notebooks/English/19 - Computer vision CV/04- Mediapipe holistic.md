<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

Usage example of MediaPipe Holistic Solution API in Python (see also http://solutions.mediapipe.dev/holistic).


```
!pip install mediapipe
```

Upload any image that that has a person. We take two example images from the web: https://unsplash.com/photos/v4zceVZ5HK8 and https://unsplash.com/photos/e_rhazQLaSs.



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
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_5_1.png)
    


    thao-le-hoang-v4zceVZ5HK8-unsplash.jpg
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_5_3.png)
    


All MediaPipe Solutions Python API examples are under mp.solutions.

For the MediaPipe Pose solution, we can access this module as `mp_holistic = mp.solutions.holistic`.

You may change the parameters, such as `static_image_mode` and `min_detection_confidence`, during the initialization. Run `help(mp_holistic.Holistic)` to get more informations about the parameters.


```
import mediapipe as mp
mp_holistic = mp.solutions.holistic

help(mp_holistic.Holistic)
```


```
# Import drawing_utils and drawing_styles.
mp_drawing = mp.solutions.drawing_utils 
mp_drawing_styles = mp.solutions.drawing_styles
```


```
# Run MediaPipe Holistic and draw pose landmarks.
with mp_holistic.Holistic(
    static_image_mode=True, min_detection_confidence=0.5, model_complexity=2) as holistic:
  for name, image in images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Pose.
    results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print nose coordinates.
    image_hight, image_width, _ = image.shape
    if results.pose_landmarks:
      print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_hight})'
      )

    # Draw pose landmarks.
    print(f'Pose landmarks of {name}:')
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(annotated_image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(
        annotated_image,
        results.face_landmarks,
        mp_holistic.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp_drawing_styles
        .get_default_face_mesh_tesselation_style())
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.
        get_default_pose_landmarks_style())
    resize_and_show(annotated_image)
```

    Downloading model to /usr/local/lib/python3.7/dist-packages/mediapipe/modules/pose_landmark/pose_landmark_heavy.tflite
    Nose coordinates: (183.17447662353516, 254.24443006515503)
    Pose landmarks of david-hofmann-e_rhazQLaSs-unsplash.jpg:
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_9_1.png)
    


    Nose coordinates: (206.55911922454834, 203.0031123161316)
    Pose landmarks of thao-le-hoang-v4zceVZ5HK8-unsplash.jpg:
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_9_3.png)
    



```
# Run MediaPipe Holistic and plot 3d pose world landmarks.
with  mp_holistic.Holistic(static_image_mode=True) as holistic:
  for name, image in images.items():
    results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print the real-world 3D coordinates of nose in meters with the origin at
    # the center between hips.
    print('Nose world landmark:'),
    print(results.pose_world_landmarks.landmark[mp_holistic.PoseLandmark.NOSE])
    
    # Plot pose world landmarks.
    print(f'Pose world landmarks of {name}:')
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_holistic.POSE_CONNECTIONS)
```

    Nose world landmark:
    x: -0.6770456433296204
    y: 0.11645156145095825
    z: -0.20827025175094604
    visibility: 0.9999970197677612
    
    Pose world landmarks of david-hofmann-e_rhazQLaSs-unsplash.jpg:
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_10_1.png)
    


    Nose world landmark:
    x: -0.053249772638082504
    y: -0.6610630750656128
    z: -0.21999822556972504
    visibility: 0.999910831451416
    
    Pose world landmarks of thao-le-hoang-v4zceVZ5HK8-unsplash.jpg:
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_10_3.png)
    



```
# Run MediaPipe Holistic with `enable_segmentation=True` to get pose segmentation.
with mp_holistic.Holistic(
    static_image_mode=True, enable_segmentation=True) as holistic:
  for name, image in images.items():
    results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

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
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_11_1.png)
    


    Pose segmentation of thao-le-hoang-v4zceVZ5HK8-unsplash.jpg:
    


    
![png](04-%20Mediapipe%20holistic_files/04-%20Mediapipe%20holistic_11_3.png)
    

