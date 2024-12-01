# install qr code generator module
# pip install qrcode
# pip install qrcode[pil] - pil for pillow packages handles images

# for decoding a QR Code, we need 2 more module
# pyzbar - pip install pyzbar
# pillow - pip install pillow


import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

print("Hello! Have a look I have created a QR Code!")
own_qrcode = qrcode.make("https://www.facebook.com/shahidullahkaiser.talib")
own_qrcode.save("own_qrcode.png")

decoded_data = decode(Image.open("own_qrcode.png"))
print(decoded_data[0].data.decode("ascii"))

