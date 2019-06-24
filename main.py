from document_scanner.scanner import DocScanner
from ocr.core import ocr
import argparse
import os

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", help="Path to single image to be scanned")

    args = vars(ap.parse_args())
    file_path = args["image"]

    scanner = DocScanner(False)

    valid_formats = [".jpg", ".jpeg", ".jp2", ".png", ".bmp", ".tiff", ".tif"]

    get_ext = lambda f: os.path.splitext(f)[1].lower()

    # Scan single image specified by command line argument --image <IMAGE_PATH>
    if file_path:
        path = scanner.scan(file_path)
        print("scan completed.")
        print( ocr(path))

    else:
        raise Exception("Can not read file %s" % file_path)
