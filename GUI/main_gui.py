import customtkinter

class ReminderInfoFrame(customtkinter.CTkFrame):
    def __init__(self, master, corner_radius = 8):
        super().__init__(master, corner_radius)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder info")
        self.title_label.grid(row=0, column=0, columnspan=3, padx=4, pady=(10, 2), sticky="we")

        self.name_label = customtkinter.CTkLabel(self, text="Name")
        self.name_label.grid(row=1, column=0, padx=10, pady=2, sticky="w")

        self.desc_label = customtkinter.CTkLabel(self, text="Description")
        self.desc_label.grid(row=2, column=0, padx=10, pady=2, sticky="w")

        self.date_label = customtkinter.CTkLabel(self, text="Date")
        self.date_label.grid(row=3, column=0, padx=10, pady=2, sticky="w")

        self.link_label = customtkinter.CTkLabel(self, text="Link")
        self.link_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")

        self.recurrent_label = customtkinter.CTkLabel(self, text="Recurrent")
        self.recurrent_label.grid(row=5, column=0, padx=10, pady=2, sticky="w")

        self.repeat_label = customtkinter.CTkLabel(self, text="Repeat every")
        self.repeat_label.grid(row=6, column=0, padx=10, pady=(2,4), sticky="w")

        self.create_reminder_button = customtkinter.CTkButton(self, text="Create reminder")
        self.create_reminder_button.grid(row=7, column=0, columnspan=3, padx=10, pady=(4,10), sticky="s")

class App(customtkinter.CTk):
    WIDTH: int = 800
    HEIGHT: int = 500

    def __init__(self):
        super().__init__()

        self.title("Reminders")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # =================================== Frames ===================================

        self.left_frame = ReminderInfoFrame(self)
        self.left_frame.grid(row=0, column=0, padx=(10,3), pady=10, sticky="ns")

        #TODO Replace this frame with a frame capable of putting the reminders' information
        self.right_frame = ReminderInfoFrame(self)
        self.right_frame.grid(row=0, column=1, padx=(3,10), pady=10, sticky="nswe")

if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()