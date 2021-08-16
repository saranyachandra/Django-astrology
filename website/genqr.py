import pyqrcode

qr = pyqrcode.create('hello')
qr.png('abc', scale=8)