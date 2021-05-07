import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def build_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save('qrcode001.png')


build_qr('hi')


def decode_qr(fp: str):
    data = decode(Image.open(fp))
    print(data)


decode_qr('qrcode001.png')
