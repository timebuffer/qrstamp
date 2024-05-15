import qrcode

# URL of the Git repository
url = 'https://github.com/timebuffer/timestamp'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an Image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save it somewhere, change the path as needed
img.save('repository_qr.png')

print("QR code generated successfully!")
