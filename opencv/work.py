import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    im_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    t, binary_img = cv2.threshold(im_grey, 145, 255, cv2.THRESH_BINARY_INV)
 
    contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    o1 = cv2.drawContours(frame, contours, -1, (0, 0, 255), 5)
    cv2.imshow('frame', o1)
    if cv2.waitKey(1) == ord('q'):
        out = cv2.imwrite('pic001.jpg', frame)
        break
cap.release()
cv2.destroyAllWindows()