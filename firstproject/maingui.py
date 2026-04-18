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
      
        



        #====================== Content  ============

        self.content = ctk.CTkFrame(self.main_frame, corner_radius= 0,fg_color="#FFFFFF")
        self.content.grid(row=0, column=1, sticky="nsew")

        box1 = ctk.CTkFrame(
            self.content,
            width=380,
            height=120,
            corner_radius=15,
            fg_color="#F3F4F6"
                            )
        
        box2 = ctk.CTkFrame(
            self.content,
            width=380,
            height=120,
            corner_radius=15,
            fg_color="#E5E7EB"
                            )


        self.dash_label = ctk.CTkLabel(
            self.content,
            text="Dashboard",
            text_color="#111827",
            font=("Segoe UI", 24, "bold"))
        

        
        self.dash_label.grid(row=0, column=0, columnspan=5, pady=40, sticky="new" )
        box1.grid(row=2, column=1, padx=30, pady=20)
        box1.grid_propagate(False)

        box2.grid(row=2, column=4, padx=30, pady=20)
        box2.grid_propagate(False)

       



app = App()
app.mainloop()