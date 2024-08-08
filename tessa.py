import pytesseract
from PIL import Image


def text_recognition(file_path: str, rotate: bool = False):
    image = Image.open(file_path)
    if rotate:
        img_rotate = image.rotate(90, expand=True, resample=Image.BICUBIC)
        img_rotate.save(file_path, quality=95)
        image.close()

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, lang='rus', config=custom_config)

    file_name = image.filename.split('.')[0]
    with open(f'{file_name}.txt', 'w') as file:
        file.write(text)


def main():
    file_path = input('File path: ')
    rotate = input('Rotate? (Y/n): ')
    if rotate == 'Y' or rotate == 'y':
        rotate = True
    elif rotate == 'N' or rotate == 'n':
        rotate = False
    else:
        print('Please choose "Y" or "n"!')
    text_recognition(file_path, rotate)


if __name__ == '__main__':
    main()
