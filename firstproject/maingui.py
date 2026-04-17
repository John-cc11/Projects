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
        self.minsize(800, 500)

     
        self.resizable(True, True)

     
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        #====================== sidebar ============

        self.sidebar = ctk.CTkFrame(self.main_frame, width=60,corner_radius=0)
        self.sidebar.grid(row=0, column=0,sticky="ns")
        self.sidebar.grid_rowconfigure(1, minsize=55)
        self.sidebar.grid_propagate(False)

        self.main_frame.grid_columnconfigure(0, weight=0, minsize=60)

       
    
        #====================== Content  ============

        self.content = ctk.CTkFrame(self.main_frame, corner_radius= 0,fg_color="#18181B")
        self.content.grid(row=0, column=1, sticky="nsew")

        

        #===================== sidebar menu ================

        self.sidebar_logo = ctk.CTkLabel(
            self.sidebar,
            text="📚      Library",
            compound="left",
            font=("Segoe UI", 20, "bold"),
            width=180,
            fg_color="transparent"

        )
       
        self.sidebar_buttons = []
        self.sidebar_icons = []

        sidebar_items = [
            ("   Dashboard", "dashboard.png"),
            ("   Books", "books.png"),
            ("   Users", "Users.png"),
            ("   Borrow", "borrow.png"),
            ("   Reports", "reports.png"),
            ("Settings", "settings.png")
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
                font=("Segoe UI", 18)
            )

            btn.grid(row=i, column=0, pady=15, padx=20)
            self.sidebar_buttons.append((btn, name))
        

        self.sidebar_logo.grid(row=0, column=0, pady=(30, 15),sticky="w")
        self.main_label = ctk.CTkLabel(self.content, text="Dashboard", font=("Segoe UI", 24))
        self.main_label.grid(pady=40)

       



app = App()
app.mainloop()