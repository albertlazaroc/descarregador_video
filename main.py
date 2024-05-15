import tkinter as tk
import customtkinter
from pytube import YouTube

# Funcion para descargar el video
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Descarregat!")
        
        # Mostrar información del video
        description_label.configure(text=
                                         f"Autor: {ytObject.author}\n"
                                         f"Durada: {ytObject.length} segundos")
    except Exception as e:
        finishLabel.configure(text="Error de Descarrega", text_color="red")

# Funcion barra y porcentaje
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text= per + "%")
    pPercentage.update()

    #Actualizar barra de progreso
    progressBar.set(float(percentage_of_completion) / 100)

# Color de la GUI
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("green")

# Main frame de la GUI
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Albert Lazaro Descarregador de videos de youtube")

# Titulo YT
title = customtkinter.CTkLabel(app, text="Posar YT link")
title.pack(padx=10, pady=10)

# Campo de entrada para que el usuario ingrese el enlace de YouTube
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Estado de la descarga
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Mostrar porcentaje
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Boton descarga
download = customtkinter.CTkButton(app, text="Descarregar", command=startDownload)
download.pack(padx=10, pady=10)

# Campo de texto para la descripción del video
description_label = customtkinter.CTkLabel(app, text="", wraplength=600)
description_label.pack(padx=10, pady=10)

# Run app
app.mainloop()