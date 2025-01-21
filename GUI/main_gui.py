import customtkinter
import tkinter

class ReminderInfoFrame(customtkinter.CTkFrame):
    def __init__(self, master, corner_radius = 8):
        super().__init__(master, corner_radius=corner_radius)

        self.reminder_name_var = tkinter.StringVar()
        self.reminder_desc_var = tkinter.StringVar()
        self.reminder_date_var = tkinter.StringVar()
        self.reminder_link_var = tkinter.StringVar()
        self.reminder_repeat_time_var = tkinter.IntVar(value=1)
        self.reminder_end_repeat_time_var = tkinter.IntVar(value=1)
        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder info", font=self.TITLE_FONT)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=4, pady=(10, 2), sticky="we")

        self.name_label = customtkinter.CTkLabel(self, text="Name", font=self.SUBTITLE_FONT)
        self.name_label.grid(row=1, column=0, padx=10, pady=2, sticky="w")
        self.name_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_name_var)
        self.name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.desc_label = customtkinter.CTkLabel(self, text="Description", font=self.SUBTITLE_FONT)
        self.desc_label.grid(row=2, column=0, padx=10, pady=2, sticky="w")
        self.desc_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_desc_var)
        self.desc_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.date_label = customtkinter.CTkLabel(self, text="Date", font=self.SUBTITLE_FONT)
        self.date_label.grid(row=3, column=0, padx=10, pady=2, sticky="w")
        self.date_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_date_var)
        self.date_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.link_label = customtkinter.CTkLabel(self, text="Link", font=self.SUBTITLE_FONT)
        self.link_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")
        self.link_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_link_var)
        self.link_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.repeat_label = customtkinter.CTkLabel(self, text="Repeat?", font=self.SUBTITLE_FONT)
        self.repeat_label.grid(row=5, column=0, padx=10, pady=(50,2), sticky="w")
        self.repeat_checkbox = customtkinter.CTkCheckBox(self, text="", command=self.toggle_repeat)
        self.repeat_checkbox.grid(row=5, column=1, padx=10, pady=(50,2), sticky="we")

        self.repeat_label = customtkinter.CTkLabel(self, text="Repeat every", font=self.SUBTITLE_FONT)
        self.repeat_label.grid(row=6, column=0, padx=10, pady=2, sticky="w")
        self.repeat_optMenu_num = customtkinter.CTkOptionMenu(self, values=[str(x) for x in range(1,8)], variable=self.reminder_repeat_time_var, state="disabled")
        self.repeat_optMenu_num.grid(row=6, column=1, padx=10, pady=2, sticky="we")
        self.repeat_time_label = customtkinter.CTkLabel(self, text="days", font=self.NORMAL_FONT)
        self.repeat_time_label.grid(row=6, column=2, padx=10, pady=2, sticky="w")

        self.end_repeat_label = customtkinter.CTkLabel(self, text="End repeat", font=self.SUBTITLE_FONT)
        self.end_repeat_label.grid(row=7, column=0, padx=10, pady=2, sticky="w")
        self.end_repeat_checkbox = customtkinter.CTkCheckBox(self, text="", command=self.toggle_end_repeat)
        self.end_repeat_checkbox.grid(row=7, column=1, padx=10, pady=2, sticky="we")

        self.end_after_label = customtkinter.CTkLabel(self, text="End after", font=self.SUBTITLE_FONT)
        self.end_after_label.grid(row=8, column=0, padx=10, pady=2, sticky="w")
        self.end_after_optMenu_num = customtkinter.CTkOptionMenu(self, values=[str(x) for x in range(1,41)], variable=self.reminder_end_repeat_time_var, state="disabled")
        self.end_after_optMenu_num.grid(row=8, column=1, padx=10, pady=2, sticky="we")
        self.end_after_time_label = customtkinter.CTkLabel(self, text="repetitions", font=self.NORMAL_FONT)
        self.end_after_time_label.grid(row=8, column=2, padx=10, pady=2, sticky="w")

        self.create_reminder_button = customtkinter.CTkButton(self, text="Create reminder", font=self.NORMAL_FONT, command=self.get_reminder_data)
        self.create_reminder_button.grid(row=9, column=0, columnspan=3, padx=10, pady=(4,10), sticky="s")

    def toggle_repeat(self) -> None:
        if self.repeat_checkbox.get(): self.repeat_optMenu_num.configure(state="normal")
        else: self.repeat_optMenu_num.configure(state="disabled")

    def toggle_end_repeat(self) -> None:
        if self.end_repeat_checkbox.get(): self.end_after_optMenu_num.configure(state="normal")
        else: self.end_after_optMenu_num.configure(state="disabled")

    def get_reminder_data(self) -> list[str]:
        data: list[str] = list()
        data.append(self.reminder_name_var.get())
        data.append(self.reminder_desc_var.get())
        data.append(self.reminder_date_var.get())
        data.append(self.reminder_link_var.get())
        data.append(self.repeat_checkbox.get())
        data.append(self.reminder_repeat_time_var.get())
        data.append(self.end_repeat_checkbox.get())
        data.append(self.reminder_end_repeat_time_var.get())
        print(data)
        return data


class ReminderDisplayFrame(customtkinter.CTkFrame):
    def __init__(self, master, corner_radius = 8):
        super().__init__(master,corner_radius=corner_radius)

        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder display frame", font=self.TITLE_FONT)
        self.title_label.grid(row=0, column=0, padx=10, pady=2, sticky="we")

class App(customtkinter.CTk):
    WIDTH: int = 1000
    HEIGHT: int = 500

    def __init__(self):
        super().__init__()

        self.title("Reminders")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        # =================================== Frames ===================================

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=400)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ReminderInfoFrame(self)
        self.left_frame.grid(row=0, column=0, padx=(6,3), pady=6, sticky="nswe")

        #TODO Replace this frame with a frame capable of putting the reminders' information
        self.right_frame = ReminderDisplayFrame(self)
        self.right_frame.grid(row=0, column=1, padx=(3,6), pady=6, sticky="nswe")

if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()