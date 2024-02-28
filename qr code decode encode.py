import pyqrcode
import png

#creating qr
link = "https://www.instagram.com/the.clever.programmer/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)


#decoding qr
from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR = decode(Image.open('instagram.png'))
print(decocdeQR[0].data.decode('ascii'))