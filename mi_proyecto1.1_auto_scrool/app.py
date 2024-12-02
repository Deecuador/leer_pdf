from flask import Flask, send_file, render_template, request
from PyPDF2 import PdfReader, PdfWriter
import os


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render proporciona el puerto en PORT
    app.run(host='0.0.0.0', port=port)


app = Flask(__name__)
UPLOAD_FOLDER = 'documentos'  # Carpeta donde se almacenan los PDFs
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Crea la carpeta si no existe

@app.route('/')
def index():
    return render_template('index_Dos.html')

@app.route('/get-pdf/<filename>')  # Ruta dinámica para servir un PDF específico
def get_pdf(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):  # Verifica si el archivo existe
        return send_file(filepath)
    return "Archivo no encontrado", 404  # Devuelve un 404 si el archivo no está

@app.route('/upload', methods=['POST'])  # Ruta para subir archivos PDF
def upload_pdf():
    if 'file' not in request.files:
        return "No se envió ningún archivo", 400

    file = request.files['file']
    if file.filename == '':
        return "Nombre de archivo vacío", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)  # Guarda el archivo en la carpeta documentos
    return f"Archivo {file.filename} subido exitosamente"

@app.route('/rotate/<filename>')  # Ruta para rotar un archivo PDF
def rotate_pdf(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return "Archivo no encontrado", 404

    reader = PdfReader(filepath)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(90)  # Rotar cada página 90 grados
        writer.add_page(page)

    output_path = os.path.join(UPLOAD_FOLDER, f"rotado_{filename}")
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    return send_file(output_path)  # Devuelve el archivo rotado

if __name__ == '__main__':
    app.run(debug=True)
