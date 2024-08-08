import easyocr


def text_recognition(file_path: str):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(file_path)

    return result


def main():
    file_path = input('File path: ')
    print(text_recognition(file_path))


if __name__ == '__main__':
    main()
