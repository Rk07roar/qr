import cv2
import csv
import pyzbar.pyzbar as pyzbar
import time
import tkinter as tk
from tkinter import ttk

class AttendanceApp:
    def __init__(self, root):
        self.background_image = tk.PhotoImage(file="home.png")
        # Resize the image to fit the screen
        self.background_image = self.background_image.zoom(2)  # Zoom the image
        self.background_label = ttk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image
        root.style = ttk.Style()
        root.style.configure("Start.TButton", foreground="green")
        root.style.configure("Stop.TButton", foreground="red")

        self.root = root
        self.root.title("Galgotias Attendance System")

        # Increase the size of the container (box)
        self.container = ttk.Frame(root, width=800, height=600)
        self.container.pack_propagate(False)  # Prevent the container from resizing its children
        self.container.pack(pady=60)

        self.names = []

        self.label = ttk.Label(self.container, text="Galgotias Attendance System", font=("Helvetica", 30), foreground="blue")
        self.label.pack()

        self.text_var = tk.StringVar()
        self.text_var.set("")

        self.result_label = ttk.Label(self.container, textvariable=self.text_var)
        self.result_label.pack(pady=20)

        self.start_button = ttk.Button(self.container, text="Start Attendance", command=self.start_attendance, style="Start.TButton")
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.container, text="Stop Attendance", command=self.stop_attendance, style="Stop.TButton")
        self.stop_button.pack(pady=10)

        # OpenCV setup
        self.cap = cv2.VideoCapture(0)
        self.reading_code = False

    def enter_data(self, z):
        if z not in self.names:
            self.names.append(z)
            writer.writerow({'Name': z})
            return self.names

    def check_data(self, data):
        data = data.decode('utf-8')
        if data in self.names:
            self.text_var.set(f"{data} already present")
        else:
            self.text_var.set(f"{data} present done")
            self.enter_data(data)

    def start_attendance(self):
        self.reading_code = True
        self.text_var.set("Reading code ...")
        self.root.after(100, self.process_frame)

    def stop_attendance(self):
        self.reading_code = False
        self.text_var.set("Attendance stopped")

    def process_frame(self):
        if self.reading_code:
            _, frame = self.cap.read()

            if frame is not None:
                # Resize the frame
                frame = cv2.resize(frame, (800, 600))  # Adjust the size as needed

                decode_objects = pyzbar.decode(frame)

                for obj in decode_objects:
                    self.check_data(obj.data)
                    time.sleep(1)

                # Display the resized frame
                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    self.stop_attendance()

            self.root.after(100, self.process_frame)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    with open('attendance.csv', 'a+', newline='') as csvfile:
        fieldnames = ['Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        root = tk.Tk()
        app = AttendanceApp(root)
        app.run()

        app.cap.release()
        cv2.destroyAllWindows()
