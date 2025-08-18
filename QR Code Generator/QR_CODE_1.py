import qrcode


Qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=2,
                   )

Qr.add_data("rabinchhatkuli.com.np")
Qr.make(fit=True)
img = Qr.make_image(fill_color = "white", back_color = "blue")
img.save(stream="./QR Code Generator/img.png",)