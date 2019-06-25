try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract

def ocr(filename):
    """
    This function will handle the core OCR processing of images.
    """
    
    """
    psm  6 / 7 / 3
    """
    tessdata_dir_config = r'--tessdata-dir "./tessdata" --oem 2 --psm 3'

    detected = pytesseract.image_to_string(Image.open(filename), config=tessdata_dir_config, lang='pol')

    print(detected)

    img = cv2.imread(filename)
    h, w, _ = img.shape 
    boxes = pytesseract.image_to_boxes(img) 

    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    cv2.imshow(filename, img)
    cv2.waitKey(0)

    return detected
