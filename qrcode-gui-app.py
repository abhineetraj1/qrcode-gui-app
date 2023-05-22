import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

# Function to generate the QR code
def generate_qr_code():
    data = entry.get()
    if data:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color=fill_color.get(), back_color=back_color.get())
        # Resize the image to fit in the window
        qr_image = qr_image.resize((200, 200))
        # Convert the image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(qr_image)
        # Update the image on the label
        qr_label.config(image=tk_image)
        qr_label.image = tk_image
    else:
        messagebox.showerror("Error", "Please enter data for the QR code.")

# Function to save the QR code as an image
def save_qr_code():
    image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if image_path:
        qr_image = qr_label.image
        qr_image.save(image_path)
        messagebox.showinfo("Success", "QR code saved successfully.")
    else:
        messagebox.showinfo("Information", "Saving canceled.")

# Function to reset the QR code generator
def reset_generator():
    entry.delete(0, tk.END)
    fill_color.set("black")
    back_color.set("white")
    qr_label.config(image="")

# Create the Tkinter window
window = tk.Tk()
window.title("QR Code Generator")
window.config(bg="#333333")
entry = tk.Entry(window, font=("Arial", 12), bg="#AAAAAA", fg="#333333")
entry.pack(pady=10)
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code, bg="#AAAAAA", fg="#333333")
generate_button.pack(pady=5)
qr_label = tk.Label(window, bg="#333333")
qr_label.pack(pady=10)
save_button = tk.Button(window, text="Save QR Code", command=save_qr_code, bg="#AAAAAA", fg="#333333")
save_button.pack(pady=5)
design_frame = tk.LabelFrame(window, text="Design Options", padx=10, pady=10, bg="#333333", fg="#AAAAAA")
design_frame.pack(pady=10)
fill_color_label = tk.Label(design_frame, text="Fill Color:", bg="#333333", fg="#AAAAAA")
fill_color_label.grid(row=0, column=0, padx=5, pady=5)
fill_color = tk.StringVar(value="black")
fill_color_dropdown = tk.OptionMenu(design_frame, fill_color, "black", "red", "green", "blue")
fill_color_dropdown.config(bg="#AAAAAA", fg="#333333")
fill_color_dropdown.grid(row=0, column=1, padx=5, pady=5)
back_color_label = tk.Label(design_frame, text="Background Color:", bg="#333333", fg="#AAAAAA")
back_color_label.grid(row=1, column=0, padx=5, pady=5)
back_color = tk.StringVar(value="white")
back_color_dropdown = tk.OptionMenu(design_frame, back_color, "white", "black", "gray", "lightgray")
back_color_dropdown.config(bg="#AAAAAA", fg="#333333")
back_color_dropdown.grid(row=1, column=1, padx=5, pady=5)
reset_button = tk.Button(window, text="Reset", command=reset_generator, bg="#AAAAAA", fg="#333333")
reset_button.pack(pady=5)

window.mainloop()