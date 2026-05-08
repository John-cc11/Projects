import customtkinter as ctk
from pathlib import Path
from PIL import Image
from Schedule import SchedulingPage


ctk.set_appearance_mode("dark")      
ctk.set_default_color_theme("blue")   

#==================== icons  = ===========================
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "../Assets/images/sidebar_images"

def load_icon(filename, size=(20, 20)):
    return ctk.CTkImage(Image.open(ASSETS / filename), size=size)

class App(ctk.CTk):
    #======================== functions
    def show_page(self, name):
            if name in self.pages:
                self.pages[name].tkraise()


    def __init__(self):
        super().__init__()


   
        self.title("Library Management System")
        self.geometry("1000x600")  
        self.minsize(1040, 500)
        #===== default frame ====
     
        self.resizable(True, True)
        

     
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.grid_columnconfigure(0, weight=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)




        #================ frames =============
        self.pages_list = {
            "dashboard": lambda parent: ctk.CTkFrame(parent, fg_color="#FFFFFF"),
            "books": lambda parent: ctk.CTkFrame(parent, fg_color="#FFFFFF"),
            "users": lambda parent: ctk.CTkFrame(parent, fg_color="#FFFFFF"),
            "borrow": lambda parent: ctk.CTkFrame(parent, fg_color="#FFFFFF"),
            "scheduling": lambda parent: SchedulingPage(parent).frame,
            "settings": lambda parent: ctk.CTkFrame(parent, fg_color="#FFFFFF"),
        }
        self.pages = {}

        for name, builder in self.pages_list.items():
            frame = builder(self.main_frame)   
            self.pages[name] = frame

        #=========== functionssss =============
        
        self.pages["dashboard"].grid_columnconfigure((0,1,2,3), weight=1)
        self.pages["dashboard"].grid_rowconfigure((0,1,2,3), weight=1)
        self.pages["dashboard"].grid(row=0, column=1, sticky="nsew")
        self.pages["dashboard"].tkraise()

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
            ("   Dashboard", "dashboard.png", "dashboard"),
            ("   Books", "books.png", "books"),
            ("   Users", "Users.png", "users"),
            ("   Borrow", "borrow.png", "borrow"),
            ("   Scheduling", "reports.png", "scheduling"),
            ("   Settings", "settings.png", "settings")
        ]

        for i, (name, icon_file, key) in enumerate(sidebar_items, start=4):

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
                command=lambda k=key: self.show_page(k)
            )
    

            btn.grid(row=i, column=0, pady=15, padx=20)
            self.sidebar_buttons.append((btn, name))
        

        self.sidebar_logo.grid(row=0, column=0,sticky="w")
      
        
   
        #====================== Contents  ============
        
       
        #======================= Dashboard Content =============== 
        self.dashboard_label = ctk.CTkLabel(
            self.pages["dashboard"],
            text_color="#111827",
            text="Dashboard", 
            font=("Segoe UI", 28, "bold"))


        self.dashboard_label.grid(row=0, column=0,sticky="n", pady=(20, 10))
        #==================== dashbaord boxes ==============
        boxes = [
        {"color": "#F87171", "row": 2, "col": 0},
        {"color": "#60A5FA", "row": 2, "col": 1},
        {"color": "#34D399", "row": 2, "col": 2},
        {"color": "#FBBF24", "row": 1, "col": 0, "columnspan": 3},
        {"color": "#A78BFA", "row": 1, "col": 3, "rowspan": 2},
                ]
        

        self.boxes = []

        for b in boxes:
            shadow = ctk.CTkFrame(
            self.pages["dashboard"],
            fg_color="#E5E7EB",
            corner_radius = 20
            )

            shadow.grid(
                row=b["row"],
                column=b["col"],
                rowspan=b.get("rowspan", 1),
                columnspan=b.get("columnspan", 1),
                padx=22,
                pady=20,
                sticky="nsew"
            )
            card = ctk.CTkFrame(
                shadow,
                fg_color="#F9FAFB",
                corner_radius=10
            )

            card.place(relx=0, rely=0, relwidth=1, relheight=1)

            
            accent = ctk.CTkFrame(
                card,
                fg_color=b["color"],
                height=10,
                corner_radius=10
            )
            accent.pack(fill="x", padx=15, pady=(10, 5))

            self.boxes.append(card)




app = App()
app.mainloop()