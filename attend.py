import cv2
import csv
import pyzbar.pyzbar as pyzbar
import time

cap = cv2.VideoCapture(0)
names = []

with open('attendance.csv', 'a+', newline='') as csvfile:
    fieldnames = ['Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if csvfile.tell() == 0:
        writer.writeheader()

    def enterData(z):
        if z not in names:
            names.append(z)
            writer.writerow({'Name': z})
            return names

    def checkData(data):
        data = str(data)
        if data in names:
            print("Already present")
        else:
            print('\n' + str(len(names) + 1) + '\n' + 'Present done')
            enterData(data)

    print("Reading code ...........................")

    while True:
        _, frame = cap.read()

        if frame is not None:
            decodeObjects = pyzbar.decode(frame)

            for obj in decodeObjects:
                checkData(obj.data)
                time.sleep(1)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.destroyAllWindows()
                break

cap.release()
cv2.destroyAllWindows()
