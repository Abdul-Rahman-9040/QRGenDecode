
# QRGenDecode

This project is a simple web application that allows users to generate and decode QR codes. The application is built using Python and Flask.


## Features
#### QR Code Generator:
- Accepts input data.
- Encodes the data into a QR code.
- Allows users to download the generated QR code.
#### QR Code Decoder:
- Accepts a QR code as input.
- Decodes the QR code to retrieve the encoded data.

## Tech Stack

**Front End:** HTML,CSS

**Backend:** Python Flask

**Libraries:**
- qrcode (for generating QR codes)
- pyzbar (for decoding QR codes)
- Flask (for web framework)

## Installation

Clone the repository:

```bash
git clone https://github.com/Abdul-Rahman-9040/QRGenDecode.git
cd QRGenDecode
```
Install the required packages:

```bash
pip install -r requirements.txt
```
## Usage/Examples
1. Run the Flask application:
```
python app.py
```
2. Open your web browser and navigate to http://127.0.0.1:5000.

3. Use the QR Code Generator to create a QR code by entering your data and clicking "Generate QR Code". You can download the generated QR code.

4. Use the QR Code Decoder to decode a QR code by uploading a QR code image and clicking "Decode QR Code". The decoded data will be displayed.




