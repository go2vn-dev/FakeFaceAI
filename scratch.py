import tkinter as tk
from pathlib import Path
from PIL import Image

window = tk.Tk()

#code here
window.title('Display an Image')
window.configure(background='grey')

path = Path("C:/Python/voham.png")

img = tk.PhotoImage(file=path)
image1 = Image.open(path)

#Size of the image
width, height = image1.size
print(width)
print()
print(height)

#window.size(width, height)
label = tk.Label(image=img)
label.pack()
# Code ends
window.mainloop()





