import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("webcam")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    if k == 27: # ESC
        print("Escape hit, closing...")
        break

    elif k == 32: #SPACE 
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


cam.release()

cv2.destroyAllWindows() 