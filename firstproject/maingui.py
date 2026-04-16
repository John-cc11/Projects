import customtkinter as ctk
from pathlib import Path
from PIL import Image

BASE_DIR  = Path(__file__).parent

ASSETS = BASE_DIR / "sidebar_images"

def load_icon(filename, size=(25,25)):
    return ctk.CTkImage(Image.open(ASSETS / filename), size=size)
    


ctk.set_appearance_mode("dark")      
ctk.set_default_color_theme("blue")   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Library Management System")
        self.geometry("1000x600")  
        self.minsize(800, 500)
        self.resizable(True, True)

        # ====================== MAIN FRAME ======================
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # make window expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        
        #=================== sidebar Functions ===================
        
        
        def show_sidebar(self, target_width):
            current_width = self.sidebar.winfo_width()
            step = 10

            if current_width < target_width:
                new_width = min(current_width + step, target_width)
            else:
                new_width = max(current_width - step, target_width)

            self.sidebar.configure(width=new_width)

            if new_width != target_width:
                self.sidebar.after(10, lambda: self.show_sidebar(target_width))


        

        # ====================== SIDEBAR configure ======================

        self.sidebar = ctk.CTkFrame(self.main_frame, width=180, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(99, weight=1)

        self.sidebar_width = 180
        self.colapse_width = 53

        self.sidebar_expanded =  False

        self.sidebar.configure(width=self.colapse_width)
        self.sidebar.grid_propagate(False)
        # ====================== CONTENT ======================
        self.content = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color="#18181B")
        self.content.grid(row=0, column=1, sticky="nsew")

        # make content expand
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # ====================== SIDEBAR ITEMS ======================
        self.sidebar_buttons = []
        self.sidebar_image = []
       



        signout_logo = load_icon("signout.png")
        self.sidebar_image.append(signout_logo)
       
        sidebar_items = [
                ("Dashboard", "dashboard.png"),
                ("Books", "books.png"),
                ("Users", "Users.png"),
                ("Borrow", "borrow.png"),
                ("Reports", "reports.png"),
                ("Settings", "settings.png")
                        ]
        
        self.lastbtn = ctk.CTkButton(
            self.sidebar, 
            text="Sign Out",
            image=signout_logo,
            compound="left",
            anchor="w",
            fg_color="transparent",
            font=("sans-serif",18)
            )
        
        

        for i, (name,icon_file) in enumerate(sidebar_items, start=3):  

            icon = load_icon(icon_file)
            self.sidebar_image.append(icon)

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


        self.lastbtn.grid(row=100, column=0, pady=8, padx=10,sticky="ew")
        

        # ====================== CONTENT ======================
        self.main_label = ctk.CTkLabel(self.content, text="Dashboard", font=("Arial", 24))
        self.main_label.grid(row=0, column=0, pady=40)

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)


app = App()
app.mainloop()