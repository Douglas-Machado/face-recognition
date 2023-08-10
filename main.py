import cv2
from deepface import DeepFace
import os

files = os.listdir()
extensions = ["jpg", "jpeg", "png"]

for file in files:
    if any([extension in file for extension in extensions]):
        image = cv2.imread("sorrindo.jpg")

        result = DeepFace.analyze(image, actions=("age", "emotion", "gender", "race"))

        print(result)