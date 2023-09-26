import json
import qrcode
from io import BytesIO
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = json.loads(request.data)
    input_word = data['inputWord']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_word)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert the QR code image to base64 for embedding in HTML
    buffered = BytesIO()
    qr_image.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()

    return f"data:image/png;base64,{qr_base64}"

if __name__ == '__main__':
    app.run(debug=True)
