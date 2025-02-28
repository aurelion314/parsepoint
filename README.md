# ParsePoint NLP API

A Natural Language Processing API that tokenizes text and provides Part of Speech (POS) data, similar to Google's NLP API.

## Features

- Text tokenization
- Part of Speech (POS) tagging
- Lemmatization
- Dependency parsing
- Sentence segmentation
- Interactive demo UI

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment (included)

### Installation

1. Activate the virtual environment:

```bash
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate     # On Windows
```

2. The required packages are already installed in the virtual environment:
   - FastAPI
   - uvicorn
   - spaCy
   - python-multipart

### Running the Application

1. Start the server:

```bash
python -m app.main
```

2. Open your browser and navigate to:
   - http://localhost:8000 - For the demo UI
   - http://localhost:8000/docs - For the API documentation (Swagger UI)

## API Endpoints

### POST /api/process

Process text and return tokens with POS data.

**Request Body:**
```json
{
  "text": "Your text to analyze here."
}
```

**Response:**
```json
{
  "tokens": [
    {
      "text": "Your",
      "lemma": "your",
      "pos": "PRON",
      "tag": "PRP$",
      "dep": "poss",
      "is_stop": true,
      "is_alpha": true,
      "is_punct": false
    },
    ...
  ],
  "sentences": [
    "Your text to analyze here."
  ],
  "text": "Your text to analyze here."
}
```

### POST /api/process-form

Same as above but accepts form data instead of JSON.

## Development

The project structure is organized as follows:

```
parsepoint/
├── venv/                  # Virtual environment
├── app/
│   ├── main.py            # Application entry point
│   ├── api/
│   │   └── nlp_api.py     # API endpoints
│   ├── nlp/
│   │   └── nlp_service.py # NLP processing logic
│   ├── static/
│   │   └── css/           # CSS files
│   └── templates/
│       └── index.html     # Demo UI template
└── README.md              # This file
