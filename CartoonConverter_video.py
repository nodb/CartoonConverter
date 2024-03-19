import cv2
import numpy as np

class CartoonConverter:
    def __init__(self, video_source):
        self.video_source = video_source
        self.capture = cv2.VideoCapture(video_source)
        if not self.capture.isOpened():
            print("Error opening video")
            return
        self.c = 9  # 엣지 검출 파라미터
        self.d = 9  # 색상 보정 파라미터

    def update(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
        gray = cv2.medianBlur(gray, 5)  # Apply median blur to reduce noise
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, self.c)   # Detect edges using adaptive thresholding
        color = cv2.bilateralFilter(frame, self.d, 300, 300)   # Convert the frame to color
        cartoon = cv2.bitwise_and(color, color, mask=edges) # Combine the color frame with the edges mask
        return cartoon

    def run(self):
        level = 5
        while True:
            ret, frame = self.capture.read()
            if not ret:
                print("Error reading frame")
                break
            
            cartoon = self.update(frame)
            
            cv2.putText(cartoon, f"Level: {level}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            
            cv2.imshow("Cartoon", cartoon) # Display the cartoon frame

            key = cv2.waitKey(25)
            if key == 27 or cv2.getWindowProperty('Cartoon', cv2.WND_PROP_VISIBLE) < 1:
                break
            elif key == ord('+'):  # + 버튼, 엣지 검출 파라미터와 색상 보정을 강조
                self.c -= 2
                self.d += 2
                level+=1
                if self.c < -2:
                    self.c += 2
                    self.d -= 2
                    level-=1
            elif key == ord('-'):  # - 버튼, 엣지 검출 파라미터와 색상 보정을 강조
                self.c += 2
                self.d -= 2
                level-=1
                if self.d < 0:
                    self.c -= 2
                    self.d += 2
                    level+=1

        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_source = "video.mp4"
    cartoon_converter = CartoonConverter(video_source)
    cartoon_converter.run()
