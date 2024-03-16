import tkinter
import customtkinter
from pytube import YouTube

# get ur heart
def startDownload():
    try:
        ytLink = link.get()
        print(f"Attempting to download: {ytLink}")
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        print(f"Selected video resolution: {video.resolution}")
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure()
        download_path = '/home/anuusz/Downloads/ttkbootstrap'  #ubah anuusz menjadi nama pc/akun pc anda
        print(f"Download path: {download_path}")
        video.download(download_path)
        finishLabel.configure(text="Download Complete!, Check your File Manager.")
    except Exception as e:
        finishLabel.configure(text="Download Eror", text_color="red")

def on_progress(streams, chunk, bytes_remaining):
    total_size = streams.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

# progress bar
    progressbar.set(float(percentage_of_compeletion) / 100 )

# buat setting temar
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# ini frame
app = customtkinter.CTk()
app.geometry("640x360")
app.title("YouTube Downloader")

# UI bukan bukan almet kuning
title = customtkinter.CTkLabel(app, text="Insert link")
title.pack(padx=10, pady=10)

# input golput
url_var= tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=320, height=25, textvariable=url_var)
link.pack()

# download selesai bukan hubungan
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# bar H club
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# tombol download xxx
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# jalanin aja dulu
app.mainloop()