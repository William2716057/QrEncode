import qrcode

def encode_to_qr_code(data, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

if __name__ == "__main__":
    text = input("Enter text to convert into QR code: ")
    filename = input("Enter filename with extension: ")
    output_path = filename #will save to current directory
    encode_to_qr_code(text, output_path)
    print(f"Saved as {output_path}")