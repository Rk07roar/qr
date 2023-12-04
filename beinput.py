

import csv

def write_to_csv(data, file_name):
    # Open the CSV file in append mode
    with open(file_name, 'a', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write data to the CSV file
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