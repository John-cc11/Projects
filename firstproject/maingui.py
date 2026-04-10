import customtkinter as ctk


ctk.set_appearance_mode("dark")      
ctk.set_default_color_theme("blue")   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

      
        self.title("Library Management System")
        self.geometry("1000x600")  
        self.minsize(800, 500)

     
        self.resizable(True, True)

     
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        #====================== sidebar ============
        self.sidebar = ctk.CTkFrame(self.main_frame, width=200, corner_radius=0)
        self.sidebar.pack(side = "left", fill = "y")

        #====================== Content  ============

        self.content = ctk.CTkFrame(self.main_frame, corner_radius= 0)
        self.content.pack(side ="left", fill="both", expand=True)

        self.side_label = ctk.CTkLabel(self.sidebar, text="MENU")
        self.side_label.pack(pady=20)

        self.main_label = ctk.CTkLabel(self.content, text="Dashboard", font=("Arial", 24))
        self.main_label.pack(pady=40)
       



app = App()
app.mainloop()