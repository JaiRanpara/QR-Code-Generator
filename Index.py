import qrcode, PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# functions for generation of QR Code


def GenerateQRCode(*args):
    data = text_input.get()
    if data:
        image = qrcode.make(data)
        resized_img = image.resize((280, 250))
        final_image = ImageTk.PhotoImage(resized_img)
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=final_image)
        qr_canvas.image = final_image
    else:
        messagebox.showwarning(
            title="invalid input", message="Please give a valid input"
        )


def SaveQRCode(*args):
    data = text_input.get()
    if data:
        image = qrcode.make(data)  # generate QRcode
        resized_img = image.resize((280, 250))  # reszie QR Code Size

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
        )
        if path:
            resized_img.save(path)
            messagebox.showinfo(
                title="QR Saved", message="Your QR code has been saved successfully"
            )
    else:
        messagebox.showwarning(
            title="Invalid Input", message="Please give a valid input"
        )


# part of code for GUI

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x400")
root.config(bg="white")
root.resizable(0, 0)


frame1 = tk.Frame(root, bd=2, relief="raised")
frame1.place(x=10, y=5, height=250, width=280)

frame2 = tk.Frame(root, bd=2, relief="sunken")
frame2.place(x=10, y=260, height=100, width=280)

coverImg = tk.PhotoImage(
    file="C:/Users/Jai/OneDrive/Desktop/Python Miniproject/qrCodeCover.png"
)


qr_canvas = tk.Canvas(frame1)
qr_canvas.bind("<Double-1>", SaveQRCode)
qr_canvas.create_image(0, 0, anchor=tk.NW, image=coverImg)
qr_canvas.image = coverImg
qr_canvas.pack(fill=tk.BOTH)

text_input = ttk.Entry(
    frame2, width=37, font=("Times New Roman", 11), justify=tk.CENTER
)
text_input.bind("<Return>", GenerateQRCode)
text_input.place(x=5, y=5)

button_1 = ttk.Button(frame2, text="Generate", width=10, command=GenerateQRCode)
button_1.place(x=25, y=50)

button_2 = ttk.Button(frame2, text="Save", width=10, command=SaveQRCode)
button_2.place(x=100, y=50)

button_3 = ttk.Button(frame2, text="Exit", width=10, command=root.destroy)
button_3.place(x=175, y=50)

root.mainloop()
