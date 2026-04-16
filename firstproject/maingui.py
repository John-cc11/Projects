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

        self.sidebar = ctk.CTkFrame(self.main_frame, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.sidebar_width = 180
        self.collapsed_width = 60

        self.animating = False
        self.sidebar_expanded = False
        
       
    
        #====================== Content  ============

        self.content = ctk.CTkFrame(self.main_frame, corner_radius= 0,fg_color="#18181B")
        self.content.grid(row=0, column=1, sticky="nsew")

        

        #===================== sidebar menu ================
        self.sidebar_buttons = []
        self.sidebar_icons = []

        sidebar_items = [
            ("Dashboard", "dashboard.png"),
            ("Books", "books.png"),
            ("Users", "Users.png"),
            ("Borrow", "borrow.png"),
            ("Reports", "reports.png"),
            ("Settings", "settings.png")
        ]

        for i, (name, icon_file) in enumerate(sidebar_items, start=1):

            icon = load_icon(icon_file)
            self.sidebar_icons.append(icon)

            btn = ctk.CTkButton(
                self.sidebar,
                text=name,
                image=icon,
                compound="left",
                anchor="w",
                width=180,
                fg_color="transparent",
                font=("sans-serif", 18)
            )

            btn.grid(row=i, column=0, pady=8, padx=10, sticky="ew")
            self.sidebar_buttons.append((btn, name))
        


        self.main_label = ctk.CTkLabel(self.content, text="Dashboard", font=("Arial", 24))
        self.main_label.grid(pady=40)
       



app = App()
app.mainloop()