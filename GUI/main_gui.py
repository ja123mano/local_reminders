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
        self.name_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_name_var, fg_color="grey10")
        self.name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.desc_label = customtkinter.CTkLabel(self, text="Description", font=self.SUBTITLE_FONT)
        self.desc_label.grid(row=2, column=0, padx=10, pady=2, sticky="w")
        self.desc_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_desc_var, fg_color="grey10")
        self.desc_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.date_label = customtkinter.CTkLabel(self, text="Date", font=self.SUBTITLE_FONT)
        self.date_label.grid(row=3, column=0, padx=10, pady=2, sticky="w")
        self.date_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_date_var, fg_color="grey10")
        self.date_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.link_label = customtkinter.CTkLabel(self, text="Link", font=self.SUBTITLE_FONT)
        self.link_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")
        self.link_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_link_var, fg_color="grey10")
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
        self.end_repeat_checkbox = customtkinter.CTkCheckBox(self, text="", command=self.toggle_end_repeat, state="disabled")
        self.end_repeat_checkbox.grid(row=7, column=1, padx=10, pady=2, sticky="we")

        self.end_after_label = customtkinter.CTkLabel(self, text="End after", font=self.SUBTITLE_FONT)
        self.end_after_label.grid(row=8, column=0, padx=10, pady=2, sticky="w")
        self.end_after_optMenu_num = customtkinter.CTkOptionMenu(self, values=[str(x) for x in range(1,41)], variable=self.reminder_end_repeat_time_var, state="disabled")
        self.end_after_optMenu_num.grid(row=8, column=1, padx=10, pady=2, sticky="we")
        self.end_after_time_label = customtkinter.CTkLabel(self, text="repetitions", font=self.NORMAL_FONT)
        self.end_after_time_label.grid(row=8, column=2, padx=10, pady=2, sticky="w")

    def toggle_repeat(self) -> None:
        if self.repeat_checkbox.get():
            self.repeat_optMenu_num.configure(state="normal")
            self.end_repeat_checkbox.configure(state="normal")
        else:
            self.repeat_optMenu_num.configure(state="disabled")
            self.end_repeat_checkbox.configure(state="disabled")

        self.toggle_end_repeat()

    def toggle_end_repeat(self) -> None:
        if self.repeat_checkbox.get() and self.end_repeat_checkbox.get():
            self.end_after_optMenu_num.configure(state="normal")
        else:
            self.end_after_optMenu_num.configure(state="disabled")

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
        # print(data)
        return data

    def validate_main_data(self) -> bool:
        validate_flag: int = True

        if self.reminder_name_var.get() == "" or self.reminder_name_var.get() == "PLEASE GIVE A NAME":
            self.reminder_name_var.set("PLEASE GIVE A NAME")
            self.name_entry.configure(fg_color="brown4")
            validate_flag = False
        else: self.name_entry.configure(fg_color="grey10")
        
        if self.reminder_desc_var.get() == "" or self.reminder_desc_var.get() == "PLEASE GIVE A DESCRIPTION":
            self.reminder_desc_var.set("PLEASE GIVE A DESCRIPTION")
            self.desc_entry.configure(fg_color="brown4")
            validate_flag = False
        else: self.desc_entry.configure(fg_color="grey10")
        
        if self.reminder_date_var.get() == "" or self.reminder_date_var.get() == "PLEASE GIVE A DATE":
            self.reminder_date_var.set("PLEASE GIVE A DATE")
            self.date_entry.configure(fg_color="brown4")
            validate_flag = False
        else: self.date_entry.configure(fg_color="grey10")
        
        return validate_flag


class ReminderDisplayFrame(customtkinter.CTkFrame):
    def __init__(self, master, corner_radius = 8):
        super().__init__(master,corner_radius=corner_radius)

        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        self.grid_columnconfigure((1,2,3,4), weight=1)
        self.grid_columnconfigure((1,2,3,4,5,6), minsize=100)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder display frame", font=self.TITLE_FONT)
        self.title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=(10,2), sticky="we")

        self.select_label = customtkinter.CTkLabel(self, text="Select", font=self.SUBTITLE_FONT)
        self.select_label.grid(row=1, column=0, padx=10, pady=2, sticky="we")

        self.name_label = customtkinter.CTkLabel(self, text="Name", font=self.SUBTITLE_FONT)
        self.name_label.grid(row=1, column=1, padx=10, pady=2, sticky="we")

        self.description_label = customtkinter.CTkLabel(self, text="Description", font=self.SUBTITLE_FONT)
        self.description_label.grid(row=1, column=2, padx=10, pady=2, sticky="we")

        self.link_label = customtkinter.CTkLabel(self, text="Link", font=self.SUBTITLE_FONT)
        self.link_label.grid(row=1, column=3, padx=10, pady=2, sticky="we")

        self.date_label = customtkinter.CTkLabel(self, text="Next remind", font=self.SUBTITLE_FONT)
        self.date_label.grid(row=1, column=4, padx=10, pady=2, sticky="we")

        self.constancy_label = customtkinter.CTkLabel(self, text="Remind every", font=self.SUBTITLE_FONT)
        self.constancy_label.grid(row=1, column=5, padx=10, pady=2, sticky="we")

        self.repeat_label = customtkinter.CTkLabel(self, text="# of repeats", font=self.SUBTITLE_FONT)
        self.repeat_label.grid(row=1, column=6, padx=10, pady=2, sticky="we")


class App(customtkinter.CTk):
    WIDTH: int = 1300
    HEIGHT: int = 500
    RIGHT_FRAME_HEADERS: int = 2
    REMINDERS: int = 0 + RIGHT_FRAME_HEADERS

    def __init__(self):
        super().__init__()

        self.title("Reminders")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        # =================================== Frames ===================================

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=400)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ReminderInfoFrame(self)
        self.left_frame.grid(row=0, column=0, padx=(6,3), pady=(6,2), sticky="nswe")

        self.create_reminder_button = customtkinter.CTkButton(self, text="Create reminder", font=self.NORMAL_FONT, command=self.create_reminder)
        self.create_reminder_button.grid(row=1, column=0, padx=10, pady=(2,6), sticky="nswe")

        self.right_frame = ReminderDisplayFrame(self)
        self.right_frame.grid(row=0, column=1, rowspan=2, padx=(3,6), pady=6, sticky="nswe")

    def create_reminder(self) -> None:
        if not self.left_frame.validate_main_data():
            return None

        # TODO: Wrap this functionality within class so all the widgets created here are part of an object of that class

        reminder_data: list[str] = self.left_frame.get_reminder_data()
        name: str = reminder_data[0]
        description: str = reminder_data[1]
        date: str = reminder_data[2]
        link: str = reminder_data[3]
        days: str = "NA"
        repetitions: str = "None"

        if link == "": link = "NA"
        if reminder_data[4]:
            days: int = f"{reminder_data[5]} day(s)"
            if reminder_data[6]: repetitions: int = reminder_data[7]
            else: repetitions = "Infinite"

        self.select_checkbox = customtkinter.CTkCheckBox(self.right_frame, width=35, text="")
        self.select_checkbox.grid(row=App.REMINDERS, column=0, padx=10, sticky="e")

        self.reminder_name = customtkinter.CTkLabel(self.right_frame, text=name, font=self.NORMAL_FONT)
        self.reminder_name.grid(row=App.REMINDERS, column=1, sticky="we")

        self.reminder_desc = customtkinter.CTkLabel(self.right_frame, text=description, font=self.NORMAL_FONT)
        self.reminder_desc.grid(row=App.REMINDERS, column=2, sticky="we")

        self.reminder_link = customtkinter.CTkLabel(self.right_frame, text=link, font=self.NORMAL_FONT)
        self.reminder_link.grid(row=App.REMINDERS, column=3, sticky="we")

        self.reminder_date = customtkinter.CTkLabel(self.right_frame, text=date, font=self.NORMAL_FONT)
        self.reminder_date.grid(row=App.REMINDERS, column=4, sticky="we")

        self.reminder_days = customtkinter.CTkLabel(self.right_frame, text=days, font=self.NORMAL_FONT)
        self.reminder_days.grid(row=App.REMINDERS, column=5, sticky="we")

        self.reminder_repetitions = customtkinter.CTkLabel(self.right_frame, text=repetitions, font=self.NORMAL_FONT)
        self.reminder_repetitions.grid(row=App.REMINDERS, column=6, sticky="we")

        App.REMINDERS += 1
        return None

if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()