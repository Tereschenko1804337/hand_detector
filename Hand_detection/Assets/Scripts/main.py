import cv2
import mediapipe as mp

# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
#
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#         model_complexity=0,
#         min_detection_confidence=0.5,
#         min_tracking_confidence=0.5) as hands:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             continue
#
#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         results = hands.process(image)
#
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#         if results.multi_hand_landmarks:
#
#             image_height, image_width, _ = image.shape
#             for hand_landmarks in results.multi_hand_landmarks:
#                 # print(f"x: { hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width } \n"
#                 #       f"y: { hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height } \n"
#                 #       f"z: { hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z * image_width }")
#                 mp_drawing.draw_landmarks(
#                     image,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS)
#         cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
#         if cv2.waitKey(5) & 0xFF == 27:
#             break
# cap.release()

class Hand_det_pythonClass:

    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.cap = cv2.VideoCapture(0)

    def get_coord(self):
        with self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            if self.cap.isOpened():
                success, image = self.cap.read()
                if not success:
                    return 0
                else:
                    image.flags.writeable = False
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    results = hands.process(image)

                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    coord = {}
                    if results.multi_hand_landmarks:
                        image_height, image_width, _ = image.shape
                        for hand_landmarks in results.multi_hand_landmarks:
                            coord.update({
                                "WRIST": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].z * image_width,
                                },
                                "THUMB_CMC": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].z * image_width,
                                },
                                "THUMB_MCP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].z * image_width,
                                },
                                "THUMB_IP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].z * image_width,
                                },
                                "THUMB_TIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].z * image_width,
                                },
                                "INDEX_FINGER_MCP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].z * image_width,
                                },
                                "INDEX_FINGER_PIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].z * image_width,
                                },
                                "INDEX_FINGER_DIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].z * image_width,
                                },
                                "INDEX_FINGER_TIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].z * image_width,
                                },
                                "MIDDLE_FINGER_MCP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z * image_width,
                                },
                                "MIDDLE_FINGER_PIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z * image_width,
                                },
                                "MIDDLE_FINGER_DIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z * image_width,
                                },
                                "MIDDLE_FINGER_TIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z * image_width,
                                },
                                "RING_FINGER_MCP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].z * image_width,
                                },
                                "RING_FINGER_PIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].z * image_width,
                                },
                                "RING_FINGER_DIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].z * image_width,
                                },
                                "RING_FINGER_TIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].z * image_width,
                                },
                                "PINKY_MCP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].z * image_width,
                                },
                                "PINKY_PIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].z * image_width,
                                },
                                "PINKY_DIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].z * image_width,
                                },
                                "PINKY_TIP": {
                                    "x": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width,
                                    "y": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height,
                                    "z": hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].z * image_width,
                                },
                            })

                            self.mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                self.mp_hands.HAND_CONNECTIONS)
                    return coord

    def __del__(self):
        self.cap.release()


detect = Hand_det_pythonClass()
while True:
    coord = detect.get_coord()

    try:
        with open("coord.json", "w") as file:
            file.write(f"{coord}")
            file.close()
    except:
        pass

"""

WRIST
THUMB_CMC
THUMB_MCP
THUMB_IP
THUMB_TIP
INDEX_FINGER_MCP
INDEX_FINGER_PIP
INDEX_FINGER_DIP
INDEX_FINGER_TIP
MIDDLE_FINGER_MCP
MIDDLE_FINGER_PIP
MIDDLE_FINGER_DIP
MIDDLE_FINGER_TIP
RING_FINGER_MCP
RING_FINGER_PIP
RING_FINGER_DIP
RING_FINGER_TIP
PINKY_MCP
PINKY_PIP
PINKY_DIP
PINKY_TIP

"""