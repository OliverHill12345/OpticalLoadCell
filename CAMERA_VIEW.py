import cv2
import time

cap1 = cv2.VideoCapture(0) 
#print(cap1.isOpened())
#cap1.set(3, 800)
#cap1.set(4, 600)
time.sleep(0.5) 

fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('20 5 5.avi',fourcc, 24.0, (640,480))



while(cap1.isOpened()):
    ret, frame = cap1.read()
    if True:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap1.release()
out.release
cv2.destroyAllWindows()