import json
import os
import qrcode

counter = 0
with open('qrcodes.json') as json_file:  
    data = json.load(json_file)
    for p in data:

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=4,
        )
        qr.add_data("https://titeeni.city/qrcode/" + p)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.path.join('codes', p + '.png' ))
        counter += 1
print(counter)