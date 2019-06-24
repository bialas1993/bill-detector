try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr(filename):
    """
    This function will handle the core OCR processing of images.
    """
    tessdata_dir_config = r'--tessdata-dir "./tessdata"'

    return pytesseract.image_to_string(Image.open(filename), config=tessdata_dir_config, lang='pol')
