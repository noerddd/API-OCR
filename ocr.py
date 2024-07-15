import pytesseract
from PIL import Image
import re

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def classify_text(text):
    lines = text.split('\n')
    metadata = {
        'title': '',
        'author': '',
        'isbn': '',
        'synopsis': '',
        'keywords': ''
    }

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Simple rules for classification
        if 'ISBN' in line:
            metadata['isbn'] = line
        elif re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+$', line):  # Simple pattern for author
            metadata['author'] = line
        elif len(line.split()) < 10 and not metadata['title']:
            metadata['title'] = line
        else:
            metadata['synopsis'] += line + ' '

    # Simple keywords extraction
    metadata['keywords'] = ', '.join(set(metadata['synopsis'].split()))

    return metadata
