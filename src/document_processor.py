import fitz
from paddleocr import PaddleOCR
from PIL import Image

class DocumentProcessor:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

    def process_document(self, document_path):
        doc = fitz.open(document_path)
        text_content = ""
        images = []
        is_ocr = False

        for page in doc:
            text = page.get_text()
            if text.strip():
                text_content += text
            else:
                is_ocr = True

            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)

        if is_ocr:
            text_content = self._perform_ocr(images)

        return text_content, images, is_ocr

    def _perform_ocr(self, images):
        texts = []
        for img in images:
            result = self.ocr.ocr(img, cls=True)
            text = "\n".join([line[1][0] for line in result[0]] if result[0] else "")
            texts.append(text)

        return "\n".join(filter(None, texts))