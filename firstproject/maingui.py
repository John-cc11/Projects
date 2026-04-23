import customtkinter as ctk
from pathlib import Path
from PIL import Image

ctk.set_appearance_mode("dark")      
ctk.set_default_color_theme("blue")   

#==================== icons  = ===========================
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "images/sidebar_images"

def load_icon(filename, size=(20, 20)):
    return ctk.CTkImage(Image.open(ASSETS / filename), size=size)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

      
        self.title("Library Management System")
        self.geometry("1000x600")  
        self.minsize(1040, 500)

     
        self.resizable(True, True)

     
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        #====================== sidebar ============

        self.sidebar = ctk.CTkFrame(self.main_frame,fg_color="#F3F4F6", width=180,corner_radius=0)
        self.sidebar.grid(row=0, column=0,sticky="ns")
        self.sidebar.grid_rowconfigure(1, minsize=55)
        self.sidebar.grid_propagate(False)

        self.main_frame.grid_columnconfigure(0, weight=0, minsize=60)
        
       

        #===================== sidebar menu ================

       



        self.sidebar_logo = ctk.CTkLabel(
            self.sidebar,
            text="📚    Library",
            compound="left",
            font=("Segoe UI", 20, "bold"),
            width=180,
            text_color="#111827",
            fg_color="transparent",

        )
       
        self.sidebar_buttons = []
        self.sidebar_icons = []

        sidebar_items = [
            ("   Dashboard", "dashboard.png"),
            ("   Books", "books.png"),
            ("   Users", "Users.png"),
            ("   Borrow", "borrow.png"),
            ("   Reports", "reports.png"),
            ("   Settings", "settings.png")
        ]

        for i, (name, icon_file) in enumerate(sidebar_items, start=4):

            icon = load_icon(icon_file)
            self.sidebar_icons.append(icon)

            btn = ctk.CTkButton(
                self.sidebar,
                text=name,
                image=icon,
                compound="left",
                anchor="w",
                fg_color="transparent",
                hover_color="#E5E7EB",
                text_color="#111827",
                font=("Segoe UI", 18),
            )
    

            btn.grid(row=i, column=0, pady=15, padx=20)
            self.sidebar_buttons.append((btn, name))
        

        self.sidebar_logo.grid(row=0, column=0, pady=(30, 15),sticky="w")
      
        



        #====================== dashboard_content  ============

        self.dashboard_content = ctk.CTkFrame(self.main_frame, corner_radius= 0,fg_color="#FFFFFF")
        
        self.dashboard_content.grid(row=0, column=1, sticky="nsew")
        self.dashboard_content.grid_columnconfigure((0,1,2,3), weight=1)
        self.dashboard_content.grid_rowconfigure((0,1,2,3), weight=1)
       
        self.dashboard_label = ctk.CTkLabel(
            self.dashboard_content,
            text_color="#111827",
            text="Dashboard", 
            font=("Segoe UI", 40, "bold"))


        self.dashboard_label.grid(row=0, column=0, columnspan=4,sticky="n", pady=(20, 10))

        #==================== dashbaord boxes ==============

        for i in range(4):
            self.dashboard_content.grid_columnconfigure(i, weight=1)

        for i in range(3):
            self.dashboard_content.grid_columnconfigure(i, weight=1)



        self.box1 = ctk.CTkFrame(self.dashboard_content, fg_color="#F87171", corner_radius=15)
        self.box2 = ctk.CTkFrame(self.dashboard_content, fg_color="#60A5FA", corner_radius=15)
        self.box3 = ctk.CTkFrame(self.dashboard_content, fg_color="#34D399", corner_radius=15)
        self.box4 = ctk.CTkFrame(self.dashboard_content, fg_color="#FBBF24", corner_radius=15)
        self.box5 = ctk.CTkFrame(self.dashboard_content, fg_color="#A78BFA", corner_radius=15)

        # small boxes
        self.box1.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.box2.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")
        self.box3.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

        # wide box
        self.box4.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

        # tall box
        self.box5.grid(row=1, column=3, rowspan=2, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()