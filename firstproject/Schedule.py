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

         self.boxes = {}

         self.Scheduling_label = ctk.CTkLabel(
            self.frame,
            text="Scheduling",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827"
        )
         

         self.Scheduling_label.grid(row=0, column=0, columnspan=4, sticky="n", pady=(20, 10))

         #================ calendar ==========
         sched_boxes = [
            {"name": "calendar", "color": "#fdc8c8", "row": 1, "col": 0, "columnspan": 7, "rowspan": 6},
            {"name": "schedule", "color": "#f1d9d9", "row": 1, "col": 7, "columnspan": 1, "rowspan": 6},
        ]
      

         for b in sched_boxes:
               shadow = ctk.CTkFrame(
                  self.frame,  
                  fg_color="#E5E7EB",
                  corner_radius=20
               )
               shadow.grid(
                  row=b["row"],
                  column=b["col"],
                  rowspan=b.get("rowspan", 1),
                  columnspan=b.get("columnspan", 1),
                  padx=5,
                  pady=5,
                  sticky="nsew"
               )
               shadow.grid_rowconfigure(0, weight=1)
               shadow.grid_columnconfigure(0, weight=1)

               card = ctk.CTkFrame(
                  shadow,
                  fg_color="#F9FAFB",
                  corner_radius=10
               )
               card.grid(row=0, column=0, sticky="nsew")

               accent = ctk.CTkFrame(
                  card,
                  fg_color=b["color"],
                  height=10,
                  corner_radius=10
               )
               accent.grid(row=0, column=0, columnspan=7, sticky="ew", padx=15, pady=(10, 5))
               self.boxes[b["name"]] = card
#====================== calendar 
         calendar_frame = self.boxes["calendar"]
         calendar_frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
         calendar_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
         
         self.current_year = datetime.now().year
         self.current_month = datetime.now().month
         

         self.header = ctk.CTkLabel(
              calendar_frame,
              text=f"{calendar.month_name[self.current_month]} {self.current_year}",
              font=("Segoe UI", 20, "bold"),
              text_color="#180b0b"
         )
         self.header.grid(row=0, column=0, columnspan=7, pady=10)

         days = ["Mon", "Tue", "Wed", "Thu" , "Fri", "Sat", "Sun"]

         for col, day in enumerate(days):
            lbl = ctk.CTkLabel(
                calendar_frame,
                text= day,
                font=("Segoe UI", 12, "bold")

            )

            lbl.grid(row=1, column=col, pady=5)


         cal = calendar.monthcalendar(self.current_year, self.current_month)


         for row, week in enumerate(cal, start=2):
             for col, day in enumerate(week):
                  if day == 0:
                     continue
                  btn = ctk.CTkButton(
                     calendar_frame,
                     text=str(day),
                     width=40,
                     height=40,
                     fg_color="#F3F4F6",
                     text_color="#111827",
                     hover_color="#E5E7EB",
                     corner_radius=10
                                 )
               
                  btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


            
         



         
      





        



      