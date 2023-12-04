**ATTENDANCE MANAGEMENT SYSTEM USING QR CODE **

##Attendance Management System Documentation

**Overview
The Attendance Management System is a Python-based 
web application that utilizes Flask for creating a 
simple system to manage and record attendance data. 
The system includes a web interface for users to 
input data and a manual input script for data entry.

Files
styles.css
Purpose: Defines the styling for the HTML templates.
Usage: Included in the input_form.html for styling the input form.

body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #0b0707; /* Set a background color if the image doesn't cover the entire screen */
}
.background-image {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    opacity: 0.4;
}
.background-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 1; /* Increment the z-index value */
}
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(4, 200, 200, 0.8);
    z-index: 2;
}


input_form.html

Purpose: HTML template for the data input form.
Usage: Rendered by Flask to create the web interface for users to input attendance data.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV Data Input</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="background-image">
        <img src="{{ url_for('static', filename='home.png') }}" alt="Background Image">
    </div>
    <div class="overlay"></div>
    <div class="container">
        <form action="/submit" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="class">Class:</label>
            <input type="text" id="class" name="class" required><br>
            <label for="roll">Roll Number:</label>
            <input type="text" id="roll" name="roll" required><br>
            <label for="section">Section:</label>
            <input type="text" id="section" name="section" required><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>



app.py

Purpose: Main application script using Flask for handling web requests.
Endpoints:
/: Renders the input form.
/submit: Handles form submissions, adds data to the CSV file, and redirects to the input form.


from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)
@app.route('/')
def index():
    return render_template('input_form.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    class_name = request.form['class']
    roll_no = request.form['roll']
    section = request.form['section']
    data_row = [name, class_name, roll_no, section]
    # Call the function to write data to the CSV file
    write_to_csv(data_row, 'data.csv')
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)



input_byuser.py
Purpose: Script for manually inputting data into the CSV file.
Usage: Run independently to input data manually into the system.


import csv
def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)
if __name__ == "__main__":
    # File name for the CSV file
    csv_file_name = 'data.csv'
    print("Enter data for the CSV file. Type 'exit' to stop.")
    while True:
        # Take input for each column
        name = input("Enter Name: ")
        class_name = int(input("Enter Class: "))
        roll_no = int(input("Enter Roll No: "))
        section = input("Enter Section: ")
        # Check if the user wants to exit
        if name.lower() == 'exit':
            break
        # Create a list with the entered data
        data_row = [name, class_name, roll_no, section]
        # Call the function to write data to the CSV file
        write_to_csv(data_row, csv_file_name)
    print(f"Data has been installed into {csv_file_name}")


Running the Application:



Execute app.py to start the Flask web server.
Open a web browser and navigate to http://127.0.0.1:5000/ to access the input form.
Data Input:

Fill in the details in the web form and click "Submit" to add data to the CSV file.
To manually input data, run input_byuser.py and follow the prompts. Type 'exit' to stop entering data.
Dependencies
Ensure you have Flask installed. If not, install it using pip install flask.
Notes
The system stores data in a CSV file named data.csv.
The web interface is styled using the styles.css file.
Manually input data using the input_byuser.py script by following the prompts.
Project Structure
The project consists of the following files:

Web Application
app.py

Purpose: Implements the Flask web application for data input.
Usage: Run the Flask app using python app.py. Access the input form through a web browser.
styles.css

Purpose: Defines the styling for the HTML templates.
Usage: Included in the input_form.html for styling the input form.
input_form.html

Purpose: HTML template for the data input form.
Usage: Rendered by Flask to create the web interface for users to input attendance data.
QR Code Generation
generate.py

Purpose: Generates QR codes for each entry in the data.csv file using MyQR.
Usage: Run using python generate.py. QR codes are saved as PNG files.
QR Code Scanning
scann.py

Purpose: Implements QR code scanning using OpenCV and updates attendance in attendance.csv.
Usage: Run using python scann.py. The GUI displays attendance information.
QR Code Generation
To generate QR codes for the entered data, execute the following steps:

bash
Copy code
python generate.py
This script reads data from data.csv and generates corresponding QR codes, saving them as PNG files.

QR Code Scanning
To start QR code scanning and track attendance, execute the following steps:

bash
Copy code
python scann.py
The script opens a GUI for attendance tracking, allowing users to start and stop the attendance process. Detected QR codes are cross-referenced with entries in attendance.csv.

Dependencies
Ensure that the required Python packages are installed before running the application. Install them using:


bash
Copy code
pip install Flask MyQR opencv-python pyzbar
Note: MyQR requires additional dependencies for image processing. Follow the instructions provided by MyQR for installation.

Manual Data Input
The project also supports manual data input using the script input_byuser.py. Run the script and follow the prompts to input data into the system.**

Feel free to customize the project according to your specific requirements.





