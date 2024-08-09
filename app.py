from fastapi import FastAPI

# import easyocr

app = FastAPI()


@app.post('/')
def text_recognition(file_path: str):
    # reader = easyocr.Reader(['ru', 'en'])
    # result = reader.readtext(file_path)

    return {'1234': 1234}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
