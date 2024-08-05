import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageChops

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

uploaded_images = [None, None]

def create_blank_image(size=(250, 250), color=(255, 255, 255)):
    return Image.new("RGB", size, color)

def upload_photo(label_img, index):
    file_path = filedialog.askopenfilename(
        title="Select a Photo",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")]
    )
    if file_path:
        try:
            img = Image.open(file_path)
            img = img.resize((250, 250), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            
            label_img.config(image=img_tk)
            label_img.image = img_tk
            uploaded_images[index] = img
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open image: {e}")

def show_difference(label_img):
    if uploaded_images[0] and uploaded_images[1]:
        try:
            diff = ImageChops.difference(uploaded_images[0], uploaded_images[1])
            if diff.getbbox():
                diff = diff.resize((250, 250), Image.LANCZOS)
                diff_tk = ImageTk.PhotoImage(diff)
                label_img.config(image=diff_tk)
                label_img.image = diff_tk
            else:
                messagebox.showinfo("Info", "The images are identical.")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to compare images: {e}")
    else:
        messagebox.showwarning("Warning", "Please upload both images before comparing.")

root = tk.Tk()
root.title("Photo Upload and Compare")
root.config(padx=100,pady=50,bg=GREEN)
root.minsize(width=600,height=400)

blank_image = create_blank_image()
blank_image_tk = ImageTk.PhotoImage(blank_image)

label_img1 = tk.Label(root,image=blank_image_tk)
label_img1.grid(row=1, column=0)
button_upload1 = tk.Button(root, text="Upload Photo 1", command=lambda: upload_photo(label_img1, 0))
button_upload1.grid(row=0, column=0)

label_img2 = tk.Label(root,image=blank_image_tk)
label_img2.grid(row=1, column=1)
button_upload2 = tk.Button(root, text="Upload Photo 2", command=lambda: upload_photo(label_img2, 1))
button_upload2.grid(row=0, column=1)

label_img_diff = tk.Label(root,image=blank_image_tk)
label_img_diff.grid(row=1, column=2)
button_compare = tk.Button(root, text="Compare Photos", command=lambda: show_difference(label_img_diff))
button_compare.grid(row=0, column=2)

root.mainloop()
