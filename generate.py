import csv
from MyQR import myqr
import os
import base64

with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        data = row[0].encode()
        name = base64.b64encode(data)
        _, _, qr_name = myqr.run(
            str(name),
            level='H',
            version=1,
            picture='bg.jpg',
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name=str(row[0] + '.png'),  # Change the extension if needed
            save_dir=os.getcwd()
        )
        print(f"QR Code generated for: {row[0]}")
