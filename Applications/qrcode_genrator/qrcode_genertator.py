from pathlib import Path
import importlib

qrcode = importlib.import_module("qrcode")

data = input("Enter some text or URL: ").strip()
filename = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

output_dir = Path(__file__).resolve().parent / "qr_images"
output_dir.mkdir(exist_ok=True)

image.save(output_dir / f"{filename}.png")

print(f"QR code saved as {filename}.png")