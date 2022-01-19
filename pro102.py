import cv2
import dropbox
import time
import random
stime = time.time()
def takeSnapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        iname = "img"+str(number)+".png"
        cv2.imwrite(iname,frame)
        stime = time.time
        result = False
    
    return iname
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(iname):
    accessToken = 'sl.BAaYeu9R4f7Kkt36nVCtA6Q-yHYQsZ49yezdjKFikYctSDZOIwSM8HQwMXKRB8lgUX2jzovYRwAXHTiM7geTYc1gn8lmNsbPA8-qhF3hkfLWAUOCnbRvGjfM6-q7FF5PeiF3bR2DCjnG'
    file = iname
    filefrom = file
    fileto = "/photo/"+(iname)
    dbx = dropbox.Dropbox(accessToken)
    with open(filefrom, "rb") as f:
        dbx.files_upload(f.read(), fileto, mode = dropbox.files.WritMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if(time.time()-stime)>=5:
            name = takeSnapshot()
            uploadFiles(name)

main()


