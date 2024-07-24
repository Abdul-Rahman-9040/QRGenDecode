from flask import Flask, request, send_file, render_template, jsonify
import qrcode
import io
import base64
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return jsonify({'img_base64': img_base64})

@app.route('/download', methods=['POST'])
def download():
    data = request.form['data']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return send_file(buf, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

@app.route('/decode', methods=['POST'])
def decode():
    file = request.files['file']
    npimg = np.fromfile(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    decoded_objects = pyzbar.decode(img)
    result = ""
    for obj in decoded_objects:
        result += obj.data.decode('utf-8')
    return jsonify({'decoded_data': result})

if __name__ == '__main__':
    app.run(debug=True)
