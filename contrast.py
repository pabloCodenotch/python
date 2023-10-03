import cv2 as cv
import tkinter as tk
import tkinter.filedialog as fd

root = tk.Tk()
root.title('Herramienta del Equipo VOX')

file = []

def select_file():
    file_path = fd.askopenfilename()
    file.append(file_path)

def convert_file():
    image1 = cv.imread(file[0])
    window_name = 'Original'
    cv.imshow(window_name, image1)

    grey_img = cv.cvtColor(image1,cv.COLOR_BGR2GRAY)
    invert = cv.bitwise_not(grey_img)

    blur = cv.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv.bitwise_not(blur)
    sketch = cv.divide(grey_img, invertedblur, scale=256)

    cv.imwrite('sketch.png', sketch)

    image = cv.imread('sketch.png')

    window_name = 'Sketch image'
    cv.imshow(window_name, image)
    cv.waitKey(0)


tk.Button(text= ('Open'), command= select_file).pack(fill=tk.X)
tk.Button(text=('Sketch'),command=convert_file ).pack(fill=tk.X)

tk.mainloop()