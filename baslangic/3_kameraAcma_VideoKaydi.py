# !pip install cv2
import cv2
# capture
cap = cv2.VideoCapture(0) # 0 bilgisayar kamerasini ifade eder

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# video kaydet
# VideoWriter_fourcc = Video kaydetmek icin windows icin cerceveleri sikistirma islemi 4 karakterli codec kodu
writer = cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))

while True: 
    # ret = return
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    # save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
writer.release()
cv2.destroyAllWindows()
    


