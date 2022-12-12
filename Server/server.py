import socket
import time

import cv2
import mediapipe as mp


class Hand_det_pythonClass:

    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.cap = cv2.VideoCapture(0)

    def get_coord(self):
        with self.mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) as hands:
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
                    # coord = "nothing"
                    if results.multi_hand_landmarks:
                        image_height, image_width, _ = image.shape
                        for hand_landmarks in results.multi_hand_landmarks:
                            # coord = "" \
                            #     f"WRIST-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].z * image_width, 10)}\n" \
                            #     f"THUMB_CMC-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].z * image_width, 10)}\n" \
                            #     f"THUMB_MCP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].z * image_width, 10)}\n" \
                            #     f"THUMB_IP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].z * image_width, 10)}\n" \
                            #     f"THUMB_TIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].z * image_width, 10)}\n" \
                            #     f"INDEX_FINGER_MCP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].z * image_width, 10)}\n" \
                            #     f"INDEX_FINGER_PIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].z * image_width, 10)}\n" \
                            #     f"INDEX_FINGER_DIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].z * image_width, 10)}\n" \
                            #     f"INDEX_FINGER_TIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].z * image_width, 10)}\n" \
                            #     f"MIDDLE_FINGER_MCP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z * image_width, 10)}\n" \
                            #     f"MIDDLE_FINGER_PIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z * image_width, 10)}\n" \
                            #     f"MIDDLE_FINGER_DIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z * image_width, 10)}\n" \
                            #     f"MIDDLE_FINGER_TIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z * image_width, 10)}\n" \
                            #     f"RING_FINGER_MCP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].z * image_width, 10)}\n" \
                            #     f"RING_FINGER_PIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].z * image_width, 10)}\n" \
                            #     f"RING_FINGER_DIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].z * image_width, 10)}\n" \
                            #     f"RING_FINGER_TIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].z * image_width, 10)}\n" \
                            #     f"PINKY_MCP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].z * image_width, 10)}\n" \
                            #     f"PINKY_PIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].z * image_width, 10)}\n" \
                            #     f"PINKY_DIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].z * image_width, 10)}\n" \
                            #     f"PINKY_TIP-{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height, 10)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].z * image_width, 10)}" \
                            coord.update({
                                "WRIST": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y * image_height, 3)}_{hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].z * image_width}",
                                "THUMB_CMC": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC].z * image_width, 3)}",
                                "THUMB_MCP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_MCP].z * image_width, 3)}",
                                "THUMB_IP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].z * image_width, 3)}",
                                "THUMB_TIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].z * image_width, 3)}",
                                "INDEX_FINGER_MCP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].z * image_width, 3)}",
                                "INDEX_FINGER_PIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_PIP].z * image_width, 3)}",
                                "INDEX_FINGER_DIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].z * image_width, 3)}",
                                "INDEX_FINGER_TIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].z * image_width, 3)}",
                                "MIDDLE_FINGER_MCP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z * image_width, 3)}",
                                "MIDDLE_FINGER_PIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP].z * image_width, 3)}",
                                "MIDDLE_FINGER_DIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].z * image_width, 3)}",
                                "MIDDLE_FINGER_TIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z * image_width, 3)}",
                                "RING_FINGER_MCP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].z * image_width, 3)}",
                                "RING_FINGER_PIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_PIP].z * image_width, 3)}",
                                "RING_FINGER_DIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].z * image_width, 3)}",
                                "RING_FINGER_TIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].z * image_width, 3)}",
                                "PINKY_MCP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_MCP].z * image_width, 3)}",
                                "PINKY_PIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_PIP].z * image_width, 3)}",
                                "PINKY_DIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].z * image_width, 3)}",
                                "PINKY_TIP": f"{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height, 3)}_{round(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].z * image_width, 3)}"
                                })

                            self.mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                self.mp_hands.HAND_CONNECTIONS)

                    cv2.imshow("Hand_detector", cv2.flip(image, 1))
                    if cv2.waitKey(1) & 0xFF == 27: pass

                    return coord

    def __del__(self):
        self.cap.release()


# Описываем работу сервера
# Ф-ция описывает как сервер должен принмать информацию
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8081))
# server.bind(("192.168.1.71", 11111))

server.listen()
user, address = server.accept()
print("Connect", end=" ")
print(user, address)

detect = Hand_det_pythonClass()

while True:
    coord = detect.get_coord()

    if coord:
        user.send(f"{ coord }".encode("utf-8"))
    else:
        user.send(f"nothing".encode("utf-8"))

    # time.sleep(0.2)