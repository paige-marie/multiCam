import cv2
import threading
import time

class camThread(threading.Thread):
    def __init__(self, previewName, camID, p_num):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.p_num = p_num
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID, self.p_num)

def camPreview(previewName, camID, p_num):

    name = "which_cam?"
    now = int(time.time() * 1000.0)



    if camID == 2:
        name = "LGT"
    if camID == 1:
        name = "NXG"

    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    path = '/Users/logan/Desktop/multi_cam/videos/'"_" + str(now) +"_g_"+str(p_num) + "_" + str(name) + '.avi'
    width = int(cam.get(3))
    height = int(cam.get(4))
    fcc = cv2.VideoWriter_fourcc(*'XVID')
    print(path + ' recording')
    writer = cv2.VideoWriter(path, fcc, 30.0, (width, height))  # fps=30.0

    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        hms = time.strftime('%H:%M:%S', time.localtime())
        cv2.putText(frame, str(hms), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        writer.write(frame)

        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            writer.release()
            break
    cv2.destroyWindow(previewName)


# Create threads as follows
num = input("Enter group id: ")


#If Owl starts recording change numbers either 0 and 1, or 0 and 2 or 1 and 2
thread1 = camThread("Camera 1", 2, num) #NXG
thread2 = camThread("Camera 2", 1, num) #LGT


#thread3 = camThread("Camera 3", 0, num)

thread1.start()
thread2.start()
#thread3.start()
print()
print("Active threads", threading.activeCount())