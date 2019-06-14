import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# realise trot in simulators via
# train trotting gait in a simulators
# ppo with adam optimiser
# analyse the resulting gait obtained in simulation via pca
# extract motion primitives and reconstruct the gait
#realise gait in hardware by PD trajectory tracking control
# abduction gaits

#arex motors

#dual motor vs stanford bldc

#qp control : more accurate
#do position and then qp :1 kHz
# pi is not deterministic enough
# current control
