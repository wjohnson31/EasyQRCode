from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Path to save the QR code image
QR_CODE_IMG = "static/qrcode.png"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the data from the form input
        data = request.form["data"]

        # Create a QR code
        qr = qrcode.QRCode(
            version=1,  # size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate the image
        img = qr.make_image(fill="black", back_color="white")
        img.save(QR_CODE_IMG)

        # Display the generated QR code
        return render_template("index.html", qr_code=QR_CODE_IMG)

    return render_template("index.html", qr_code=None)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
