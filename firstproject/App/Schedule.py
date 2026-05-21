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

   
         self.day_buttons = {}
         self.boxes = {}
         self.today = datetime.now().date()

         self.Scheduling_label = ctk.CTkLabel(
            self.frame,
            text="Scheduling",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827"
        )
         

         self.Scheduling_label.grid(row=0, column=0, columnspan=4, sticky="n", pady=(20, 10))

         #================ calendar ==========
         sched_boxes = [
            {"name": "calendar", "color": "#fdc8c8", "row": 1, "col": 2, "columnspan": 7, "rowspan": 6},
            {"name": "schedule", "color": "#f1d9d9", "row": 1, "col": 0, "columnspan": 2, "rowspan": 6},
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


               self.boxes[b["name"]] = card



#====================== calendar 

   

         self.calendar_frame = self.boxes["calendar"]
         self.calendar_frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
         self.calendar_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
         
         self.current_year = datetime.now().year
         self.current_month = datetime.now().month

   
         
#=================================== month drop down 
         header_frame = ctk.CTkFrame(self.calendar_frame, fg_color="transparent")
         header_frame.grid(row=0, column=0, columnspan=7, pady=10, sticky="w")
         header_frame.grid_columnconfigure(0, weight=0)
         header_frame.grid_columnconfigure(1, weight=0)
        

         self.month_var = ctk.StringVar(value=calendar.month_name[self.current_month])
         self.year_var = ctk.StringVar(value=str(self.current_year))

         month_menu = ctk.CTkOptionMenu(
              header_frame,
              values=list(calendar.month_name)[1:],
              variable=self.month_var,
              command=self.change_date
              
              
         )
         month_menu.grid(row=0, column=0, padx=5, pady=10)

         year_menu = ctk.CTkOptionMenu(
               header_frame,
               values=[str(y) for y in range(self.current_year - 5, self.current_year + 6)],
               variable=self.year_var,
               width=80,
               command=self.change_date
            
               
         )

         year_menu.grid(row=0, column=1, padx=5, pady=10)

         days = ["Mon", "Tue", "Wed", "Thu" , "Fri", "Sat", "Sun"]

         for col, day in enumerate(days):
            lbl = ctk.CTkLabel(
                self.calendar_frame,
                text= day,
                font=("Segoe UI", 12, "bold")

            )

            lbl.grid(row=1, column=col, pady=5)


         cal = calendar.Calendar()
         month_days = cal.monthdatescalendar(self.current_year, self.current_month)

         for row, week in enumerate(month_days, start=2):
            for col, day in enumerate(week):

               is_current = (day.month == self.current_month)

               if is_current:
                     fg_color = "#F3F4F6"
                     text_color = "#111827"
               else:
                     fg_color = "#E5E7EB"
                     text_color = "#9CA3AF"

               btn = ctk.CTkButton(
                     self.calendar_frame,
                     text=str(day.day),
                     width=40,
                     height=40,
                     fg_color=fg_color,
                     text_color=text_color,
                     hover_color="#E5E7EB",
                     corner_radius=10,
                     anchor="nw"
               )

               btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

               self.day_buttons[(row, col)] = btn
               self.update_calendar()
                  
   
   def change_date(self, value):

      self.current_month = list(calendar.month_name).index(
        self.month_var.get()
    )

      self.current_year = int(
         self.year_var.get()
    )
      self.calendar_frame.after(50, self.update_calendar)

  
   def refresh_today(self):
    self.today = datetime.now().date()


   def update_calendar(self):

      self.refresh_today()

      for key, btn in self.day_buttons.items():
        btn.configure(
            text="",
            fg_color="#E5E7EB",
            text_color="#9CA3AF"
        )

      cal = calendar.Calendar()
      month_days = cal.monthdatescalendar(
          self.current_year, 
          self.current_month)

      for row, week in enumerate(month_days, start=2):
        for col, day in enumerate(week):


            btn = self.day_buttons.get((row, col))
            if not btn:
                continue

            is_today = (day == self.today)
            is_current = (day.month == self.current_month)

            if is_today:
                fg_color = "#3B82F6"
                text_color = "white"

            elif is_current:
                fg_color = "#F3F4F6"
                text_color = "#111827"

            else:
                fg_color = "#E5E7EB"
                text_color = "#9CA3AF"

            btn.configure(
                text=str(day.day),
                fg_color=fg_color,
                text_color=text_color
            )



#======================= <> bar 
      
            
         



         
      





        



      