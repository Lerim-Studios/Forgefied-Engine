import customtkinter as ctk
import os
import tkinter as tk
from tkinter import font

app = ctk.CTk()
fullscreen = True
app.attributes("-fullscreen", fullscreen)
app.title("Craftix os")

vcr_font = ctk.CTkFont("Better VCR", 14)

def close_app():
    os._exit(0)

bottomcontrols = ctk.CTkFrame(app, fg_color="black")
bottomcontrols.pack(fill="x", side="bottom")

mainframe = ctk.CTkFrame(app, bg_color="red")
mainframe.pack(fill="both")

closebutton = ctk.CTkButton(bottomcontrols, border_color="white", border_width=2, corner_radius=10, width=30, height=30, text="X", fg_color="Black", hover_color="darkred", command=close_app)
closebutton.pack(side="left", pady=2, padx=2)

app_title = ctk.CTkLabel(bottomcontrols, text="Craftix OS", font=vcr_font)
app_title.pack(side="left", padx=10)

app.mainloop()