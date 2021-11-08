from pyzbar.pyzbar import decode
from PIL import Image

import Constant


def get_data(barcode_link: str) -> str:
    source_image = Image.open(barcode_link)
    data = ''.join(
        map(lambda symbol: symbol.data.decode(Constant.ENCODING_TYPE), decode(source_image)))
    return data
