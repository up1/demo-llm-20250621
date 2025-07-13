from typhoon_ocr import ocr_document
import os

# please set env TYPHOON_API_KEY

image_path = "./data/doc-scan.pdf"

markdown = ocr_document(
    image_path, page_num=2)
print(markdown)