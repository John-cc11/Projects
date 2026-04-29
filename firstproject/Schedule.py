import customtkinter as ctk
import calendar
from datetime import datetime




#===============================Scheduling 

class SchedulingPage:
   def __init__(self, parent):
         self.frame =ctk.CTkFrame(parent, fg_color="#ffffff")
         self.frame.grid(row=0, column=1, sticky="nsew")

         self.frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
         self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

         label = ctk.CTkLabel(
            self.frame,
            text="Scheduling",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827"
        )

         label.grid(row=0, column=0, sticky="n",pady=(20, 10))

          #===== scheduling boxes 
         
       






        



      