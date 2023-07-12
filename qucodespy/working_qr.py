# Creating and reading from QR Codes with Python!
import pyqrcode
import pyqrcodeng

data = 'Hey Your Secret Code is sfg2230d'
url = pyqrcode.create(data)
# create and save qr code in image files
# by-default qr is too small that's why we use scale
url.png('your_secret_code.png', scale=7)

# for just run the script we write main script below
if __name__ == '__main__':
    pass
