import qrcode
from PIL import Image  

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.youtube.com/channel/UCAYO6s81SqtD7hQqwXORKtg/playlists"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("test.png")

print("QR Code generated successfully and saved as test.png")
