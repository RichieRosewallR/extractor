# Invoice Information Extractor

This project provides an API for extracting structured information from invoice PDFs using OCR and NLP techniques.

## Features

- PDF text extraction with automatic OCR fallback
- Information extraction using the NuExtract-1.5 model
- FastAPI-based REST API
- Support for both searchable and scanned PDFs

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd invoice_extractor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python src/main.py
```

2. The API will be available at `http://localhost:8000`

3. Use the `/extract/{file_path}` endpoint to process invoices:
```bash
curl http://localhost:8000/extract/path/to/your/invoice.pdf
```

4. Access the API documentation at `http://localhost:8000/docs`

## API Endpoints

- `GET /extract/{file_path}`: Extracts information from the specified PDF file
  - Parameters:
    - `file_path`: Path to the PDF file (URL encoded)
  - Returns: JSON object containing extracted information

## Project Structure

- `src/`: Source code directory
  - `document_processor.py`: PDF processing and OCR
  - `model_handler.py`: NuExtract model interface
  - `examples.py`: Example data for model training
  - `main.py`: Application entry point
- `api/`: API-related code
  - `endpoints.py`: FastAPI endpoint definitions
- `requirements.txt`: Project dependencies