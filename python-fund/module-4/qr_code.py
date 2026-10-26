import qrcode

# Define the target URL or text
url = "https://alphabitinfoway.com/"

# Generate the QR code image directly
img = qrcode.make(url)

# Save the image to your local directory
img.save("basic_qr.png")
