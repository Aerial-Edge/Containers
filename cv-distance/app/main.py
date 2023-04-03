import cv2 as cv
import imutils
import math

# DISTANSEMÅLNG:
frameWidth = 600    # px
ballRadius = 3.25   # cm
kameraFOV = 62.2    # grader
faktor = (frameWidth / 2) * (ballRadius / math.tan(math.radians(kameraFOV / 2)))    # Piksler fra senter til kant delt på minimum avstand fra linse

def kalkulerDistanse (_ballRadius_px):
    return (int(faktor / _ballRadius_px))   # Returnerer distanse fra linse til ballen

# FARGEDETEKSJON:
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

videoCap = cv.VideoCapture(0)     # Starter opptak av /dev/video0

while True:
    (grabbed, frame) = videoCap.read()

    frame = imutils.resize(frame, width=frameWidth)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, greenLower, greenUpper)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv.contourArea)
        ((x, y), ballRadius_px) = cv.minEnclosingCircle(c)

        cv.circle(frame, (int(x), int(y)), int(ballRadius_px), (0, 255, 255), 2)

        print(kalkulerDistanse(ballRadius_px))

    # IMSHOW:
    # cv.imshow("Frame", frame)
    #key = cv.waitKey(1) & 0xFF
    #if key == ord("q"):
    #    break

videoCap.release()
#cv.destroyAllWindows()
