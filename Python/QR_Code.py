import qrcode
data = "https://wa.link/wrvqe1"
qr = qrcode.make(data)
fname = input("Enter file name (with .png extension): ")
qr.save(fname)
print("QR Code generated successfully.")
