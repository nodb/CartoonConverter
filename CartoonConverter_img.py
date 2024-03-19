import cv2
import numpy as np

class CartoonConverter:
    def __init__(self, image_source):
        self.image_source = image_source
        self.img = cv2.imread(image_source) # Load the image
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)    # Convert the image to grayscale
        self.gray = cv2.medianBlur(self.gray, 5)  # Apply median blur to reduce noise
        self.edges = cv2.adaptiveThreshold(self.gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)   # Detect edges using adaptive thresholding
        self.color = cv2.bilateralFilter(self.img, 13, 300, 300)   # Convert the image to color
        self.cartoon = cv2.bitwise_and(self.color, self.color, mask=self.edges) # Combine the color image with the edges mask
    
    def update(self, c, d):
            self.edges = cv2.adaptiveThreshold(self.gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, c)
            self.color = cv2.bilateralFilter(self.img, d, 300, 300)
            self.cartoon = cv2.bitwise_and(self.color, self.color, mask=self.edges)

    def run(self):
        c=9
        d=9
        level=5
        while True:
            cv2.putText(self.cartoon, f"Level: {level}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            
            cv2.imshow("Cartoon", self.cartoon) # Display the cartoon image
            
            key = cv2.waitKey(0)    # 키입력 무한 대기
            
            if key == 27 or cv2.getWindowProperty('Cartoon', cv2.WND_PROP_VISIBLE) < 1:  # ESC key or window closed
                break
            elif key == ord('+'):  # + 버튼, 엣지 검출 파라미터와 색상 보정을 강조
                c-=2
                d+=2
                level+=1
                if c>-2:
                    self.update(c, d)
                else:
                    c+=2
                    d-=2
                    level-=1
            elif key == ord('-'):  # - 버튼, 엣지 검출 파라미터와 색상 보정을 강조
                c+=2
                d-=2
                level-=1
                if d>0:
                    self.update(c, d)
                else:
                    c-=2
                    d+=2
                    level+=1
        cv2.destroyAllWindows()

if __name__ == "__main__":
    image_source = "image.jpg"
    cartoon_converter = CartoonConverter(image_source)
    cartoon_converter.run()