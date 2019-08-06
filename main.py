import cv2
videofile = "Play1.mp4"
cap = cv2.VideoCapture(videofile)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    if (ret):
        # edit the frame here to search for players
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()