import customtkinter as ctk
import tkinter as tk
import calendar
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Utils.database_func import load_schedule,delete_schedule,save_schedule



#===============================Scheduling 

class SchedulingPage:
    def __init__(self, parent):
        self.frame =ctk.CTkFrame(parent, fg_color="#ffffff")
        self.frame.grid(row=0, column=1, sticky="nsew")

        self.frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)

        self.day_buttons = {}
        self.preview_frame = None

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
            {"name": "calendar", "color": "#fdc8c8", "row": 1, "col": 1, "columnspan": 7, "rowspan": 6},
            {"name": "schedule", "color": "#f1d9d9", "row": 1, "col": 0, "columnspan": 1, "rowspan": 6},
        ]
      
        self.frame.grid_propagate(False)

        for b in sched_boxes:
               shadow = ctk.CTkFrame(
                  self.frame,  
                  fg_color="#E5E7EB",
                  corner_radius=20
               )
               #lock 
              


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
#================================= schedule 
        schedules = load_schedule()

        self.schedule_dates = {}

        for schedule in schedules:

            id, title, content, date, time, priority, category, completed = schedule

            if date not in self.schedule_dates:
                self.schedule_dates[date] = 0

            self.schedule_dates[date] += 1
       

        
        # =========================================
        # SCHEDULE FRAME
        # =========================================

        self.schedule_frame = self.boxes["schedule"]

        # grid layout
        self.schedule_frame.grid_rowconfigure(0, weight=1)
        self.schedule_frame.grid_columnconfigure(0, weight=1)

        # =========================================
        # CANVAS
        # =========================================

        self.canvas = tk.Canvas(
            self.schedule_frame,
            highlightthickness=0,
            bg="#F9FAFB"
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        

        # =========================================
        # SCROLLBAR
        # =========================================

        self.scrollbar = ctk.CTkScrollbar(
            self.schedule_frame,
            orientation="vertical",
            command=self.canvas.yview
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        # =========================================
        # SCROLLABLE FRAME
        # =========================================

        self.scrollable_frame = ctk.CTkFrame(
            self.canvas,
            fg_color="transparent"
        )

        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )

    
        def on_frame_configure(event):

            self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )

          

        self.scrollable_frame.bind(
            "<Configure>",
            on_frame_configure
        )
        # =========================================
# SMOOTH MOUSEWHEEL SCROLL
# =========================================

        self.scroll_animation = 0

        def smooth_scroll():

            if self.scroll_animation != 0:

                self.canvas.yview_moveto(
                    self.canvas.yview()[0] + (self.scroll_animation * 0.01)
                )

                self.scroll_animation *= 0.85

            
                if abs(self.scroll_animation) < 0.1:
                    self.scroll_animation = 0
                    return

                self.frame.after(15, smooth_scroll)

        def on_mousewheel(event):

            delta = 0

            if event.delta:
                delta = event.delta / 120

            self.scroll_animation += -delta * 1.5

            smooth_scroll()

        def bind_mousewheel(event):
            self.canvas.bind("<MouseWheel>", on_mousewheel)

        def unbind_mousewheel(event):
            self.canvas.unbind("<MouseWheel>")

        self.scrollable_frame.bind(
            "<Enter>",
            bind_mousewheel
        )

        self.scrollable_frame.bind(
            "<Leave>",
            unbind_mousewheel
        )



        # =========================================
        # RESIZE INNER FRAME
        # =========================================

        def on_canvas_resize(event):
            self.canvas.itemconfig(
                self.canvas_window,
                width=event.width
            )
            self.canvas.configure(
                    scrollregion=self.canvas.bbox("all")
                
            )
        self.canvas.bind(
            "<Configure>",
            on_canvas_resize
        )

        # =========================================
        # SCHEDULE CARDS
        # =========================================

        for index, schedule in enumerate(schedules):
            id, title, content, date, time, priority, category, completed = schedule

            

            card = ctk.CTkFrame(
                self.scrollable_frame,
                fg_color="#FFFFFF",
                corner_radius=15
            )

            card.grid(
                row=index,
                column=0,
                sticky="ew",
                padx=10,
                pady=5
            )

            card.grid_columnconfigure(0, weight=1)

            # ================= TITLE =================

            title = ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 18, "bold")
            )

            title.grid(
                row=0,
                column=0,
                sticky="w",
                padx=10,
                pady=(10, 0)
            )

            # ==================================
            #               Content
            # ==================================

            content = ctk.CTkLabel(
                card,
                text=content,
                font=("Arial", 14),
                text_color="gray"
            )

            content.grid(
                row=1,
                column=0,
                sticky="w",
                padx=10
            )

            # ==================================
            #       DATE TIME
            # ==================================

            datetime_sched = ctk.CTkLabel(
                card,
                text=f'{date} • {time}',
                font=("Arial", 12)
            )

            datetime_sched.grid(
                row=2,
                column=0,
                sticky="w",
                padx=10,
                pady=(5, 0)
            )

            # ==================================
            #                INFO 
            # ==================================

            info = ctk.CTkLabel(
                card,
                text=f'Priority: {priority} | Category: {category}',
                font=("Arial", 12),
                text_color="gray"
            )

            info.grid(
                row=3,
                column=0,
                sticky="w",
                padx=10,
                pady=(0, 10)
            ) 
            card.bind("<MouseWheel>", on_mousewheel)
            title.bind("<MouseWheel>", on_mousewheel)
            content.bind("<MouseWheel>", on_mousewheel)
            datetime_sched.bind("<MouseWheel>", on_mousewheel)
            info.bind("<MouseWheel>", on_mousewheel)
            



        #==================================
        #               calendar
        #==================================
        

   

        self.calendar_frame = self.boxes["calendar"]
        self.calendar_frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.calendar_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.calendar_frame.grid_columnconfigure(0, weight=1)
         
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

         
        #==================================
        #           month
        #==================================
        header_frame = ctk.CTkFrame(
        self.calendar_frame, 
        fg_color="transparent")
        header_frame.grid(row=0, column=0, columnspan=7, pady=10, sticky="ew")
        header_frame.grid_columnconfigure(0, weight=0)
        header_frame.grid_columnconfigure(1, weight=0)
        header_frame.grid_columnconfigure(6, weight=1)
       
        
        self.today_btn = ctk.CTkButton(
            header_frame,
            text="Today",
            width=90,
            height=36,
            corner_radius=18,   
            fg_color="#3B82F6",
            hover_color="#2563EB",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            command=self.go_to_today
        ).grid(row=0, column=0, padx=(15, 15), sticky="e")

        
        
        self.next_month_btn = ctk.CTkButton(
            header_frame,
            text="▶",
            width=1,
            height=28,
            fg_color="transparent",
            hover=False,
            anchor="n",
            text_color="#000000",
            font=("Segoe UI", 18),
            command=self.next_month
        ).grid(row=0, column=5)




        self.prev_month = ctk.CTkButton(
            header_frame,
            text="◀",
            width=1,
            anchor="n",
            height=28,
            fg_color="transparent",
            hover=False,
            text_color="#000000",
            font=("Segoe UI", 16),
            command=self.prev_month
        ).grid(row=0, column=1, padx=(0,0))

   

        self.months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        
        self.month_label = ctk.CTkLabel(
            header_frame,
            text=self.months[self.current_month - 1],
            font=("Segoe UI", 20, "bold"),
            width=200,
            text_color="#000000"
        )

        self.month_label.grid(row=0, column=3)


        self.year_button = ctk.CTkButton(
            header_frame,
            text=str(self.current_year),
            width=70,
            text_color="#000000",
            fg_color="transparent",
            hover=False,
            font=("Segoe UI", 20, "bold")
  
        )
       
        self.year_button.grid(row=0, column=8, padx=(0,10),sticky="w")

       

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

        

      #=====================================
      #         month func
      #=====================================

    

#------------------------------

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

            formatted_day = day.strftime("%B %d, %Y")

            count = self.schedule_dates.get(formatted_day, 0)

            display_text = str(day.day)

            if count > 0:
                display_text = f"{day.day}\n• {count}"

            btn.configure(
                text=display_text,
                fg_color=fg_color,
                text_color=text_color
            )

           

#==========================================================================
# create schedule window / for schedule window
#=========================================================================

    
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

        self.top_frame = ctk.CTkFrame(
        self.schedule_window,
        fg_color="transparent"
    )

        self.top_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=15,
            pady=(15, 10)
        )

        self.top_frame.grid_columnconfigure(0, weight=1)
       
        self.date_form = ctk.CTkLabel(
        self.top_frame,
        text_color="#000000",
        text=day.strftime("%B %d, %Y"),
        font=("Segoe UI", 20, "bold"),
        width=180,
        
    )

        self.date_form.grid(
            row=0,
            column=0,
            sticky="w",
            
        )
        #=====================================
        #title Entry
        #=====================================
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
        #===================================== 
        # time entry
        #=====================================
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

       
        #=====================================
        # Priority &  category dropdown menu
        #=====================================
        priority = ["-- Select Priority --", "Low", "Medium", "High", "Urgent"]
        category = ["-- Select Category --","School", "Work", "Personal", "Health", "Finance", "Other"]

        self.priority_var = ctk.StringVar(value=priority[0])
        self.category_var = ctk.StringVar(value=category[0])

        self.priority_menu = ctk.CTkComboBox(
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

        self.category_menu = ctk.CTkComboBox(
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

        self.priority_menu.grid(
            row=3,
            column=0,
            padx=(15, 5),
            pady=5,
            sticky="w"
        )

        self.category_menu.grid(
            row=3,
            column=0,
            padx=(180, 15),
            columnspan=4,
            pady=5,
            sticky="w"
        )
        #=====================================
              #  TEXTBOX 
        #=====================================


        
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
        
    
    


        #=====================================
        #           SAVE BUTTON 
        #=====================================

        save_btn = ctk.CTkButton(

            self.schedule_window,
            text="Save Schedule",
            height=30,
            width=140,
            corner_radius=12,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            command=self.save_sched
            )
        

        save_btn.grid(
            row=5,
            column=1,
            padx=15,
            pady=(0, 15),
            sticky="w"
        )

        delete_btn = ctk.CTkButton(
            self.schedule_window,
            text="Delete",
            height=30,
            width=140,
            corner_radius=12,
            fg_color="#3B82F6",
            hover_color="#DC2626",
        )
           
        
        delete_btn.grid(
            row=5,
            column=0,
            padx=15,
            pady=(0, 15),
            sticky="w"
        )
        #=====================================
         #          CLOSE BUTTON 
         #=====================================

        close_btn = ctk.CTkButton(
            self.top_frame,
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



    def save_sched(self):
            time = self.time_entry.get()
            title    =  self.title_entry.get()
            priority = self.priority_menu.get()
            category  = self.category_menu.get()
            schedule = self.schedule_textbox.get("1.0", "end-1c")
            date = self.date_form.cget("text")


            save_schedule(None,title,schedule,date,time,priority,category, False)
    
        
    
            

       


            
         



         
      





        



      