# CartoonConverter 🎨

## ✍ 소개
- 이미지 및 동영상을 만화(cartoon) 스타일로 변환하는 프로그램입니다.
- 이미지 변환 : CartoonConverter_img.py
- 동영상 변환 : CartoonConverter_video.py

## 🗂️ 사용 기술
- Python
- OpenCV

## 💻 기능
- 키보드 기능
  - \+ : 만화 같은 느낌이 강해진다. level이 1 커진다
  - \- : 만화 같은 느낌이 약해진다. level이 1 작아진다
  - ESC : 프로그램 종료
- 마우스 기능
  - X 버튼 : 프로그램 종료
- 화면 기능
  - level : 현재 만화 정도 레벨(1~10), 기본 값 : 5

## 🏆 한계
- '+' 버튼을 누르면 adaptiveThreshold의 C(임계값) 파라미터를 작게하고 bilateralFilter의 D(필터링에 사용될 이웃 픽셀의 거리) 파리미터를 크게하여 만화 같은 느낌이 잘 표현되게 한다.
- '-' 버튼을 누르면 반대로 C(임계값) 파라미터를 크게하고 D(필터링에 사용될 이웃 픽셀의 거리) 파리미터를 작게하여 만화 같은 느낌을 줄인다.
- 영상 변환의 경우 + 값을 통해 level이 높아지면 Otsu 이진화 연산에서 점점 느려져 영상 프레임이 점점 느려지는 한계점을 가지고 있다.

## 시연
- 이미지 변환
- https://youtube.com/shorts/0obI8tKbhik
- https://youtube.com/shorts/hS0APrEdorc
- 동영상 변환
- https://youtu.be/NS-a7UPqMvY
- https://youtu.be/xaw4gMae0yQ
