import glob
import time
from send_email import send_email
from datetime import datetime
from threading import Thread
import os
import cv2

video = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
status_list = []
count = 1


def clean_folder():
    print("Clean folder function started")
    images = glob.glob("images_web/*png")
    for image in images:
        os.remove(image)
    print("Clean folder function finished")


while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    now = datetime.now()
    cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                thickness=2, lineType=cv2.LINE_AA)
    cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                thickness=2, lineType=cv2.LINE_AA)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # if it's a fake object we just continue
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images_web/{count}.png", frame)
            count += 1
            all_images = glob.glob("images_web/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object, ))
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow("My video", frame)
    # close the app if the user click on "Q" on keyboard
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
clean_thread = Thread(target=clean_folder())
clean_thread.daemon = True
clean_thread.start()