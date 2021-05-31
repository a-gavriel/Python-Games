from tkinter import *
from tkinter import messagebox, filedialog
import os
from urllib.request import urlopen, HTTPError, URLError
import _thread

fln = ""
filesize = ""
def startDownload():
  global fln
  fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="save File", filetypes=(("JPG IMAGE FILE", "*.jpg"), \
    ("PNG FILES", "*.png"), ("ALL FILES", "*.*")))
  filename.set(os.path.basename(fln))
  _thread.start_new_thread(initDownload, ())

def initDownload():
  global filesize
  furl = url.get()
  target = urlopen(furl)
  meta = target.info()
  filesize = float((meta['Content-Length']))
  filesize_mb = round((filesize / 1024 / 1024), 2)
  downloaded = 0
  chunks = 1024 * 5
  with open(fln, "wb") as f:
    while True:
      parts = target.read(chunks)
      if not parts:
        messagebox.showinfo("Download Complete","Your Download has been completed successfully")
        break
      downloaded += chunks
      download_progress.set(str(downloaded)+" MB /" + str(filesize_mb)+" MB")
      download_percentage.set(str(round(downloaded/filesize*100,2))+"%")
      f.write(parts)
  f.close()

def exitProg():
  if messagebox.askyesno(" exit program?"," are you sure you want to exit the rpogram?") == False:
    return False
  exit()

root = Tk()
url = StringVar()
filename = StringVar()
download_progress = StringVar()
download_percentage = StringVar()

download_progress.set("N/A")
download_percentage.set("N/A")

wrapper = LabelFrame(root, text="fileURL")
wrapper.pack(fill="both",expand="yes",padx=10,pady=10)


wrapper2 = LabelFrame(root, text="Download Info")
wrapper2.pack(fill="both",expand="yes",padx=10,pady=10)

lbl = Label(wrapper, text=" Download URL: ")
lbl.grid(row=0, column =0, padx = 10, pady=10)
ent = Entry(wrapper, textvariable=url)
ent.grid(row=0, column= 0, padx = 5, pady=10 )
btn = Button(wrapper, text=" download", command=startDownload)
btn.grid(row = 0, column=2, padx=5, pady=10)
root.geometry("450x400")
root.mainloop()









