import customtkinter as ctk
import calendar
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Utils.json_shortcut import load_json, add_data,update_data, remove_data

data = load_json("sched.json")

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
         #for sched window
        self.schedule_data = data if data else {}

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
               #lock 
               self.frame.grid_propagate(False)


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

         
#=================================== month 
        header_frame = ctk.CTkFrame(
            self.calendar_frame, 
            fg_color="transparent")
        header_frame.grid(row=0, column=0, columnspan=7, pady=10, sticky="w")
        header_frame.grid_columnconfigure(0, weight=0)
        header_frame.grid_columnconfigure(1, weight=0)
        header_frame.grid_columnconfigure(3, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)
        
        self.today_btn = ctk.CTkButton(
            header_frame,
            text="Today",
            width=90,
            height=36,
            corner_radius=18,   # half of height = oval shape
            fg_color="#3B82F6",
            hover_color="#2563EB",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            command=self.go_to_today
        ).grid(row=0, column=3, padx=(15, 5))


        
        self.next_month_btn = ctk.CTkButton(
            header_frame,
            text="▶",
            width=40,
            height=40,
            fg_color="transparent",
            hover=False,
            anchor="n",
            text_color="#000000",
            font=("Segoe UI", 20),
            command=self.next_month
        ).grid(row=0, column=6, padx=2)




        self.prev_month= ctk.CTkButton(
            header_frame,
            text="◀",
            width=40,
            height=40,
            fg_color="transparent",
            hover=False,
            anchor="n",
            text_color="#000000",
            font=("Segoe UI", 20),
            command=self.prev_month
        ).grid(row=0, column=4, padx=(0,10))

        self.months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        
        self.month_label = ctk.CTkLabel(
            header_frame,
            text=self.months[self.current_month - 1],
            font=("Segoe UI", 20, "bold"),
            text_color="#000000"
        )

        self.month_label.grid(row=0, column=5, padx=10)

   
      

        days = ["Mon", "Tue", "Wed", "Thu" , "Fri", "Sat", "Sun"]

        for col, day in enumerate(days):
            lbl = ctk.CTkLabel(
                self.calendar_frame,
                text= day,
                font=("Segoe UI", 12, "bold")

            ).grid(row=1, column=col, pady=5)

     


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
                     anchor="nw",
                     command=lambda d=day: self.create_schedule(d)
               )    

               btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
               btn.date = day
               self.day_buttons[(row, col)] = btn
               self.update_calendar()

      #===================================== month func
    def next_month(self):
        self.current_month += 1

        if self.current_month > 12:
            self.current_month = 1
        

        self.month_label.configure(
            text=self.months[self.current_month - 1]
        
        )
        self.update_calendar()


    def prev_month(self):
        self.current_month -= 1

        if self.current_month < 1:
            self.current_month = 12

        self.month_label.configure(
            text=self.months[self.current_month - 1]
        )   
        self.update_calendar()


    def go_to_today(self):

        today = datetime.now()

        self.current_month = today.month
        self.current_year = today.year

        self.month_label.configure(
            text=self.months[self.current_month - 1]
        )

        self.update_calendar()          
#
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


# create schedule window / for schedule window

    
    def create_schedule(self, day):
        if self.preview_frame and self.preview_frame.winfo_exists():
                self.preview_frame.destroy()


        self.schedule_window = ctk.CTkFrame(
            self.frame,
            fg_color="#FFFFFF",
            corner_radius=15,
            border_width=1,
            border_color="#E5E7EB",
            width=350,
            height=400
        )


        self.schedule_window.grid_propagate(False)

        self.schedule_window.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )



        self.schedule_window.grid_columnconfigure(0, weight=1)
        self.schedule_window.grid_columnconfigure(1, weight=1)
        
        self.schedule_window.grid_rowconfigure(0, weight=0)
        self.schedule_window.grid_rowconfigure(1, weight=0)
        self.schedule_window.grid_rowconfigure(2, weight=0)
        self.schedule_window.grid_rowconfigure(3, weight=0)
        self.schedule_window.grid_rowconfigure(4, weight=1)
        self.schedule_window.grid_rowconfigure(5, weight=0) 

        top_frame = ctk.CTkFrame(
        self.schedule_window,
        fg_color="transparent"
    )

        top_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=15,
            pady=(15, 10)
        )

        top_frame.grid_columnconfigure(0, weight=1)
       
        date_form = ctk.CTkLabel(
        top_frame,
        text_color="#000000",
        text=day.strftime("%B %d, %Y"),
        font=("Segoe UI", 20, "bold"),
        width=180,
        
    )

        date_form.grid(
            row=0,
            column=0,
            sticky="w",
            
        )
#title Entry
        self.title_entry = ctk.CTkEntry(
            self.schedule_window,
            placeholder_text="Title",
            fg_color="#FFFFFF",
            text_color="#000000",
            border_color="#E5E7EB"

        )
        self.title_entry.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=15,
            pady=10,
            sticky="ew"
        )   
# time entry
        self.time_entry = ctk.CTkEntry(
        self.schedule_window,
        placeholder_text="Time (e.g. 3:00 PM)",
        fg_color="#FFFFFF",
        text_color="#000000",
        border_color="#E5E7EB"
            )

        self.time_entry.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=15,
            pady=5,
            sticky="ew"
        )

       

# Priority &  category dropdown menu
        priority = ["-- Select Priority --", "Low", "Medium", "High", "Urgent"]
        category = ["-- Select Category --","School", "Work", "Personal", "Health", "Finance", "Other"]

        self.priority_var = ctk.StringVar(value=priority[0])
        self.category_var = ctk.StringVar(value=category[0])

        priority_menu = ctk.CTkComboBox(
            self.schedule_window,
            values=priority,
            variable=self.priority_var,
            state="readonly",
            fg_color="#FFFFFF",
            border_color="#E5E7EB",
            button_color="#3B82F6",
            text_color="#000000",
            dropdown_fg_color="#FFFFFF",
            dropdown_text_color="#111827",
            dropdown_hover_color="#E5E7EB",
            hover=False,
            width=150
  
        )

        category_menu = ctk.CTkComboBox(
            self.schedule_window,
            values=category,
            variable=self.category_var,
            state="readonly",
            fg_color="#FFFFFF",
            border_color="#E5E7EB",
            button_color="#3B82F6",
            text_color="#000000",
            dropdown_fg_color="#FFFFFF",
            dropdown_text_color="#111827",
            dropdown_hover_color="#E5E7EB",
            hover=False,
            width=150

        )

        priority_menu.grid(
            row=3,
            column=0,
            padx=(15, 5),
            pady=5,
            sticky="w"
        )

        category_menu.grid(
            row=3,
            column=0,
            padx=(180, 15),
            columnspan=4,
            pady=5,
            sticky="w"
        )
        
                # ================= TEXTBOX =================


        
        self.schedule_textbox = ctk.CTkTextbox(
                self.schedule_window,
                fg_color="#F3F4F6",
                text_color="#000000",
                corner_radius=12,
                height=120
        )

        self.schedule_textbox.grid(
                row=4,
                column=0,
                columnspan=2,
                padx=15,
                pady=10,
                sticky="nsew"
        )
        




        # ================= SAVE BUTTON =================

        save_btn = ctk.CTkButton(
            self.schedule_window,
            text="Save Schedule",
            height=30,
            corner_radius=12,
            fg_color="#3B82F6",
            hover_color="#2563EB"
        )

        save_btn.grid(
            row=5,
            column=0,
            columnspan=4,
            padx=15,
            pady=(0, 15),
            sticky="ew"
        )
         # ================= CLOSE BUTTON =================

        close_btn = ctk.CTkButton(
            top_frame,
            text="✕",
            width=35,
            height=35,
            corner_radius=10, 
            fg_color="#F3F4F6",
            hover_color="#E5E7EB",
            text_color="#111827",
            command=self.schedule_window.destroy

        )

        close_btn.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(0, 5)
        )
            

       



#======================= <> bar 
      
            
         



         
      





        



      