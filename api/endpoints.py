from fastapi import FastAPI, HTTPException
from src.document_processor import DocumentProcessor
from src.model_handler import ModelHandler
from src.examples import get_values
import os

app = FastAPI(title="Invoice Information Extractor")

doc_processor = DocumentProcessor()
model_handler = ModelHandler()

@app.get("/extract/{file_path}")
async def get_extracted_json(file_path: str):
    try:
        # Validate file path
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")

        # Process document
        text_content, images, is_ocr = doc_processor.process_document(file_path)
        print(f"Document has been processed using {'OCR' if is_ocr else 'PDF parsing'}")

        # Get example values
        keys_to_extract, example_text, example_json = get_values()

        # Extract information
        output = model_handler.extract_information(
            text_content,
            keys_to_extract,
            example_text,
            example_json
        )

        return output

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))