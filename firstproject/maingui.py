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

        
        self.label = ctk.CTkLabel(
            self.main_frame,
            text="Welcome to Library System",
            font=("Arial", 24)
        )
        self.label.pack(pady=40)



app = App()
app.mainloop()