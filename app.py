



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
