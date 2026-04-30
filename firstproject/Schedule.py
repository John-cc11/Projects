import customtkinter as ctk
import calendar
from datetime import datetime




#===============================Scheduling 

class SchedulingPage:
   def __init__(self, parent):
         self.frame =ctk.CTkFrame(parent, fg_color="#ffffff")
         self.frame.grid(row=0, column=1, sticky="nsew")

         self.frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
         self.frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

         label = ctk.CTkLabel(
            self.frame,
            text="Scheduling",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827"
        )

         label.grid(row=0, column=0, sticky="n",pady=(20, 10))

         #================ calendar ==========
         self.current_year = datetime.now().year
         self.current_month = datetime.now().month
         

         self.header = ctk.CTkLabel(
              self.frame,
              text=f"{calendar.month_name[self.current_month]} {self.current_year}",
              font=("Segoe UI", 20, "bold"),
              text_color="#ffffff"
         )

         days = ["Mon", "Tue", "Wed", "Thu" , "Fri", "Sat", "Sun"]

         for col, day in enumerate(days):
            lbl = ctk.CTkLabel(
                self.frame,
                text= day,
                font=("Segoe UI", 12, "bold")

            )

            lbl.grid(row=2, column=col, pady=5)


         cal = calendar.monthcalendar(self.current_year, self.current_month)


         for row, week in enumerate(cal, start=3):
             for col, day in enumerate(week):
                  if day == 0:
                     continue
                  btn = ctk.CTkButton(
                     self.frame,
                     text=str(day),
                     width=40,
                     height=40,
                     fg_color="#F3F4F6",
                     text_color="#111827",
                     hover_color="#E5E7EB",
                     corner_radius=10
                                 )
               
                  btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")






        



      