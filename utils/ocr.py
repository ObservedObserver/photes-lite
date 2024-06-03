import easyocr
def ocr(image_path: str):
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext(image_path, detail=0)
    return result