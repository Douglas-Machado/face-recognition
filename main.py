import cv2

from deepface import DeepFace

image = cv2.imread("sorrindo.jpg")

result = DeepFace.analyze(image, actions=("age", "emotion", "gender", "race"))

print(result)