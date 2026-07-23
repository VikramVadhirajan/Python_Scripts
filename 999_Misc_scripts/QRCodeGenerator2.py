import tkinter as tk
from PIL import Image, ImageTk
import qrcode

def generate_qr_code(text):
    # Create a QR code object with the given text
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make()

    # Generate the PIL image from the QR code
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Resize image if needed (optional)
    # img = img.resize((200, 200), Image.ANTIALIAS)

    # Convert PIL image to Tkinter PhotoImage
    photo = ImageTk.PhotoImage(img)
    return photo

def show_qr():
    text = text_entry.get()
    qr_image = generate_qr_code(text)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image  # Keep a reference to prevent garbage collection

root = tk.Tk()
root.title("QR Code Generator")

# Entry for input text
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=show_qr)
generate_button.pack(pady=5)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()