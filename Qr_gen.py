import tkinter as tk
import pyqrcode

root = tk.Tk()
root.title("Zp's QR Gen") # Provide Tittle
root.geometry("250x300")

url_label = tk.Label(root, text="Enter your URL: ") # provide URL
url_entry = tk.Entry(root) 

def generateQR():
    url = url_entry.get() # get url from entry box
    qr = pyqrcode.create(url) # create a QR code for the given url
    qr.png("QR.png", scale= 8) # save the qr
    qr_image = tk.PhotoImage(file="QR.png") # load qr code image into tkinter photoimage object

    qr_label = tk.Label(root, image= qr_image) # display qr code image
    qr_label.image = qr_image # keep reference of image to prevent garbage
    qr_label.pack()

generate = tk.Button(root, text= "Generate", command= generateQR) # create a button

# place widgets in window
url_label.pack()
url_entry.pack()
generate.pack()

root.mainloop()