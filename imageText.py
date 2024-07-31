import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'D:\PROGRAMING\Softwares\tesseract'
pytesseract.pytesseract.tesseract_cmd = r'D:\PROGRAMING\Softwares\tesseract\tesseract.exe'


image = Image.open('quote.jpeg')

image_text = pytesseract.image_to_string(image)

print(image_text)