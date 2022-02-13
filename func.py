# Функции для ReadBarcodeBot


# для распознавания штрих-кодов
from pyzbar.pyzbar import decode
from PIL import Image  # pip install Pillow


def img_decode () -> str:
    """Распознаёт штрихкод на фотке."""
    print('Привет')
    image_barcode = Image.open('img.jpg')
    img_decode = decode(image_barcode)
    if img_decode:
        mes = 'штрих-код: '+ img_decode[0].data.decode('utf-8')
        print(mes)
    else:
        mes = 'нет штрихкода'
        print(mes)
    return mes