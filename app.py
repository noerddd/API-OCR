from flask import Flask, request, jsonify, render_template
from camera import capture_image
from ocr import extract_text, classify_text
from gpt3 import get_summary
from database import init_db, save_metadata, fetch_metadata

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    image_path = capture_image()
    return jsonify({'image_path': image_path})

@app.route('/extract', methods=['POST'])
def extract():
    image_path = request.json['image_path']
    text = extract_text(image_path)
    metadata = classify_text(text)
    metadata['synopsis'] = get_summary(metadata['synopsis'])
    return jsonify(metadata)


@app.route('/books', methods=['GET'])
def books():
    metadata = fetch_metadata()
    return jsonify(metadata)

@app.route('/add_book', methods=['POST'])
def add_book():
    book_data = request.json
    save_metadata(book_data)
    return jsonify({'message': 'Book added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
