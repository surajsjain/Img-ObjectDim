from keras.models import load_model
import yolo
import cv2

model = load_model('yolo.h5')


def captureImg(webCam):
    cap = cv2.VideoCapture(webCam)
    i=0
    ret, frame = cap.read()
    cv2.imwrite('../pics/pic'+str(webCam)+'.png', frame)
    cap.release()
    cv2.destroyAllWindows()

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow("imshow",frame)
#     key=cv2.waitKey(30)
#     if key==ord('q'):
#         break
#     if key==ord('c'):
#         i+=1
#         cv2.imshow("imshow2",frame)
#         cv2.imwrite('../pics/'+str(i)+'.png', frame)
#         print("Wrote Image")
#
# # release the capture
# cap.release()
# cv2.destroyAllWindows()

# ## Test script
# captureImg(0)
# print(str(yolo.getBoxes('../pics/pic0.png', model)))
