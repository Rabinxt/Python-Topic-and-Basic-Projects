import qrcode

# Data to encode
data = "https://example.com"

# Create QR Code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest, 40 is the largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
