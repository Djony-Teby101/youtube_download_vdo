import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink= link.get()
        ytObject=YouTube(ytLink, on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="black")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Telechargement complet !",text_color="green")

    except:
        finishLabel.configure(text="Erreur lors du telechargement",text_color="red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size=stream.filesize
    bytes_download=total_size - bytes_remaining
    pourcentage_of_completion=bytes_download/total_size*100
    per= str(int(pourcentage_of_completion))
    percentage.configure(text=per +'%')
    percentage.update()

    #modification de la barre.
    progessBar.set(float(pourcentage_of_completion)/100)




#parametre du systeme

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# notre fenetre.
app= customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube download")

#ajouter les elements de l'UI.
title= customtkinter.CTkLabel(app, text='Inserer le lien de video:')
title.pack(padx=10, pady=10)

#lien de l'entree.
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#UI telechargement terminer.
finishLabel=customtkinter.CTkLabel(app, text="")
finishLabel.pack()

####barre de telechargement.
percentage=customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progessBar=customtkinter.CTkProgressBar(app, width=400)
progessBar.set(0)
progessBar.pack(padx=10, pady=10)



#Button de telechargement.
download=customtkinter.CTkButton(app, text="Telecharger", command=startDownload)
download.pack(padx=3,pady=3)


#lancer l'app.
app.mainloop()
